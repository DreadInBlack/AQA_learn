from Locators.elements_page_locators import TextBoxPageLocators
from Pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('Test Testovich')
        self.element_is_visible(self.locators.EMAIL).send_keys('psp@mail.ru')
        self.element_is_visible(self.locators.CURRENT_ADDRRESS).send_keys('test12345')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('test67890')
        self.element_is_visible(self.locators.SUBMIT).click()

    def check_filled_from(self):
        full_name = self.elemet_is_present(self.locators.CREATED_FULL_NAME).text
        email = self.elemet_is_present(self.locators.CREATED_EMAIL).text
        current_address = self.elemet_is_present(self.locators.CREATED_CURRENT_ADDRESS).text
        permanent_address = self.elemet_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text
        return full_name, email, current_address, permanent_address
