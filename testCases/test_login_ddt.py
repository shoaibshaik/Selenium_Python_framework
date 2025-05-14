import time
import os
import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utils.properties import ReadConfig
from utils.logger import LogGen
from utils import xlUtlis


class Test_002_DDT_Login:
    baseURL=ReadConfig.getApplicationUrl()
    path = os.path.join('.', 'TestData', 'login_users.xlsx')
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info('********************************    Test_002_DDT_Login   ********************************')
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

    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info(
            '********************************    Verifying test_login   ********************************')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.rows = xlUtlis.getRowCount(self.path,"Sheet1")
        print(self.rows)
        lst_status=[]
        for r in range(2,self.rows+1) :
            self.user=xlUtlis.readData(self.path,"Sheet1",r,1)
            self.password=xlUtlis.readData(self.path,"Sheet1",r,2)
            self.expected=xlUtlis.readData(self.path,"Sheet1",r,3)
            self.lp.set_username(self.user)
            self.lp.set_password(self.password)
            self.lp.click_login()
            time.sleep(2)
            act_url = self.driver.current_url
            expt_url = "https://www.saucedemo.com/inventory.html"
            if act_url == expt_url:
                if self.expected=="pass":
                    self.logger.info(
                    '********************************    DDT_test_login Passed   ********************************')
                    self.lp.click_logout()
                    lst_status.append("pass")
                elif self.expected=="fail":
                    self.logger.info(
                        '********************************   DDT_ test_login failed   ********************************')
                    try:
                        self.lp.click_logout()
                    except Exception as e:
                        self.logger.warning(f"Logout skipped due to error: {e}")

                    lst_status.append("fail")
            elif act_url != expt_url :
                if self.expected=="pass":
                    self.logger.info(
                    '********************************    DDT_test_login failed   ********************************')
                    try:
                        self.lp.click_logout()
                    except Exception as e:
                        self.logger.warning(f"Logout skipped due to error: {e}")

                    lst_status.append("fail")
                elif self.expected=="fail":
                    self.logger.info(
                        '********************************   DDT_ test_login passed   ********************************')
                    try:
                        self.lp.click_logout()
                    except Exception as e:
                        self.logger.warning(f"Logout skipped due to error: {e}")

                    lst_status.append("pass")
        print(lst_status)
        if "fail" not in lst_status:
            self.logger.info("******** Login_DDT_test_Passed ******** ")
            self.driver.close()
            assert True
        else:
            self.logger.info("******** Login_DDT_test_failed ******** ")
            self.driver.close()
            assert False


        self.logger.info("******** End of test case ********  ")
        self.logger.info("******** completed Test002 ********  ")













