from pages.base_page import BasePage


class Dashboard(BasePage):
    button_xpath = "//*[@id='login']"

    the_email_field_xpath = "//input[@name='email']"
    the_name_field_xpath = "//input[@name='name']"
    the_surname_field_xpath = "//input[@name='surname']"
    the_phone_field_xpath = "//input[@name='phone']"
    the_weight_field_xpath = "//input[@name='weight']"
    the_height_field_xpath = "//input[@name='height']"
    the_age_field_xpath = "//input[@name='age']"
    the_leg_field_xpath = "//div[@id='mui-component-select-leg']"
    the_club_field_xpath = "//input[@name='club']"
    the_level_field_xpath = "//input[@name='level']"
    the_mainPosition_field_xpath = "//input[@name='mainPosition']"
    the_secondPosition_field_xpath = "//input[@name='secondPosition']"
    the_district_field_xpath = "//div[@id='mui-component-select-district']"
    the_achievements_field_xpath = "//input[@name='achievements']"
    the_addLanguage_button_xpath = "//span[contains(text(),'Add language')]"
    the_webLaczy_field_xpath = "//input[@name='webLaczy']"
    the_90minut_field_xpath = "//input[@name='web90']"
    the_facebook_field_xpath = "//label[contains(text(),'Facebook')]/following::div[1]"
    the_addLinkToYoutube_button_xpath = "//span[contains(text(),'Add link to Youtube')]"
    the_submit_button_xpath = "//span[contains(text(),'Submit')]"
    the_clear_button_xpath = "//span[contains(text(),'Clear')]"
