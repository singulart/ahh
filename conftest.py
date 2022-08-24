import pytest
import os
from appium import webdriver
from typing import Callable


MakeDriver = Callable[[str], webdriver.Remote]

TWITTER_ANDROID_CAPS = {
    'platformName': 'Android',
    'deviceName': 'Android',
    'appPackage': 'com.twitter.android',
    'appActivity': 'com.twitter.android.StartActivity',
    'automationName': 'UiAutomator2',
    'newCommandTimeout': 300,
}


@pytest.fixture
def make_driver() -> webdriver.Remote:
    driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities= TWITTER_ANDROID_CAPS
    )
    yield driver
    driver.quit()
