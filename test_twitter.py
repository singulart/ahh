import os
from appium import webdriver
from pages import TwHomePage
import pytest


TWITTER_ANDROID_CAPS = {
    'platformName': 'Android',
    'deviceName': 'Android',
    'appPackage': 'com.twitter.android',
    'appActivity': 'com.twitter.android.StartActivity',
    'automationName': 'UiAutomator2',
    'newCommandTimeout': 300,
}

class TestTwitter(object):

    # def test_login_and_logout(self: 'TestTwitter', make_driver: MakeDriver) -> None:
    #     d: webdriver.Remote = make_driver("twitter")
    #     splash_page = TwSplashPage(d)
    #     login_page = splash_page.nav_to_login()
    #     home_page = login_page.login(USERNAME, PASSWORD)
    #     home_page.allow_data_collection()
    #     home_page.skip_location_settings()
    #     home_page.logout()
    #     splash_page.verify()


    @pytest.fixture
    def browser(self):
        driver = webdriver.Remote(
                command_executor='http://localhost:4723/wd/hub',
                desired_capabilities= TWITTER_ANDROID_CAPS
        )
        yield driver
        driver.quit()

    def test_follow_and_unfollow(self: 'TestTwitter', browser) -> None:
        d = browser
        splash_page = TwHomePage(d)
        search_page = splash_page.nav_to_search()
        profile_page = search_page.search_for_user('jlipps')
        profile_page.follow()
        profile_page.unfollow()
        d.back()
        search_page.nav_to_home()
        # home_page.logout()
        splash_page.verify()
