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

    driver.get("http://192.168.100.42:8080/login")
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


def test_create_day_graph(driver):
    """Создание суточного графика"""

    test_login(driver)

    wait_time()

    wait = WebDriverWait(driver, 30)

    wait.until(EC.element_to_be_clickable((By.TAG_NAME, "div[class='left-nav__menu-unit-header-title']")))
    # left_elements = driver.find_elements_by_tag_name("div[class='left-nav__menu-unit-header-title']")
    # print(len(left_elements))

    WebDriverWait(driver, 30)

    # Эфир

    driver.find_elements_by_tag_name("div[class='left-nav__menu-unit-header-title']")[0].click()

    WebDriverWait(driver, 10)

    # Суточные графики

    driver.find_element_by_tag_name("a[href='/ether/broadcastSchedule']").click()

    wait_time()

    # Создать суточный график

    driver.find_element_by_tag_name("button[class='btn btn-primary margin-bottom']").click()

    wait_time()

    # Заполнить обязательные поля "Название" и "Описание"

    driver.find_elements_by_tag_name("div[class='col col-6'] input")[0].send_keys('Moscow AutoGraph')

    driver.find_elements_by_tag_name("div[class='col col-6'] input")[1].send_keys('Moscow AutoGraph')

    #  Нажать кнопку "Добавить окно вещания"

    driver.find_elements_by_tag_name("div[class='col col-6'] input")[0]

    wait_time()

    driver.find_elements_by_tag_name("button[class='btn btn-primary margin-bottom']")[0].click()

    #  Нажать кнопку "Добавить рубрику"
    wait_time()

    driver.find_elements_by_tag_name("button[class='btn btn-primary']")[0].click()

# TODO Отметить чек-боксами рубрики "Новости", "Точное время", "Погода", "КОЗ", "ТТВ", "Реклама"

    wait_time()

    # Можно сделать цикл, но потом зарефакторим

    driver.find_elements_by_tag_name("div[class='col col-12'] li label[class='checkbox checkbox-wrapper']")[21].click()

    driver.find_elements_by_tag_name("div[class='col col-12'] li label[class='checkbox checkbox-wrapper']")[26].click()

    driver.find_elements_by_tag_name("div[class='col col-12'] li label[class='checkbox checkbox-wrapper']")[32].click()

    driver.find_elements_by_tag_name("div[class='col col-12'] li label[class='checkbox checkbox-wrapper']")[37].click()

    driver.find_elements_by_tag_name("div[class='col col-12'] li label[class='checkbox checkbox-wrapper']")[41].click()

    driver.find_elements_by_tag_name("div[class='col col-12'] li label[class='checkbox checkbox-wrapper']")[42].click()

# TODO Нажать кнопку Сохранить

    wait_time()

    driver.find_elements_by_tag_name("button[class='btn btn-success']")[0].click()

# TODO заполнить проценты и нажать сохранить

    wait_time()

    driver.find_elements_by_tag_name("div[class='window__rubric'] input[type='number']")[0].send_keys(Keys.CONTROL, 'a')

    driver.find_elements_by_tag_name("div[class='window__rubric'] input[type='number']")[0].send_keys('17')

    driver.find_elements_by_tag_name("div[class='window__rubric'] input[type='number']")[1].send_keys(Keys.CONTROL, 'a')

    driver.find_elements_by_tag_name("div[class='window__rubric'] input[type='number']")[1].send_keys('17')

    driver.find_elements_by_tag_name("div[class='window__rubric'] input[type='number']")[2].send_keys(Keys.CONTROL, 'a')

    driver.find_elements_by_tag_name("div[class='window__rubric'] input[type='number']")[2].send_keys('17')

    driver.find_elements_by_tag_name("div[class='window__rubric'] input[type='number']")[3].send_keys(Keys.CONTROL, 'a')

    driver.find_elements_by_tag_name("div[class='window__rubric'] input[type='number']")[3].send_keys('17')

    driver.find_elements_by_tag_name("div[class='window__rubric'] input[type='number']")[4].send_keys(Keys.CONTROL, 'a')

    driver.find_elements_by_tag_name("div[class='window__rubric'] input[type='number']")[4].send_keys('17')

    driver.find_elements_by_tag_name("div[class='window__rubric'] input[type='number']")[5].send_keys(Keys.CONTROL, 'a')

    driver.find_elements_by_tag_name("div[class='window__rubric'] input[type='number']")[5].send_keys('15')

    driver.find_elements_by_tag_name("button[class='btn btn-success']")[1].click()

    assert ''

    wait_time()