from pages.base_page import BasePage
import time

class AddPlayerPage(BasePage):
    expected_title = 'Add player'
    add_player_url = ('https://scouts-test.futbolkolektyw.pl/en/players/add')
    add_player_header_xpath = "//title[text()='Add player']"
    header_of_box = 'Add player'
    email_field_xpath = "//input[@name='email']"
    name_field_xpath = "//input[@name='name']"
    surname_field_xpath = "//input[@name='surname']"
    phone_field_xpath = "//input[@name='phone']"
    weight_field_xpath = "//input[@name='weight']"
    height_field_xpath = "//input[@name='height']"
    age_field_xpath = "//input[@name='age']"
    leg_field_xpath = "//div[@id='mui-component-select-leg']"
    right_leg_button_xpath = "//li[@data-value='right']"
    club_field_xpath = "//input[@name='club']"
    level_field_xpath = "//input[@name='level']"
    mainPosition_field_xpath = "//input[@name='mainPosition']"
    secondPosition_field_xpath = "//input[@name='secondPosition']"
    district_field_xpath = "//div[@id='mui-component-select-district']"
    achievements_field_xpath = "//input[@name='achievements']"
    addLanguage_button_xpath = "//span[contains(text(),'Add language')]"
    webLaczy_field_xpath = "//input[@name='webLaczy']"
    the_90minut_field_xpath = "//input[@name='web90']"
    facebook_field_xpath = "//label[contains(text(),'Facebook')]/following::div[1]"
    addLinkToYoutube_button_xpath = "//span[contains(text(),'Add link to Youtube')]"
    submit_button_xpath = "//span[contains(text(),'Submit')]"
    clear_button_xpath = "//span[contains(text(),'Clear')]"


    def check_title_of_header(self):
        self.assert_element_text(self.driver, self.add_player_header_xpath, self.header_of_box)

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.add_player_url) == self.expected_title

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_club(self, club):
        self.field_send_keys(self.club_field_xpath, club)

    def type_main_position(self, position):
        self.field_send_keys(self.mainPosition_field_xpath, position)

    def type_leg_field(self):
        self.click_on_the_element(self.leg_field_xpath)

    def type_right_leg(self):
        self.click_on_the_element(self.right_leg_button_xpath)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)




