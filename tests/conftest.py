import pytest
from selene import browser


@pytest.fixture
def url():
    return 'https://reqres.in/api'


@pytest.fixture(scope="function")
def browser_setup():
    browser.config.base_url = 'https://demowebshop.tricentis.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()