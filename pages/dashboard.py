from pages.base_page import BasePage
import time

class Dashboard(BasePage):
    expected_title = 'Scouts panel'
    dashboard_url = ('https://scouts-test.futbolkolektyw.pl/')
    scounts_panel_header_xpath = "//h6[text()='Scouts Panel']"
    header_of_box = 'Scouts Panel'
    main_page_link_xpath = "//span[text()='Main page']"
    players_link_xpath = "//span[text()='Players']"
    polski_link_xpath = "//span[text()='Polski']"
    sign_out_link_xpath = "//span[text()='Sign out']"
    players_count_section_xpath = "//div[text()='Players count']"
    matches_count_section_xpath = "//div[text()='Matches count']"
    reports_count_section_xpath = "//div[text()='Reports count']"
    events_count_section_xpath = "//div[text()='Events count']"
    shortcuts_section_xpath = "//h2[text()='Shortcuts']"
    add_player_link_xpath = "//span[text()='Add player']"
    logo_xpath = "//div[@title='Logo Scouts Panel']"

    def check_title_of_header(self):
        self.assert_element_text(self.driver, self.scounts_panel_header_xpath, self.header_of_box)

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
    def click_on_the_add_player_link(self):
        self.click_on_the_element(self.add_player_link_xpath)




