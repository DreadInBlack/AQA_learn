from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self, driver: object, url: object) -> object:
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
    def element_is_visible (self,  locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    def elemets_are_visble (self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    def elemet_is_present (self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    def elements_are_presents (self, locator, timeout = 5):
        return wait(self.driver,timeout).until(EC.visibility_of_all_elements_located(locator))
    def element_is_not_visible (self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
    def element_is_clickable(self,locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    def go_to_element(self, element):
        self.driver.executt_script('argumetn[0].scrollIntoView();', element)