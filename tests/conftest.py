import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    browser.config.base_url = 'http://demoqa.com'
    browser.config.window_width = 768
    browser.config.window_height = 1360
    #browser.config.timeout = 5.0
    #driver_options.add_argument("--disable-notifications")
   
    yield

    browser.quit()
