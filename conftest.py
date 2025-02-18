import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from page import Triangle_Page

@pytest.fixture(scope='session')
def driver():
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def triangle_page(driver):
    url = "https://playground.learnqa.ru/puzzle/triangle"
    page = Triangle_Page(driver, url)  
    page.open()  
    yield page