import time
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Triangle_Page:
    
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.locator_side_a = (By.CSS_SELECTOR, ".js_a")
        self.locator_side_b = (By.CSS_SELECTOR, ".js_b")
        self.locator_side_c = (By.CSS_SELECTOR, ".js_c")
        self.button_submit = (By.CSS_SELECTOR, ".btn-submit")
        self.bug_logg = (By.CSS_SELECTOR, ".bug_details .untraveled")
        self.case_logg = (By.CSS_SELECTOR, ".case_details .untraveled")
        

    def open(self):
        if self.driver.current_url != self.url:
            self.driver.get(self.url)

    def enter_side(self, locator, value):
        side = self.element_is_visible(locator, timeout=5)
        side.clear()
        side.send_keys(value)
    
    def enter_sides(self, side_a, side_b, side_c):
        self.enter_side(self.locator_side_a, side_a)
        self.enter_side(self.locator_side_b, side_b)
        self.enter_side(self.locator_side_c, side_c)
        self.element_is_clickable(self.button_submit).click()
        time.sleep(2)
        # info = self.element_is_visible(self.info, timeout=5).text
        # print(info)
        # assert "Это прямоугольный треугольник." == info

    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
    
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
    
    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)