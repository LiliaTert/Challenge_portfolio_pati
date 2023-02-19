import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_a_player_page import AddPlayerPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        #self.driver_service = Service(executable_path=ChromeDriverManager().install())
        #self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.user_login = LoginPage(self.driver)
        self.dashboard_page = Dashboard(self.driver)
        self.add_a_player_page = AddPlayerPage(self.driver)
    #
    # def test_login_to_the_system(self):
    #     user_login = LoginPage(self.driver)
    #     user_login.title_of_page()
    #     user_login.type_in_email('user10@getnada.com')
    #     user_login.type_in_password('Test-1234')
    #     #user_login.wait_for_button_will_be_clickable()
    #     user_login.click_on_the_sign_in_button()
    #     dashboard_page = Dashboard(self.driver)
    #     dashboard_page.title_of_page()
    #     dashboard_page.click_on_the_add_player_link()
    #     #time.sleep(5)
    #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(('xpath', "//span[text()='Add player']")))

    def test_login_to_the_system_using_valid_data(self):
        self.user_login.title_of_page()
        self.user_login.type_in_email('user10@getnada.com')
        self.user_login.type_in_password('Test-1234')
        self.user_login.click_on_the_sign_in_button()
        self.dashboard_page.title_of_page()
        time.sleep(3)

    def test_login_to_the_system_using_invalid_data(self):
        self.user_login.title_of_page()
        self.user_login.type_in_email('user10@getnada')
        self.user_login.type_in_password('Test-1234')
        self.user_login.click_on_the_sign_in_button()
        self.user_login.title_of_page()
        time.sleep(3)

    def test_log_out(self):
        self.user_login.type_in_email('user10@getnada.com')
        self.user_login.type_in_password('Test-1234')
        self.user_login.click_on_the_sign_in_button()
        self.dashboard_page.click_on_the_sign_out_link()
        time.sleep(3)

    def test_add_player(self):
        self.user_login.type_in_email('user10@getnada.com')
        self.user_login.type_in_password('Test-1234')
        self.user_login.click_on_the_sign_in_button()
        self.dashboard_page.click_on_the_add_player_link()
        self.add_a_player_page.type_in_name('Mateusz')
        self.add_a_player_page.type_in_surname('Młyński')
        self.add_a_player_page.type_in_age('02012001')
        self.add_a_player_page.type_club('Wisła Kraków')
        self.add_a_player_page.type_main_position('Winger')
        self.add_a_player_page.type_leg_field()
        self.add_a_player_page.type_right_leg()
        self.add_a_player_page.click_submit_button()
        time.sleep(3)


    @classmethod
    def tearDown(self):
        self.driver.quit()
