import random
import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def move_mouse_randomly(driver: webdriver) -> None:
    """
    Имитирует движение курсора мыши случайным образом, чтобы воспроизвести действия человека.

    Эта функция полезна для обхода механизмов обнаружения автоматизации,
    которые могут проверять поведение пользователя на сайте.

    Args:
        driver (webdriver): Экземпляр веб-драйвера Selenium, используемый для управления браузером.

    Behavior:
        - Выполняет несколько (по умолчанию 5) случайных движений курсора.
        - Пауза между движениями составляет 0.5 секунды для имитации естественного поведения.
        - Движения ограничены случайными смещениями по осям X и Y (в пределах от 0 до 200 пикселей).

    Example:
        from selenium import webdriver
        driver = webdriver.Chrome()
        move_mouse_randomly(driver)
    """

    action = ActionChains(driver)
    for _ in range(5):
        x_offset = random.randint(0, 200)
        y_offset = random.randint(0, 200)
        action.move_by_offset(x_offset, y_offset)
        action.perform()
        time.sleep(0.5)
