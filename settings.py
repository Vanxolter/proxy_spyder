import os
from dotenv import load_dotenv

load_dotenv()

# Email и пароль для авторизации на сайте.
# Значения можно задавать через переменные окружения в файле .env или оставить дефолтными для тестирования.
EMAIL = os.getenv("EMAIL", "tzpythondemo@domconnect.ru")
PASSWORD = os.getenv("PASSWORD", "oJanL4dc7g")

# Настройки опций для веб-драйвера.
# "--headless" запускает браузер в скрытом режиме,
# "--disable-blink-features=AutomationControlled" помогает обойти некоторые ограничения автоматизации
# "--start-maximized" запускает браузер.
OPTIONS = ("--start-maximized", "--disable-blink-features=AutomationControlled")

# Список всех доступных прокси и их описание.
PROXYS = {1: "IPv6 Proxy",
          2: "IPv4 Proxy",
          3: "IPv4 Shared Proxy",
          4: "IPv4 Premium"}

# TODO: Указать ключи PROXYS для желаемых прокси. Например, (1, 3).
WANTED_PROXYS = (3,)

# Колонки таблицы на сайте.
TABLE_COLUMNS = {1: "select",
                 2: "Тип",
                 3: "Страна",
                 4: "Логин",
                 5: "Пароль",
                 6: "IP",
                 7: "HTTP",
                 8: "SOCKS",
                 9: "Скорость",
                 10: "Истекает",
                 11: "Комментарий"}

# TODO: Указать ключи TABLE_COLUMNS для вывода нужных колонок. Например, (6, 10).
WANTED_TABLE_COLUMNS = (6, 10,)
