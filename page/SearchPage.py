from page.BasePage import BasePage


class SearchPage(BasePage):

    def __int__(self, driver):
        super().__init__(driver)

    def search_in_google(self):
        BasePage.type(locator="//input[@name='q']")
