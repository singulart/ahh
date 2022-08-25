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
        home_page = TwHomePage(d)
        search_page = home_page.nav_to_search()
        profile_page = search_page.search_for_user('jlipps')
        profile_page.follow()
        profile_page.unfollow()
        d.back()
        search_page.nav_to_home()
        # home_page.logout()
        home_page.verify()
