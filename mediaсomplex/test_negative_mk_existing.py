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
    """Негативны тест по Созданию МК с существующим MCID в системе"""

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

    # Заполнить обязательные поля "МК ID"

    driver.find_element_by_tag_name("input[id='mcId']").send_keys("4004")

    # № материнской платы

    driver.find_element_by_tag_name("input[id='motherBoard']").send_keys("Autotest create already MK ID")

    # Транспортное агенство

    driver.find_elements_by_tag_name("a[class='chosen-single chosen-default']")[1].click()

    driver.find_elements_by_tag_name("div[class='chosen-drop'] li")[5].click()

    # Бортовой номер ТС

    wait_time()

    driver.find_element_by_tag_name("input[id='vehicleRegNumber']").send_keys("Autotest create already MK ID")

    # Монитор

    driver.find_element_by_tag_name("input[id='monitor']").send_keys("Autotest create already MK ID")

    # Город

    driver.find_elements_by_tag_name("a[class='chosen-single chosen-default']")[0].click()

    driver.find_elements_by_tag_name("div[class='chosen-drop'] li")[2].click()

    # Корпус

    driver.find_element_by_tag_name("input[id='cabinet']").send_keys("Autotest create already MK ID")

    # Имя хоста

    driver.find_element_by_tag_name("input[id='hostName']").send_keys("Autotest create already MK ID")

    # Разрешение

    driver.find_elements_by_tag_name("a[class='chosen-single chosen-default']")[0].click()

    driver.find_elements_by_tag_name("div[class='chosen-drop'] li")[1].click()

    # IP-адрес

    driver.find_element_by_tag_name("input[id='ip']").send_keys("Autotest create already MK ID")

    # Примечание

    driver.find_element_by_tag_name("input[id='comment']").send_keys("Autotest create already MK ID")

    # Нажать кнопку "Сохранить"

    driver.find_element_by_tag_name("div[class='cont-margin'] button[type='submit']").click()

    wait_time()

    exist_mc_id = driver.find_element_by_tag_name("span[id='id.errors']").get_property("innerText")

    if exist_mc_id in 'Такой МК ID уже существует':
        print('\nMK already exist!')
