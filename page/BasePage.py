
class BasePage:
    def __int__(self, driver):
        self.driver = driver

    def type(self, locator):
        self.driver.find_element_by_xpath(locator).sendkeys("hello")

