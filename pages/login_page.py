from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//span[contains(text(),'Sign in')]"
    login_url = ('https://scouts.futbolkolektyw.pl/en/')
    expected_title = ('Scouts panel - sign in')
    title_of_box_xpath = "//*[text()='Scouts Panel']"
    header_of_box = 'Scouts Panel'
    message_invalid_data = "Identifier or password invalid."
    message_invalid_data_xpath = "//span[text()='Identifier or password invalid.']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)
    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def check_title_of_header(self):
        self.assert_element_text(self.driver, self.title_of_box_xpath, self.header_of_box)

    def check_message_invalid_data(self):
        self.assert_element_text(self.driver, self.message_invalid_data_xpath, self.message_invalid_data)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

