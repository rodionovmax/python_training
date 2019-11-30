from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = WebDriver(executable_path='/Users/max/sanbox_python/python_training/chromedriver')
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)

    def return_to_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("group page").click()

    def create_group(self, group):
        driver = self.driver
        self.open_groups_page()
        # init group creation
        driver.find_element_by_name("new").click()
        # fill out group form
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        driver = self.driver
        # open groups page
        driver.find_element_by_link_text("groups").click()

    def open_home_page(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()