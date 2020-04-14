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

    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    # Переход на страницу виртуалки
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 30)

    driver.get("http://192.168.0.102:8080/login")
    driver.implicitly_wait(10)

    # wait.until(EC.presence_of_element_located((By.TAG_NAME, "div[class='cs-app__footer flex-simple']")))

    # Поиск полей Логин, Пароль, нажатие кнопки
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "button[class='btn btn-primary margin-top enter']")))
    driver.find_element_by_tag_name("input#user").send_keys("admin")
    # driver.implicitly_wait(10)

    driver.find_element_by_tag_name("input#password").send_keys("admindjrheuflvbyf") #админвокругадмина

    #driver.find_element_by_tag_name("input#password").send_keys("admindflvbyt") #админвадмине

    #driver.find_element_by_tag_name("input#password").send_keys("xnpR95BChK") # ПАТ пароль: xnpR95BChK

    # driver.implicitly_wait(10)
    driver.find_element_by_tag_name("button[class='btn btn-primary margin-top enter']").send_keys(Keys.ENTER)
    # driver.implicitly_wait(10)
    WebDriverWait(driver, 15)

    wait.until(EC.title_is("ТранспортТВ - Панель управления"))


def wait_time():

    WebDriverWait(driver, 10)

    return time.sleep(3)


def test_negative_create_already_exist_mk(driver):
    """Негативны тест по Созданию МК с незаполненными обязательными полями"""

    test_login(driver)

    wait_time()

    wait = WebDriverWait(driver, 30)

    wait.until(EC.element_to_be_clickable((By.TAG_NAME, "div[class='left-nav__menu-unit-header-title']")))
    # left_elements = driver.find_elements_by_tag_name("div[class='left-nav__menu-unit-header-title']")
    # print(len(left_elements))

    WebDriverWait(driver, 30)

    # Медиакомплекс

    driver.find_elements_by_tag_name("div[class='left-nav__menu-unit-header-title']")[3].click()

    WebDriverWait(driver, 10)

    # Управление МК

    driver.find_element_by_tag_name("a[href='/mc/?page_size=25']").click()

    wait_time()

    # Создать новый МК

    driver.find_element_by_tag_name("a[href='./add/']").click()

    wait_time()

    # Нажать кнопку "Сохранить"

    driver.find_element_by_tag_name("div[class='cont-margin'] button[type='submit']").click()

    wait_time()

    warning_validation_list = []

    elements_fields = driver.find_elements_by_tag_name("div[class='warn_danger']")

    for element_field in range(len(elements_fields)):

        warning_validation_list.append(elements_fields[element_field].text)

    wait_time()

    # TODO Реализовать проверку названия поле обязательное.

    for i in range(warning_validation_list):
        if warning_validation_list[i].strip() in 'Обязательное поле':
            print('Field ' + str(i) +'validation correct')

    # if exist_mc_id in 'Такой МК ID уже существует':
    #     print('MK already exist!')
