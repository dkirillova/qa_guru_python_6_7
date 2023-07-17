import time
import os
from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from .conftest import tmp_path

def test_download_zip():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": tmp_path,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    browser.config.driver = driver

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(5)

    assert os.path.exists(os.path.join(tmp_path, 'pytest-main.zip'))

    os.remove(os.path.join(tmp_path, 'pytest-main.zip'))