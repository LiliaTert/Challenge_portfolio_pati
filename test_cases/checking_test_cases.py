import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

# Test_case_1.1. User authorization on the site using valid data:
driver = webdriver.Chrome()
driver.get('https://scouts-test.futbolkolektyw.pl/')
driver.maximize_window()

login = 'user10@getnada.com'
login_field_xpath = "//*[@id='login']"
field_login = driver.find_element('xpath', login_field_xpath)
field_login.send_keys(login)

password = 'Test-1234'
password_field_xpath = "//*[@id='password']"
field_password = driver.find_element('xpath', password_field_xpath)
field_password.send_keys(password)

sign_in_button_xpath = "//span[contains(text(),'Sign in')]"
WebDriverWait(driver, 10).until(EC.presence_of_element_located(('xpath', sign_in_button_xpath)))
button_sign_in = driver.find_element('xpath', sign_in_button_xpath)
button_sign_in.click()

# Test_case_3.1. Adding a new player in the "Add player" form using valid data.
add_player_link_xpath = "//span[text()='Add player']"
WebDriverWait(driver, 10).until(EC.presence_of_element_located(('xpath', add_player_link_xpath)))
add_player_link = driver.find_element('xpath', add_player_link_xpath)
add_player_link.click()

name_field_xpath = "//input[@name='name']"
name = 'Mateusz'
WebDriverWait(driver, 10).until(EC.presence_of_element_located(('xpath', name_field_xpath)))
name_field = driver.find_element('xpath', name_field_xpath)
name_field.send_keys(name)
time.sleep(3)

surname_field_xpath = "//input[@name='surname']"
surname = 'Młyński'
WebDriverWait(driver, 10).until(EC.presence_of_element_located(('xpath', surname_field_xpath)))
surname_field = driver.find_element('xpath', surname_field_xpath)
surname_field.send_keys(surname)
time.sleep(3)
age_field_xpath = "//input[@name='age']"
age = '02012001'
age_field = driver.find_element('xpath', age_field_xpath)
age_field.send_keys(age)
time.sleep(3)
select_leg_dropdown_list_xpath = "//div[@id='mui-component-select-leg']"
select_leg_dropdown_list = driver.find_element('xpath', select_leg_dropdown_list_xpath)
select_leg_dropdown_list.click()
right_leg_button_xpath = "//li[@data-value='right']"
WebDriverWait(driver, 10).until(EC.presence_of_element_located(('xpath', right_leg_button_xpath)))
right_leg_button = driver.find_element('xpath', right_leg_button_xpath)
right_leg_button.click()
time.sleep(3)
club_field_xpath = "//input[@name='club']"
club = 'Wisła Kraków'
club_field = driver.find_element('xpath', club_field_xpath)
club_field.send_keys(club)
time.sleep(3)

mainPosition_field_xpath = "//input[@name='mainPosition']"
mainPosition = 'Winger'
mainPosition_field = driver.find_element('xpath', mainPosition_field_xpath)
mainPosition_field.send_keys(mainPosition)
time.sleep(3)

submit_button_xpath = "//span[contains(text(),'Submit')]"
WebDriverWait(driver, 10).until(EC.presence_of_element_located(('xpath', submit_button_xpath)))
submit_button = driver.find_element('xpath', submit_button_xpath)
submit_button.click()
time.sleep(3)

# Test_case_4.1. Checking the search by filter:
players_link_xpath = "//span[text()='Players']"
WebDriverWait(driver, 10).until(EC.presence_of_element_located(('xpath', players_link_xpath)))
players_link = driver.find_element('xpath', players_link_xpath)
players_link.click()
time.sleep(3)

filter_icon_xpath = "//button[@aria-label='Filter Table']/span[@class='MuiIconButton-label']"
WebDriverWait(driver, 15).until(EC.presence_of_element_located(('xpath', filter_icon_xpath)))
filter_icon = driver.find_element('xpath', filter_icon_xpath)
filter_icon.click()
time.sleep(3)

filter_field_surname_xpath = "//div[@data-testid='filtertextfield-surname']/div/input"
surname_filter = "Młyński"
WebDriverWait(driver, 15).until(EC.presence_of_element_located(('xpath', filter_field_surname_xpath)))
filter_field_surname = driver.find_element('xpath', filter_field_surname_xpath)
filter_field_surname.send_keys(surname_filter)
time.sleep(4)

close_filter_table_icon_xpath = "//button[@aria-label='Close']"
WebDriverWait(driver, 10).until(EC.presence_of_element_located(('xpath', close_filter_table_icon_xpath)))
close_filter_table_icon = driver.find_element('xpath', close_filter_table_icon_xpath)
close_filter_table_icon.click()
time.sleep(3)


# Make screenshots from the site pages":
links = ['https://scouts-test.futbolkolektyw.pl/', 'https://scouts-test.futbolkolektyw.pl/',
'https://scouts-test.futbolkolektyw.pl/en/players/add', 'https://scouts-test.futbolkolektyw.pl/en/players',
'https://scouts-test.futbolkolektyw.pl/en/players?lng=en&subpath=en&start=1&surname_contains=M%C5%82y%C5%84ski']
for i in range(len(links)):
    driver.get(links[i])
    print(driver.title)
    driver.get_screenshot_as_file(f'{i}.png')