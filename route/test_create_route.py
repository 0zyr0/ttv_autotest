import pytest
import time
import sqlalchemy as db

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sqlalchemy import create_engine

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

    driver.get("http://192.168.100.42:8080/login")
    driver.implicitly_wait(10)

    # wait.until(EC.presence_of_element_located((By.TAG_NAME, "div[class='cs-app__footer flex-simple']")))

    # Поиск полей Логин, Пароль, нажатие кнопки
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "button[class='btn btn-primary margin-top enter']")))
    driver.find_element_by_tag_name("input#user").send_keys("admin")
    # driver.implicitly_wait(10)
    driver.find_element_by_tag_name("input#password").send_keys("admindflvbyt") #админвадмине
    #driver.find_element_by_tag_name("input#password").send_keys("xnpR95BChK") # ПАТ пароль: xnpR95BChK
    # driver.implicitly_wait(10)
    driver.find_element_by_tag_name("button[class='btn btn-primary margin-top enter']").send_keys(Keys.ENTER)
    # driver.implicitly_wait(10)
    WebDriverWait(driver, 15)

    wait.until(EC.title_is("ТранспортТВ - Панель управления"))


def wait_time():

    WebDriverWait(driver, 10)

    return time.sleep(3)


def connect_db():
    conn = db.create_engine('postgresql_postGIS://sc_user:h2ullVAtpWapQssNYXI0@192.168.100.3:5432/zms_serv3?searchapath=route_info')

    return conn


def test_create_stops(driver):

    connect = connect_db()

    conn = db.create_engine('postgresql_postGIS://sc_user:h2ullVAtpWapQssNYXI0@192.168.100.3:5432/zms_serv3?searchapath=route_info')

    

    connect.execute(db.select([route_info.stops]))



    records = connect.fetchone()

    connect.execute('select ext_stop_id from route_info.stops')

    all_stops = connect.fetchall()

    best_list = []

    for moms in all_stops:
        best_list.append(all_stops.split(',),'))

    print(str(best_list))

    connect.close()


    # Тестовые данные для создания остановок

    # Названия остановок прямого и обратного рейса
    stops_name = ['ВДНХ (Южная)', '1-я Останкинская (ул. Академика Королева) Остановка наземно',
                  'Цандера (ул. Академика Королёва)', 'ВДНХ (Южная)', 'Цандера (ул. Академика Королёва)',
                  'Аргуновская']

    # Список координат широты
    stops_latitudes = [37.634885, 37.633789, 37.632607, 37.634747, 37.628352, 37.628352]

    # Список координат долготы
    stops_longitudes = [55.823553, 55.821562, 55.821853, 55.823437, 55.821854, 55.821481]

    # Код присвоения
    stops_counter_id = int(records[0])

    test_login(driver)

    wait_time()

    wait = WebDriverWait(driver, 30)

    wait.until(EC.element_to_be_clickable((By.TAG_NAME, "div[class='left-nav__menu-unit-header-title']")))
    # left_elements = driver.find_elements_by_tag_name("div[class='left-nav__menu-unit-header-title']")
    # print(len(left_elements))

    WebDriverWait(driver, 30)

    driver.find_elements_by_tag_name("div[class='left-nav__menu-unit-header-title']")[2].click()

    WebDriverWait(driver, 10)

    driver.find_elements_by_tag_name("div[class='collapsed none-collapsed'] div")[18].click()

    WebDriverWait(driver, 20)

    driver.find_element_by_tag_name("a[href='/route/routeInfo/stops']").click()

    wait_time()

# Реализация цикла по созданию остановки

    # вычисляем количество остановок stops = len(остановки прямого рейся) + len(остановки обратного рейса)

    stops = len(stops_name)

    for stop in range(stops):

        #driver.delete_all_cookies()
        WebDriverWait(driver, 30)

        # Нажать кнопку "Создать остановку"
        driver.find_element_by_tag_name("i[class='material-icons button-icon']").click()

        wait_time()

        driver.find_elements_by_tag_name("div[class='col col-5'] div[class='vue-select io']")[0].click()

        wait_time()

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "div[class='vue-select__options-box']"
                                                                " div[class='vue-select__options-holder']"
                                                                " div[class='vue-select__option']")))

        # Выбор "города
        # ПАТ - news
        #driver.find_elements_by_tag_name("div[class='vue-select__options-box'] div[class='vue-select__search']")[3].send_keys("Санкт-Петербург")
        #driver.find_elements_by_tag_name("div[class='vue-select__options-box'] div[class='vue-select__options-holder'] div[class='vue-select__option']")[9].click()

        # zms_serv1
        #driver.find_elements_by_tag_name("div[class='vue-select__options-box'] div[class='vue-select__options-holder'] "
        #                                "div[class='vue-select__option']")[48].click()

        driver.find_elements_by_tag_name("div[id='city'] div[id='5']")[0].click()

        wait_time()

        # Выбор агенства в БД news PAT
        #driver.find_elements_by_tag_name("div[class='vue-select__options-box'] div[class='vue-select__options-holder']"
        #                                " div[class='vue-select__option']")[10].click()

        # zms_serv1
        # driver.find_elements_by_tag_name("div[class='vue-select__options-box'] div[class='vue-select__options-holder'] "
        #                                  "div[class='vue-select__option']")[35].click()

        driver.find_elements_by_tag_name("div[class='col col-5'] div[class='vue-select io']")[0].click()

        wait_time()

        driver.find_elements_by_tag_name("div[id='agency'] div[id='1']")[0].click()

        wait_time()

        current_stops_id = stops_counter_id

        for i in range(stops):

            for j in range(1, len(all_stops)):

                if '2812' != all_stops[j - 1]:
                    if j == all_stops[len(all_stops) - 1]:
                        driver.find_element_by_tag_name("div[class='col col-2'] "
                                                        "input[class='io']").send_keys(str(current_stops_id + 1))
                else:
                    current_stops_id += 1

        wait_time()

        driver.find_elements_by_tag_name("div[class='col col-6'] "
                                         "input[class='io']")[0].send_keys(str(stops_longitudes[stop]))

        driver.find_elements_by_tag_name("div[class='col col-6'] "
                                         "input[class='io']")[0].send_keys(str(stops_latitudes[stop]))

        driver.find_elements_by_tag_name("div[class='col col-6'] "
                                         "input[class='io']")[0].send_keys(stops_name[stop])

        driver.find_elements_by_tag_name("div[class='col col-6'] "
                                         "input[class='io']")[0].send_keys(stops_name[stop])

        wait_time()

        driver.find_element_by_tag_name("div[class='margin-top'] button[class='btn btn-success']").click()

        wait_time()
