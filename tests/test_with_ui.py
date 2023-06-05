import time

import selene
from selene.support.shared import browser
from selene import be, have, command


def test_login(browser_window_size):
    browser.open("https://ts9.x1.europe.travian.com/")
    browser.element(".account input").type('QaUserAuto')
    browser.element(".pass input").type('12345678')
    browser.element("[type='submit']").click()
    browser.element(".playerName").should(have.text("QaUserAuto"))


def test_soon_available_buildings(browser_window_size):
    # browser.open("https://ts9.x1.europe.travian.com/")
    browser.element(".buildingView ").click()
    browser.element('[onclick="window.location.href=\'/build.php?id=37\'"]').click()
    browser.element('h1').should(have.text('Construct new building'))
    browser.element('h4').should(have.text('Soon available buildings'))
    browser.element('#build_list_soon').all("h2").should(have.exact_texts(['Marketplace', 'Residence', 'Palace', "Stonemason's Lodge", 'Treasury', 'Town Hall', 'Trade Office', 'Great Granary', 'Great Warehouse']))


def test_server_statistics_start_date(browser_window_size):
    # browser.open("https://ts9.x1.europe.travian.com/")
    browser.element(".statistics").click()
    browser.element("[href='/statistics/general']").click()
    browser.element("[class='step start achieved'] [class='description']").should(have.text("24.04.23"))


def test_server_statistics_culture_diagram_color(browser_window_size):
    # browser.open("https://ts9.x1.europe.travian.com/")
    browser.element(".statistics").click()
    browser.element("[href='/statistics/general']").click()
    browser.element(".culturePointsRankChart [name='0']").should(have.attribute("fill", "#608cbc"))
    browser.element(".culturePointsRankChart [name='1']").should(have.attribute("fill", "#ea866e"))


def test_buy_gold_for_gold_club(browser_window_size):
    browser.element(".shop").click()
    browser.element("[class*='bestPackage'] .price").should(be.visible)
    browser.element('.scrollingContainer').all(".content")[3].click()
    browser.element(".goldclub .featureTitle").should(have.text("Gold club"))
    browser.element("h4").should(have.text("Gold club"))
    # Кнопка отрисовывается дольше, чем элемент появлется и нажимается тестом
    time.sleep(1)
    browser.element("[class*='prosButton goldclub']").click()
    browser.element(".infoText").should(have.text("You do not have enough gold to use this feature!"))
    browser.element(".price").should(have.text("€3.99"))
