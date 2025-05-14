import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utils.properties import ReadConfig
from utils.logger import LogGen
class Test_001_Login:
    baseURL=ReadConfig.getApplicationUrl()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info('********************************    Test_001_Login   ********************************')
        self.logger.info('********************************    Verifying test_homePageTitle   ********************************')
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Swag Labs":
            assert True
            self.driver.close()
            self.logger.info('********************************    test_homePageTitle Passed   ********************************')
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info('********************************    test_homePageTitle Failed   ********************************')
            assert False

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info(
            '********************************    Verifying test_login   ********************************')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title
        if act_title == "Swag Labs":
            assert True
            self.driver.close()
            self.logger.info('********************************    test_login Passed   ********************************')
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.info('********************************    test_login Failed   ********************************')
            assert False






