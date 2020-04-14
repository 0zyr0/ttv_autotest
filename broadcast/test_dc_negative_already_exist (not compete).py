import pytest
import time

import sqlalchemy as db

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

    driver.get("http://192.168.0.102:8080/login")
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


def test_already_name_drum_create(driver):
    """Создание барабана вещания c уже существующим именем"""

    test_login(driver)
    time.sleep(5)
    wait = WebDriverWait(driver, 30)

    wait.until(EC.element_to_be_clickable((By.TAG_NAME, "div[class='left-nav__menu-unit-header-title']")))

    WebDriverWait(driver, 30)

    # Подключаемся к БД

    engine = db.create_engine('postgresql://sc_user:h2ullVAtpWapQssNYXI0@192.168.100.3/zms_task_6012', echo=True)

    connection = engine.connect()

    metadata = db.MetaData()

    revolvers = db.Table('revolvers', metadata, autoload=True, autoload_with=engine)

    # TODO Научить выбирать только по одному столбцу
    # https://docs.sqlalchemy.org/en/13/core/tutorial.html
    # https://stackoverflow.com/questions/37133774/how-can-i-select-only-one-column-using-sqlalchemy
    # https://docs.sqlalchemy.org/en/13/orm/query.html
    # https://docs.sqlalchemy.org/en/13/orm/loading_columns.html

    query = db.select([revolvers])

    ResultProxy = connection.execute(query)

    ResultSet = ResultProxy.fetchall()

    ResultSet[:3]

    # Эфир

    driver.find_elements_by_tag_name("div[class='left-nav__menu-unit-header-title']")[0].click()

    WebDriverWait(driver, 10)

    # Управление барабанами вещания

    driver.find_element_by_tag_name("a[href='/ether/broadcastRevolvers']").click()

    WebDriverWait(driver, 10)

    # Создать барабан

    driver.find_elements_by_tag_name("button[class='btn btn-primary']")[1].click()

    wait_time()

    # Город

    driver.find_elements_by_tag_name("div[class='col col-6'] [class='vue-select io']")[0].click()

    #wait_time()

    driver.find_elements_by_tag_name("div[class='vue-select__search'] input[tabindex='-1']")[0].send_keys("Москва")

    #wait_time()

    driver.find_elements_by_tag_name("div[class='vue-select__search'] input[tabindex='-1']")[0].send_keys(Keys.ENTER)

    #wait_time()

    driver.find_elements_by_tag_name("div[class='vue-select__option']")[0].click()

    #wait_time()


    # driver.find_elements_by_tag_name("div[class='col col-6'] [class='vue-select io']")[0].click()
    #
    # #wait_time()
    #
    # #driver.find_elements_by_tag_name("div[id='city'] div[id='4']")[1].click()
    #
    # driver.find_elements_by_tag_name("input[tabindex='-1']")[0].click()
    #
    # driver.find_elements_by_tag_name("div[id='city'][class='vue-select__options-holder'] div[id='4']")[1].click()
    #
    #
    #
    # # TODO Этот гад не хочет находиться. НЕ интерактивный видите ли
    #
    # wait.until(EC.presence_of_element_located((By.TAG_NAME, "div[class='vue-select__options-box']"
    #                                                         " div[class='vue-select__options-holder']"
    #                                                         " div[class='vue-select__option']")))
    #
    # driver.find_elements_by_tag_name("div[id='city'][class='vue-select__options-holder'] div[id='4']")[1].click()
    #
    # wait_time()

    # Название

    driver.find_elements_by_tag_name("div[class='row'] input[type='text']")[0].send_keys("Autotest Drum")

    # Описание

    driver.find_elements_by_tag_name("div[class='row'] input[type='text']")[1].send_keys("Autotest Drum")

    # График для рабочих дней

    driver.find_elements_by_tag_name("div[class='vue-select io']")[0].click()

    #wait_time()

    driver.find_elements_by_tag_name("div[class='vue-select__search'] input[tabindex='-1']")[4].send_keys("Moscow AutoGraph")

    #wait_time()

    driver.find_elements_by_tag_name("div[class='vue-select__search'] input[tabindex='-1']")[4].send_keys(Keys.ENTER)

    wait_time()

    driver.find_elements_by_tag_name("div[class='vue-select__option']")[8].click()

    #wait_time()

    # График для праздников

    driver.find_elements_by_tag_name("div[class='vue-select io']")[0].click()

    #wait_time()

    driver.find_elements_by_tag_name("div[class='vue-select__search'] input[tabindex='-1']")[5].send_keys("Moscow AutoGraph")

    #wait_time()

    driver.find_elements_by_tag_name("div[class='vue-select__search'] input[tabindex='-1']")[5].send_keys(Keys.ENTER)

    wait_time()

    driver.find_elements_by_tag_name("div[class='vue-select__option']")[8].click()

    #wait_time()

    # График для выходных дней

    driver.find_elements_by_tag_name("div[class='vue-select io']")[0].click()

    #wait_time()

    driver.find_elements_by_tag_name("div[class='vue-select__search'] input[tabindex='-1']")[6].send_keys("Moscow AutoGraph")

    #wait_time()

    driver.find_elements_by_tag_name("div[class='vue-select__search'] input[tabindex='-1']")[6].send_keys(Keys.ENTER)

    wait_time()

    driver.find_elements_by_tag_name("div[class='vue-select__option']")[8].click()

    wait_time()

    # Нажать кнопку "Сохранить"

    driver.find_element_by_tag_name("button[class='btn btn-success']").click()

    wait_time()

    # Проверка уведомления об успешно созданном Барабане

    notify_drum_created = driver.find_element_by_tag_name("span[data-notify='message']").get_property("innerText")

    valid_notify = "Барабан успешно создан"

    if notify_drum_created == valid_notify:
        print("\n Drum broadcast has created. Notify message is valid.")
