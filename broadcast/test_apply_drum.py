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

    driver.get("http://192.168.0.106:8080/login")
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


def test_drum_create(driver):
    """Применение барабана вещания"""

    test_login(driver)
    time.sleep(5)
    wait = WebDriverWait(driver, 30)

    wait.until(EC.element_to_be_clickable((By.TAG_NAME, "div[class='left-nav__menu-unit-header-title']")))

    WebDriverWait(driver, 30)

    # Эфир

    driver.find_elements_by_tag_name("div[class='left-nav__menu-unit-header-title']")[0].click()

    WebDriverWait(driver, 10)

    # Управление барабанами вещания

    driver.find_element_by_tag_name("a[href='/ether/broadcastRevolvers']").click()

    WebDriverWait(driver, 10)

    # Выбрать город

    driver.find_elements_by_tag_name("div[class='vue-select__selected']")[0].click()

    wait_time()

    driver.find_elements_by_tag_name("input[tabindex='-1']")[2].send_keys("Москва")

    wait_time()

    driver.find_elements_by_tag_name("input[tabindex='-1']")[2].send_keys(Keys.ENTER)

    wait_time()

    driver.find_elements_by_tag_name("div[class='vue-select__option']")[4].click()

    # Выбрать барабан

    driver.find_elements_by_tag_name("div[class='vue-select__selected']")[0].click()

    wait_time()

    driver.find_elements_by_tag_name("input[tabindex='-1']")[2].send_keys("Autotest Drum")

    wait_time()

    driver.find_elements_by_tag_name("input[tabindex='-1']")[2].send_keys(Keys.ENTER)

    wait_time()

    driver.find_elements_by_tag_name("div[class='vue-select__option']")[7].click()

    # Нажать кнопку "Применить барабан"

    driver.find_elements_by_tag_name("button[class='btn btn-primary']")[0].click()
