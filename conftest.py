from selene.support.shared import browser
from dotenv import load_dotenv
import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config

from utils import attach
from utils.helper import BaseSession

API_URL = 'https://demowebshop.tricentis.com/'
WEB_URL = 'https://www.travian.com/ru'

browser.config.base_url = WEB_URL

DEFAULT_BROWSER_VERSION = "100.0"


@pytest.fixture(scope="session", autouse=True)
def browser_window_size():
    browser.config.window_width = 1024
    browser.config.window_height = 768



@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="session")
def travian_login_api():
    login = os.getenv("LOGIN_TRAVIAN")
    password = os.getenv("PASSWORD_TRAVIAN")
    with BaseSession(base_url="https://ts9.x1.europe.travian.com/api/v1/auth") as session:
        response = session.post(
            url='login',
            params={'Email': "QaUserAuto", 'Password': "12345678"},
            headers={'content-type': "application/x-www-form-urlencoded; charset=UTF-8"},
            allow_redirects=False
        )
        authorization_cookie = response.cookies.get('NOPCOMMERCE.AUTH')
        session.cookies.set('NOPCOMMERCE.AUTH', authorization_cookie)
        browser.open("")
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
        yield session

        attach.add_screenshot(browser)


@pytest.fixture(scope='function')
def travian_login_ui(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser = Browser(Config(driver))

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
