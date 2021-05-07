from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH ="C:\development\chromedriver.exe"

USERNAME = input('Enter instagram handle: ')
PASSWORD = input('Enter password: ')
ACCOUNT = input('Enter the account whose top 10 followers you want to follow: ')


class InstaFollower:
    def __init__(self, CHROME_DRIVER_PATH):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)


    def login(self, ig_handle, login_password):
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        username.send_keys(ig_handle)
        password.send_keys(login_password)
        log_in = self.driver.find_element_by_css_selector('button.sqdOP.L3NKy.y3zKF')
        log_in.click()


    def find_following(self,account_name):
        time.sleep(8)
        search = self.driver.find_element_by_css_selector('input.XTCLo.x3qfX')
        search.send_keys(account_name)
        time.sleep(5)
        account_name = self.driver.find_element_by_css_selector("._01UL2 a")
        account_name.click()
        time.sleep(8)
        following = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span')
        following.click()
        time.sleep(5)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(4)


    def follow(self):
        list = self.driver.find_elements_by_css_selector('ul.jSC57._6xe7A button')
        i = 0
        for button in list:
            if i<10:
                if button.text != "Follow":
                    print('Already Following')
                    i+=1
                else:
                    button.click()
                    time.sleep(2)
                    i += 1


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login(USERNAME, PASSWORD)
bot.find_following(ACCOUNT)
bot.follow()

