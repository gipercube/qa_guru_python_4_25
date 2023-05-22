import time

import selene
from selene.support.shared import browser
from selene import be, have, command


def test_change_skin_color(browser_window_size):
    browser.open("https://ts9.x1.europe.travian.com/")

    # принять куки
    #browser.element("#cmpbntyestxt").click()
    # login
    #browser.element("a[href='#login']").click()

    #выбрать сервер Европы
    #browser.element(".codexVictoria").click()

    #auth
    browser.element(".account input").type('QaUserAuto')
    browser.element(".pass input").type('12345678')
    browser.element("[type='submit']").click()
    time.sleep(3)

