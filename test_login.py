import pytest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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

# очистка кэша переход в раздел настроек
# def get_clear_browsing_button(driver):
#     """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
#     return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')
#
#
# def clear_cache(driver, timeout=60):
#     """Clear the cookies and cache for the ChromeDriver instance."""
#     # navigate to the settings page
#     driver.get('chrome://settings/clearBrowserData')
#
#     # wait for the button to appear
#     wait = WebDriverWait(driver, timeout)
#     wait.until(get_clear_browsing_button)
#
#     # click the button to clear the cache
#     get_clear_browsing_button(driver).click()
#
#     # wait for the button to be gone before returning
#     wait.until_not(get_clear_browsing_button)


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


def broadcast_link_click(driver):
    wait = WebDriverWait(driver, 30)

    broadcast_revolver = driver.find_element_by_tag_name("a[href='/ether/broadcastRevolvers']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "span[class='breadcrumbs__item_active']")))

    broadcast_shedule = driver.find_element_by_tag_name("a[href='/ether/broadcastSchedule']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "span[class='breadcrumbs__item_active']")))

    broadcast_monitoring = driver.find_element_by_tag_name("a[href='/ether/broadcastMonitoring']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "span[class='breadcrumbs__item_active']")))

    broadcast_stats = driver.find_element_by_tag_name("a[href='/ether/broadcastStats']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "span[class='breadcrumbs__item_active']")))

    broadcast_holiday = driver.find_element_by_tag_name("a[href='/ether/broadcastHoliday']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "span[class='breadcrumbs__item_active']")))


def content_link_click(driver):
    wait = WebDriverWait(driver, 30)

    rubrics = driver.find_element_by_tag_name("div[class='collapsed none-collapsed'] div[class='left-nav__menu-child-unit'] div[class='left-nav__icon-holder arrow']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))

    time.sleep(5) #КОСТЫЛИ

    news = driver.find_element_by_tag_name("a[href='/content/rubrics/news']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))

    time.sleep(5) #КОСТЫЛИ

    weather = driver.find_element_by_tag_name("a[href='/weather/']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    time.sleep(5) #КОСТЫЛИ

    transport_tv = driver.find_element_by_tag_name("a[href='/content/rubrics/transportTv']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='is-playing-showing-plan-trigger__trigger']")))

    time.sleep(5) #КОСТЫЛИ

    countdown = driver.find_element_by_tag_name("a[href='/heading/view/20/tab/1']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    birthdays = driver.find_element_by_tag_name("a[href='/heading/view/20/tab/1']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    time.sleep(3) #КОСТЫЛИ

    learn_moscow = driver.find_element_by_tag_name("a[href='/rubric/section/38?tab=1']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    time.sleep(5) #КОСТЫЛИ

    stops_info = driver.find_element_by_tag_name("a[href='/rubric/section/42?tab=1']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    time.sleep(5) #КОСТЫЛИ

    transort_scheme = driver.find_element_by_tag_name("a[href='/rubric/section/43?tab=1']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    time.sleep(5) #КОСТЫЛИ

    calendar = driver.find_element_by_tag_name("a[href='/content/rubrics/calendar']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))

    time.sleep(5) #КОСТЫЛИ

    # nebo_digital = driver.find_element_by_tag_name("a[href='/heading/view/22/tab/1']").click()
    # wait.until(EC.presence_of_element_located((By.TAG_NAME, "span[class='breadcrumbs__item_active']")))

    afisha = driver.find_element_by_tag_name("a[href='/content/rubrics/afisha']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "span[class='breadcrumbs__item_active']")))

    time.sleep(5) #КОСТЫЛИ

    info_mchs = driver.find_element_by_tag_name("a[href='/content/rubrics/mchs']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))

    time.sleep(5) #КОСТЫЛИ

    videostream = driver.find_element_by_tag_name("a[href='/heading/view/24/tab/1']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    time.sleep(5) #КОСТЫЛИ

    pool = driver.find_element_by_tag_name("a[href='/content/rubrics/poll']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))

    time.sleep(5) #КОСТЫЛИ

    quiz = driver.find_element_by_tag_name("a[href='/content/rubrics/quiz']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))

    time.sleep(5) #КОСТЫЛИ

    you_know_what = driver.find_element_by_tag_name("a[href='/heading/view/2/tab/1']").click()
    WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    time.sleep(5) #КОСТЫЛИ

    photoquote = driver.find_element_by_tag_name("a[href='/heading/view/3/tab/1']").click()
    #wait.until(EC.presence_of_element_located((By.TAG_NAME, "span[class='breadcrumbs__item_active']")))

    time.sleep(5) #КОСТЫЛИ

    qa = driver.find_element_by_tag_name("a[href='/heading/view/4/tab/1']").click()
    #wait.until(EC.presence_of_element_located((By.TAG_NAME, "span[class='breadcrumbs__item_active']")))

    time.sleep(5) #КОСТЫЛИ

    advice = driver.find_element_by_tag_name("a[href='/heading/view/5/tab/1']").click()
    #wait.until(EC.presence_of_element_located((By.TAG_NAME, "span[class='breadcrumbs__item_active']")))

    time.sleep(5) #КОСТЫЛИ

    interest_video = driver.find_element_by_tag_name("a[href='/heading/view/6/tab/1']").click()
    #wait.until(EC.presence_of_element_located((By.TAG_NAME, "span[class='breadcrumbs__item_active']")))

    time.sleep(5) #КОСТЫЛИ

    congratulation = driver.find_element_by_tag_name("a[href='/heading/view/7/tab/1']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    time.sleep(5) #КОСТЫЛИ

    night_route = driver.find_element_by_tag_name("a[href='/heading/view/1/tab/1']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    time.sleep(5) #КОСТЫЛИ

    instagram = driver.find_element_by_tag_name("a[href='/instagram/']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    time.sleep(5) #КОСТЫЛИ

    active_citizen = driver.find_element_by_tag_name("a[href='/heading/view/12/tab/1']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    time.sleep(5) #КОСТЫЛИ

    ngpt = driver.find_element_by_tag_name("a[href='/heading/view/14/tab/1']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    time.sleep(5) #КОСТЫЛИ

    crypt_currency = driver.find_element_by_tag_name("a[href='/content/rubrics/cryptoCurrency']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))

    time.sleep(5) #КОСТЫЛИ

    #Футбольные рубрики

    # football = driver.find_element_by_tag_name("div[class='left-nav__menu-child-unit2'] div").click()
    # #wait.until(EC.presence_of_element_located((By.TAG_NAME, "span[class='breadcrumbs__item_active']")))
    #
    # match_annonce = driver.find_element_by_tag_name("a[href='/content/rubrics/football/matchAnnouncement']").click()
    # wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))
    #
    # match_online = driver.find_element_by_tag_name("a[href='/content/rubrics/football/matchOnline']").click()
    # wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))
    #
    # match_result = driver.find_element_by_tag_name("a[href='/content/rubrics/football/matchResult']").click()
    # wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))
    #
    # table_group_st = driver.find_element_by_tag_name("a[href='/content/rubrics/football/tournamentGroupStage']").click()
    # wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))
    #
    # calendar_tour = driver.find_element_by_tag_name("a[href='/content/rubrics/football/tournamentCalendar']").click()
    # wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))
    #
    # tour_edit = driver.find_element_by_tag_name("a[href='/content/rubrics/football/tournamentEditor']").click()
    # wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))

    #------

    content_from_cust = driver.find_element_by_tag_name("a[href='/content/rubrics/contentFromCustomer']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))

    time.sleep(5) #КОСТЫЛИ

    sights = driver.find_element_by_tag_name("a[href='/rubric/section/15?tab=1']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    time.sleep(5) #КОСТЫЛИ

    service_info = driver.find_element_by_tag_name("a[href='/content/rubrics/serviceInfo']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))

    time.sleep(5) #КОСТЫЛИ

    emmergency = driver.find_element_by_tag_name("a[href='/emergency/emergency_message']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    time.sleep(5) #КОСТЫЛИ

    #Опповещения о маршруте

    aero_rec = driver.find_element_by_tag_name("a[href='/heading/view/8/tab/1']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    time.sleep(5) #КОСТЫЛИ

    rubrics_set = driver.find_element_by_tag_name("a[href='/content/rubricsSettings']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))

    time.sleep(5) #КОСТЫЛИ

    stat_view = driver.find_element_by_tag_name("a[href='/stat/content/view']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    time.sleep(5) #КОСТЫЛИ
    # Долго открывается, закоментил на момент написания
    # monitoring_actual = driver.find_element_by_tag_name("a[href='/monitoring/actualdata?filter=all']").click()
    # wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))


def route_link_click(driver):
    wait = WebDriverWait(driver, 30)

    leaving_route_list = driver.find_element_by_tag_name("div a[href='/mcOutOfRoute/list']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    run_status_mk = driver.find_element_by_tag_name("div a[href='/vehicleDetails/list']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    integration_status = driver.find_element_by_tag_name("div a[href='/integrationStatus/list']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    iskra_update = driver.find_element_by_tag_name("div a[href='/transportPark/info']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    route_info = driver.find_element_by_tag_name("div a[href='javascript:void(0)'][class='item-expand item-expand--opened']").click()
    #wait.until(EC.presence_of_element_located((By.TAG_NAME, "span[class='breadcrumbs__item_active']")))

    agencies = driver.find_element_by_tag_name("div a[href='/route/routeInfo/agencies']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))

    stops = driver.find_element_by_tag_name("div a[href='/route/routeInfo/stops']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))

    translit_dict = driver.find_element_by_tag_name("div a[href='/route/routeInfo/dictionaryTranslit']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))

    sound_info = driver.find_element_by_tag_name("div a[href='/route/routeInfo/soundInformation']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))

    routes = driver.find_element_by_tag_name("div a[href='/route/routeInfo/routes']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))

    sync_asu_gpt = driver.find_element_by_tag_name("div a[href='/routesInfo/sync/list']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))


def mediacomplex_link_click(driver):
    wait = WebDriverWait(driver, 15)

    control_mk = driver.find_element_by_tag_name("div a[href='/mc/?page_size=25']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    monitoring_mk = driver.find_element_by_tag_name("div a[href='/monitoring/']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header clearfix']")))


def info_link_click(driver):
    wait = WebDriverWait(driver, 30)

    resolution_dict = driver.find_element_by_tag_name("div a[href='/screen/resolutions/list']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    guard_timer = driver.find_element_by_tag_name("div a[href='/mc/guardtimer']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    events = driver.find_element_by_tag_name("div a[href='/events/']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div ol[class='breadcrumb']")))

    licenses = driver.find_element_by_tag_name("div a[href='/information/licenses']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))


def mobile_link_click(driver):
    wait = WebDriverWait(driver, 30)

    user_control = driver.find_element_by_tag_name("div a[href='/mobile/userManagement']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))


def advertise_link_click(driver):
    wait = WebDriverWait(driver, 30)

    campaign = driver.find_element_by_tag_name("div a[href='/advertising/campaigns']").click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "div [class='page__header breadcrumbs']")))


def test_smoke_links(driver):
    test_login(driver)
    time.sleep(5)
    wait = WebDriverWait(driver, 30)

    wait.until(EC.element_to_be_clickable((By.TAG_NAME, "div[class='left-nav__menu-unit-header-title']")))
    left_elements = driver.find_elements_by_tag_name("div[class='left-nav__menu-unit-header-title']")
    print(len(left_elements))

    WebDriverWait(driver, 30)

    links_list = []

    for i, element in enumerate(left_elements):

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "a[href='/advertising/campaigns']")))
        links_counter = driver.find_elements_by_tag_name("div[class='left-nav__menu-unit-header-title']")[i].click()

        links_list.append(element)

        if element == links_list[0]:
            broadcast_link_click(driver)
        elif element == links_list[1]:
            content_link_click(driver)
        elif element == links_list[2]:
            route_link_click(driver)
        elif element == links_list[3]:
            mediacomplex_link_click(driver)
        elif element == links_list[4]:
            info_link_click(driver)
        elif element == links_list[5]:
            mobile_link_click(driver)
        elif element == links_list[6]:
            advertise_link_click(driver)
