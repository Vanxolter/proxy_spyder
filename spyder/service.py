import time
import logging
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from settings import EMAIL, PASSWORD, OPTIONS, PROXYS, WANTED_PROXYS, WANTED_TABLE_COLUMNS, TABLE_COLUMNS
from spyder.driver_manager import WebDriverManager

logger = logging.getLogger(__name__)


class ProxySpyder:
    """
    Класс для автоматизации работы с сайтом belurk.online.
    Выполняет авторизацию, выбор прокси и извлечение данных из таблиц.
    """

    # Заголовки для HTTP-запросов
    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    # Путь для сохранения данных в JSON формате (пока не используется).
    path_to_json = "data/results.json"

    def __init__(self):
        """
        Инициализация объекта. Создает настройки драйвера.
        """
        self.options = self._create_driver()
        self.driver = None
        self.soup = None

    @staticmethod
    def _create_driver():
        """
        Создает объект настроек для веб-драйвера.

        :return: Экземпляр ChromeOptions с добавленными аргументами.
        """
        options = webdriver.ChromeOptions()
        [options.add_argument(argument) for argument in OPTIONS]
        return options

    def _get_soup(self):
        """
        Получает HTML-код страницы и создает объект BeautifulSoup для его обработки.

        :return: BeautifulSoup объект.
        """
        src = self.driver.page_source
        return BeautifulSoup(src, "lxml")

    def run(self):
        """
        Запуск основного сценария:
        1. Переход на сайт.
        2. Авторизация.
        3. Извлечение данных из таблиц.
        """
        with WebDriverManager(self.options) as self.driver:
            self.driver.get("https://belurk.online/")
            time.sleep(1)  # Ожидание прогрузки начальной страницы

            # Нажимаем на кнопку "Войти"
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div/div/div/div[1]/a").click()

            self._authorization()  # Авторизация

            self._working_with_tables()  # Обработка таблиц

    def _waiting_for_element(self, xpath: str, timeout: int = 5):
        """
        Ожидание элемента по XPath в течение заданного времени.

        :param xpath: XPath элемента.
        :param timeout: Время ожидания (по умолчанию 5 секунд).
        :return: Найденный элемент.
        :raises str: Если элемент не найден - "Нет данных."
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except TimeoutException as e:
            print("Нет данных.")
            # TODO: Разблокировать при разработке
            # error_message = (
            #     f"Ошибка: элемент с XPath '{xpath}' не появился в течение {timeout} секунд."
            # )
            # logger.error(error_message)
            # logger.debug("Оригинальное исключение:", exc_info=e)
            # raise TimeoutException(error_message) from e

    def _click_and_wait(self, xpath_to_click: str, xpath_to_wait: str, timeout: int = 5):
        """
        Кликает по элементу и ожидает загрузки другого элемента.

        :param xpath_to_click: XPath элемента для клика.
        :param xpath_to_wait: XPath элемента, который должен загрузиться после клика.
        :param timeout: Время ожидания (по умолчанию 5 секунд).
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                ec.element_to_be_clickable((By.XPATH, xpath_to_click))
            ).click()
            time.sleep(0.2)
            WebDriverWait(self.driver, timeout).until(
                ec.presence_of_element_located((By.XPATH, xpath_to_wait))
            )
        except TimeoutException:
            print("Нет данных.")
            # TODO: Разблокировать при разработке
            # error_message = (
            #     f"Ошибка: не удалось обработать {xpath_to_click}"
            # )
            # logger.error(error_message)
            # logger.debug("Оригинальное исключение:", exc_info=e)
            # raise TimeoutException(error_message) from e

    def _authorization(self):
        """
        Выполняет авторизацию на сайте с использованием EMAIL и PASSWORD.
        """
        email_field = self._waiting_for_element('//*[@id="signInForm"]/div[1]/div/input')
        password_field = self.driver.find_element(By.XPATH, '//*[@id="signInForm"]/div[2]/div/input')
        email_field.send_keys(EMAIL)
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.ENTER)

    def _extract_table_data(self):
        """
        Извлекает данные из таблицы на веб-странице, представленной объектом BeautifulSoup.

        Для каждой строки таблицы (tbody tr) извлекаются значения ячеек (td),
        которые затем маппируются на заранее определённые колонки, указанные в
        WANTED_TABLE_COLUMNS, и собираются в список.

        :return: Список строк, содержащих данные таблицы, в виде объединённых строк с данными.
        """
        rows = self.soup.select('table tbody tr')  # Получаем все строки таблицы
        data = []  # Список для хранения извлечённых данных
        for row in rows:
            cells = row.find_all('td')  # Извлекаем все ячейки в строке
            entry = {TABLE_COLUMNS[column]: cells[column - 1].text.strip() for column in WANTED_TABLE_COLUMNS}  # Создаём словарь из данных ячеек
            data.append(' - '.join(entry.values()))  # Формируем строку с объединёнными значениями ячеек
        return data

    def _working_with_tables(self):
        """
        Работает с таблицами на веб-странице, выбирает нужные прокси и извлекает данные.

        Для каждого прокси из WANTED_PROXYS происходит клик по соответствующему элементу на странице,
        ожидание загрузки таблицы, затем извлечение данных таблицы с помощью _extract_table_data и вывод
        полученной информации в консоль.

        :return: None
        """
        for proxy in WANTED_PROXYS:
            # Кликаем по ссылке прокси и ожидаем загрузки таблицы
            self._click_and_wait(
                f'/html/body/div[1]/div/main/div/section/div/div/a[{proxy}]',
                '/html/body/div[1]/div/main/div/div/section/div[2]/div/table'
            )

            self.soup = self._get_soup()  # Получаем HTML-код страницы
            data = self._extract_table_data()  # Извлекаем данные из таблицы

            # Выводим данные для выбранного прокси
            print(f"Данные по {PROXYS[proxy]}:")
            for entry in data:
                print(entry)  # Выводим каждую строку данных
            print()  # Печатаем пустую строку между результатами для разных прокси
