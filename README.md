# ProxySpyder

**ProxySpyder** — это скрипт на Python для автоматизированного сбора данных о прокси-серверах с веб-сайта [belurk.online](https://belurk.online). <br/> 
Скрипт использует Selenium для автоматизации браузера и BeautifulSoup для анализа HTML-кода страниц.

Author: Maksim Laurou ```Lavrov.python@gmail.com```<br/> 
Source link: https://github.com/Vanxolter/proxy_spyder

## 📋 Функциональность

1. **Авторизация на сайте**: Скрипт автоматически вводит учетные данные (email и пароль) для входа на сайт.
2. **Навигация по разделам сайта**: Пользователь может указать желаемые типы прокси в настройках.
3. **Сбор данных из таблиц**: Данные о прокси, такие как IP-адреса, срок действия и другие параметры, извлекаются в удобном формате.
4. **Режим "headless"**: Работа программы может выполняться без отображения окна браузера.
5. **Настройка через переменные окружения**: Скрипт использует файл `.env` для хранения конфиденциальной информации.

## 🚀 Установка и настройка

1. Убедитесь, что у вас установлен Python (рекомендуется версия 3.8 или выше).
2. Клонируйте репозиторий:<br/> 
   ```
   git clone git@github.com:Vanxolter/proxy_spyder.git 
   cd proxy_spyder
   ```
3. Установите зависимости:<br/> 
   ```pip install -r requirements.txt```
4. Создайте файл .env в корневой директории и добавьте свои учетные данные:<br/> 
   ```
   EMAIL=ваш_email
   PASSWORD=ваш_пароль
   ```
5. Убедитесь, что у вас установлен Google Chrome и соответствующий драйвер chromedriver.<br/> 
   Убедитесь, что версия драйвера совпадает с установленной версией Chrome.

## ⚙️ Конфигурация

   ### Переменные окружения
   - ```EMAIL``` — email для входа на сайт.
   - ```PASSWORD``` — пароль для входа.

   ### Настройки скрипта
   - **Типы прокси**: Укажите желаемые типы прокси в переменной ```WANTED_PROXYS``` в файле ```settings.py```. Например:<br/> 
      ```WANTED_PROXYS = (3, 4)  # IPv4 Shared Proxy и IPv4 Premium```
   - **Столбцы таблиц**: Укажите нужные столбцы данных в переменной ```WANTED_TABLE_COLUMNS```. Например:<br/> 
      ```WANTED_TABLE_COLUMNS = (6, 10)  # IP-адрес и срок действия```
   - **Режим браузера**: Чтобы запустить скрипт с отображением окна браузера, удалите опцию ```--headless``` в переменной ```OPTIONS```.

## 🖥️ Использование
   
   Для запуска программы выполните:<br/> 
   ```python main.py```<br/> 
   Программа автоматически выполнит вход, соберет данные по указанным прокси-серверам и отобразит результаты в консоли.
   
   ### Пример результата:

   ```
   Данные по IPv4 Shared Proxy:
   185.200.188.230 - 04.01.2025, 17:23
   103.127.76.222 - 04.01.2025, 17:23
   ```

## 🛠️ Зависимости
   - ```selenium``` — для управления браузером.
   - ```beautifulsoup4``` — для парсинга HTML.
   - ```lxml``` — для парсинга страниц с использованием beautifulsoup4.
   - ```python-dotenv``` — для работы с переменными окружения.<br/> 
   Установите все зависимости через файл ```requirements.txt```.

## ⚠️ Важные замечания
   - Скрипт предназначен для использования только в **легальных** целях. Убедитесь, что вы соблюдаете правила сайта [belurk.online](https://belurk.online).
   - Для корректной работы скрипта на сайт требуется доступ через учетную запись.
   - В случае изменений на сайте функционал может потребовать доработки.
