# coding:utf-8
from common.base import Base
from selenium import webdriver

class Login_swsp(Base):
    userId=("id","userId")
    password=("id","password")
    loginBtn=("id","loginBtn")
    swpt=("xpath",".//*[@id='ssolist']/li[8]/a/span")
    def login(self,username,psw):
        self.clear_element(self.userId)
        self.sendkeys(self.userId,username)
        self.sendkeys(self.password,psw)
        self.click_element(self.loginBtn)
        try:
            swsp_but=self.find_element(self.swpt)
            swsp_text=swsp_but.text
            if swsp_text=="新办公平台":
                swsp_but.click()
                return True
            else:
                print("未找到新办公平台系统!")
                return False
        except:
            print("登录失败")
            return False


    def login_out(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        #self.driver.quit()
if __name__=="__main__":
    driver=webdriver.Firefox()
    url="http://10.3.108.25:9001/"
    driver.get(url)
    a=Login_swsp(driver)
    a.login("wudi","Aa123456")
    a.login_out()