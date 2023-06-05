import time

import selene
from selene.support.shared import browser
from selene import be, have


def test_login(browser_window_size):
    browser.open("https://ts9.x1.europe.travian.com/")
    browser.element(".account input").type('QaUserAuto')
    browser.element(".pass input").type('12345678')
    browser.element("[type='submit']").click()
    browser.element(".playerName").should(have.text("QaUserAuto"))

