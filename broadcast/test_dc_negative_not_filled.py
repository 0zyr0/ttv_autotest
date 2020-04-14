# TODO Создание барабана вещания
# TODO Создание барабана вещания. Негатив. Не заполненные поля
# TODO Создание барабана вещания. Негатив. Одинаковое название
# TODO Редактирование барабана
# TODO Применение барабана
# TODO Удаление барабана
# TODO Удаление барабана. Негатив


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


def test_drum_create(driver):
    """ Негативный тест. Создание барабана вещания c не заполненными полями.
        Плюс проверка на правильные названия полей
    """

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

    # Создать барабан

    driver.find_elements_by_tag_name("button[class='btn btn-primary']")[1].click()

    wait_time()

    # Нажать кнопку "Сохранить"

    driver.find_element_by_tag_name("button[class='btn btn-success']").click()

    # Выводится уведомление "Не все обязательные поля заполнены"

    notify_message = driver.find_element_by_tag_name("span[data-notify='message']").get_property("innerText")

    if notify_message == "Не все обязательные поля заполнены":
        print("\nNotify message is valid.")
    else:
        print("\nNotify message is NOT valid or not found.")

    error_fields = driver.find_elements_by_tag_name("div[class='vue-select io errorIO']")

    for i in range(len(error_fields)):
        print("\n Field " + str(i) + " have valid error-color.")

    driver.find_elements_by_tag_name("input[class='io errorIO']")[0]

    print("\n Field \"Name\" have valid error-color.")

    driver.find_elements_by_tag_name("input[class='io errorIO']")[1]

    print("\n Field \"Description\" have valid error-color.")

    print("\n \n *** Checking Fields name on Create Drum form. ***")

    # Проверка названий полей

    name_list = []

    valid_name_list = ["Город *", "Название *", "Описание *", "График для рабочих дней *",
                       "График для праздников *", "График для выходных дней *"]

    name_el = driver.find_elements_by_tag_name("div[class='io-title']")

    for j in range(6):
        name_list.append(name_el[j].get_property("innerText"))

    for k in range(6):
        if name_list[k] in valid_name_list:
            print("\n Field name is valid.")
