import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    username_id="user-name"
    password_id="password"
    login_button="login-button"
    menu = '//button[@id="react-burger-menu-btn"]'
    logout='//a[@id="logout_sidebar_link"]'


    def __init__(self,driver):
        self.driver=driver

    def set_username(self, username):
        self.driver.find_element(By.ID, self.username_id).clear()
        self.driver.find_element(By.ID, self.username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID,self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_button).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.menu).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.logout).click()
