from selenium import webdriver


class WebDriverManager:
    """
    Контекстный менеджер для управления жизненным циклом веб-драйвера Selenium.

    Этот класс предоставляет удобный способ автоматического создания и закрытия
    экземпляра веб-драйвера. Когда вы используете этот класс в контексте `with`,
    веб-драйвер автоматически запускается при входе и завершает работу при выходе.

    Attributes:
        options (webdriver.ChromeOptions, optional): Опции для настройки веб-драйвера.
        driver (webdriver.Chrome, optional): Экземпляр веб-драйвера, создается при входе в контекст.
    """

    def __init__(self, options: webdriver.ChromeOptions | None = None):
        """
        Инициализация менеджера.

        Args:
            options (webdriver.ChromeOptions, optional): Опции для настройки веб-драйвера.
        """
        self.options = options
        self.driver = None

    def __enter__(self):
        """
        Создает экземпляр веб-драйвера при входе в контекст.

        Returns:
            webdriver.Chrome: Экземпляр веб-драйвера Selenium.
        """
        self.driver = webdriver.Chrome(options=self.options)
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Закрывает веб-драйвер при выходе из контекста.

        Args:
            exc_type (type, optional): Тип исключения, если оно возникло.
            exc_value (Exception, optional): Значение исключения, если оно возникло.
            traceback (traceback, optional): Трассировка исключения, если оно возникло.
        """
        if self.driver:
            self.driver.quit()
