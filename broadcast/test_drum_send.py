import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver(request):
    # создание драйвера. Инициализация браузера
    #profile - это кэш, который каждый раз очищаем
    # profile = webdriver.ChromeOptions()
    # profile.set_preference("browser.cache.disk.enable", False)
    # profile.set_preference("browser.cache.memory.enable", False)
    # profile.set_preference("browser.cache.offline.enable", False)
    # profile.set_preference("network.http.use-cache", False)
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    # Переход на страницу виртуалки
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 30)

    driver.get("http://192.168.1.33:8080/login")
    driver.implicitly_wait(10)
    #wait.until(EC.presence_of_element_located((By.TAG_NAME, "div[class='cs-app__footer flex-simple']")))
    # Поиск полей Логин, Пароль, нажатие кнопки
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "button[class='btn btn-primary margin-top enter']")))
    driver.find_element_by_tag_name("input#user").send_keys("admin")
    #driver.implicitly_wait(10)
    #driver.find_element_by_tag_name("input#password").send_keys("admindflvbyt")

    driver.find_element_by_tag_name("input#password").send_keys("admindjrheuflvbyf") #админвокругадмина

    #driver.implicitly_wait(10)
    driver.find_element_by_tag_name("button[class='btn btn-primary margin-top enter']").send_keys(Keys.ENTER)
    #driver.implicitly_wait(10)
    WebDriverWait(driver, 15)

    wait.until(EC.title_is("ТранспортТВ - Панель управления"))


def wait_time():

    WebDriverWait(driver, 10)

    return time.sleep(5)


def test_drum_send(driver):
    """Отправка барабана вещания"""

    # Словарь всех названий рубрик

    rubric_dict = {'Авиарейсы': 'Flights', 'Активны гражданин': 'ActiveCitizen', 'Анонс матча': 'MatchPreview',
                   'Афиша': 'Afisha', 'Аэросъемка': 'AERIAL', 'Видео из внешнего источника': 'StreamVideo',
                   'Видеопоток': 'VideoRegistrator', 'Викторина': 'QUIZ', 'Вопрос-ответ': 'qa', 'Города мира': 'goroda',
                   'Гороскоп':'horoscope', 'Достопримечательности': 'SightInfo', 'Знаете ли вы что': 'dykt',
                   'Изменения в работе НГПТ': 'CHANGES_NGPT', 'Инстаграм': 'instagram',
                   'Интересное видео': 'INTEREST_VIDEO', 'Интересный факт': 'interestingFact',
                   'МЧС': 'InformationFromMCHS', 'Календарь': 'CalendarEvent',
                   'Календарь турнира': 'TournamentCalendar', 'Камеры видеорегистратора': 'IpCamera',
                   'Контент от заказчика': 'RubricOfPAT', 'Курсы криптовалют': 'CryptCurrency', 'Маршрут': 'marshrut',
                   'Матч онлайн': 'MatchOnline', 'Nebo.Digital': 'NeboDigital', 'Новости': 'News',
                   'Контент от МГТ': 'MGT_CONTENT', 'Обратный отсчет':'COUNTDOWN', 'Опрос': 'POLL',
                   'Остановочная информация': 'StopInfo', 'Памятный день-Именины': 'BirthDay', 'Погода': 'weather',
                   'Поздравление': 'CONGRATULATION', 'Полезный совет': 'sovet', 'Прямое включение': 'DirectInclusion',
                   'Результат матча': 'MatchResult', 'Рекламный модуль': 'AdvertisingModule',
                   'Служебная информация': 'ServiceInformation', 'Таблица группового этапа': 'TournamentGroupStage',
                   'Твиттер': 'twitter', 'Точное время': 'ExactTime', 'ТранспортТВ': 'TRANSPORT_TV',
                   'Транспортная схема': 'TransportSchema', 'Узнай Москву': 'SightsOfMoskow',
                   'Фотоцитата': 'photoquote', 'Соцопрос': 'VOTE'}

    test_login(driver)
    time.sleep(5)
    wait = WebDriverWait(driver, 30)

    wait.until(EC.element_to_be_clickable((By.TAG_NAME, "div[class='left-nav__menu-unit-header-title']")))

    WebDriverWait(driver, 30)

    # Эфир

    driver.find_elements_by_tag_name("div[class='left-nav__menu-unit-header-title']")[0].click()

    WebDriverWait(driver, 10)

    # Узнать процент рубрик в суточном графике

    # Суточные графики

    driver.find_element_by_tag_name("a[href='/ether/broadcastSchedule']").click()

    wait_time()

    # Заполнить поле "Название" в таблице СГ

    driver.find_elements_by_tag_name("thead input[type='text']")[0].send_keys("Moscow AutoGraph")

    WebDriverWait(driver, 10)

    driver.find_elements_by_tag_name("thead input[type='text']")[0].send_keys(Keys.ENTER)

    WebDriverWait(driver, 10)

    wait_time()

    driver.find_element_by_tag_name("i[title='Редактировать суточный график']").click()

    WebDriverWait(driver, 10)

    # Узнаем какие рубрики и процентаж

    dict_day_graph = {}

    counter_rubrics = driver.find_elements_by_tag_name("div[class='window__rubric__name']")

    counter_percents = driver.find_elements_by_tag_name("input[type='number']")

    for i in range(len(counter_rubrics)):

        dict_day_graph.update({counter_rubrics[i].get_property("outerText"): counter_percents[i].get_property("value")})

        # counter_rubrics[i].get_property("outerText")
        #
        # counter_percents[i].get_property("value")

    # Получить измененный словарь с названиями рубрик как в revolver.json

    # TODO всем чмоки в этом чатике :* Пока нихера не получается. Надо гуглить.

    for key in rubric_dict:
        if dict_day_graph[i] in rubric_dict:
            dict_day_graph.update(rubric_dict[i])

    print(dict_day_graph)

    # Управление барабанами вещания

    driver.find_element_by_tag_name("a[href='/ether/broadcastRevolvers']").click()

    WebDriverWait(driver, 10)

    # Заполнить в таблице поле "Название" и нажать Enter

    driver.find_elements_by_tag_name("thead input[type='text']")[0].send_keys("Autotest Drum")

    WebDriverWait(driver, 10)

    driver.find_elements_by_tag_name("thead input[type='text']")[0].send_keys(Keys.ENTER)

    WebDriverWait(driver, 10)

    # Нажать на разослать барабан на все МК

    driver.find_element_by_tag_name("i[class='material-icons custom-icon tip icon-normal']"
     "[data-original-title='Разослать барабан на все МК выбранного города']").click()

    WebDriverWait(driver, 10)

    # Получаем содержимое уведомлений

    list_notify = []

    ver_list_notify = []

    message_sending = driver.find_elements_by_tag_name("div[data-notify='container']")[0].get_property('innerText')

    list_notify.append(message_sending)

    wait_time()

    # TODO Попробовать удалить лишние символы из строк с помощью регулярок

    message_sending_success = driver.find_elements_by_tag_name("div[data-notify='container']")[1].get_property('innerText')

    list_notify.append(message_sending_success)

    verif_message_send = '×\nНачался процесс отправки барабана на все МК выбранного города'

    verif_message_send_success = '×\nБарабан успешно разослан на МК'

    ver_list_notify.append(verif_message_send)

    ver_list_notify.append(verif_message_send_success)

    for i in range(2):
        if list_notify[i] in ver_list_notify:
            print("\nMessage " + "\"" + list_notify[i] + "\"" + " valid")
        else:
            print("\nMessage " + "\"" + list_notify[i] + "\"" + " not valid")

