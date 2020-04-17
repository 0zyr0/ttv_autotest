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


def test_news_rss(driver):
    """Создание источника новостей"""

    test_login(driver)
    time.sleep(5)
    wait = WebDriverWait(driver, 30)

    wait.until(EC.element_to_be_clickable((By.TAG_NAME, "div[class='left-nav__menu-unit-header-title']")))

    WebDriverWait(driver, 30)

    # Контент

    driver.find_elements_by_tag_name("div[class='left-nav__menu-unit-header-title']")[1].click()

    WebDriverWait(driver, 10)

    # Рубрики

    driver.find_elements_by_tag_name("div[class='left-nav__menu-child-unit'] img")[0].click()

    WebDriverWait(driver, 10)

    # Новости

    driver.find_element_by_tag_name("a[href='/content/rubrics/news']").click()

    WebDriverWait(driver, 10)

    # Вкладка "Источники новостей"

    driver.find_elements_by_tag_name("div[class='tab-nav__tab']")[1].click()

    WebDriverWait(driver, 10)

    # Добавить источник

    driver.find_elements_by_tag_name("button[class='btn btn-primary margin-bottom']")[2].click()

    # Заполнить поля "Источник новостей" и "Город"

    driver.find_element_by_tag_name("input[class='io tip']").send_keys("http://habrahabr.ru/rss/best/")

    WebDriverWait(driver, 10)

    driver.find_elements_by_tag_name("div[tabIndex='-1']")[0].click()

    wait_time()

    driver.find_elements_by_tag_name("input[tabIndex='-1']")[0].send_keys("Москва")

    wait_time()

    driver.find_elements_by_tag_name("input[tabIndex='-1']")[0].send_keys(Keys.ENTER)

    wait_time()

    driver.find_elements_by_tag_name("div[id='city'] div[id='4']")[0].click()

    # Нажать кнопку "Сохранить"

    driver.find_element_by_tag_name("button[class='btn btn-success']").click()

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "span[data-notify='message']")))

    notify_import_news = driver.find_elements_by_tag_name("span[data-notify='message']")[0].get_property("innerText")

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "span[data-notify='message']")))

    wait_time()

    print('Test Done')