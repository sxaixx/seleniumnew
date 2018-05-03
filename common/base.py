#cording:utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.action_chains import ActionChains
import time

class Base():
    def __init__(self,driver):
        self.driver=driver
        self.timeout=15
        self.poll_frequency=0.5
# 1查找元素=======================================================
    def find_element(self,locator):
        '''
        args:
        loctor 元祖，如（"id","xx"）
        '''
        ele=WebDriverWait(self.driver,self.timeout,self.poll_frequency).until(Ec.presence_of_element_located(locator))
        return ele

    def find_elements(self,locator):
        '''
        args:
        loctor 元祖，如（"id","xx"）
        '''
        ele=WebDriverWait(self.driver,self.timeout,self.poll_frequency).until(Ec.presence_of_all_elements_located(locator))
        return ele


# 2操作元素=======================================================
    def click_element(self,locator):
        #点击事件
        self.find_element(locator).click()

    def click_elements(self,locator,n):
        #点击list的第几个元素
        elements=self.find_elements(locator)
        if len(elements) < 1:
            print("没有找到元素")
        elif n > len(elements)-1:
            print("超过list的长度：%s" % len(elements))
        else:
            elements[n].click()

    def sendkeys(self,locator,text):
        #输入文本事件
        self.find_element(locator).send_keys(text)

    def clear_element(self,locator):
        #清除事件
        self.find_element(locator).clear()

    def moveto_element(self,locator):
        '''鼠标移动事件'''
        element=self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def text_persent_in_element(self,locator,text):
        #判断文本是否在元素文本中
        #元素本省文本为空也是false
        try:
            ele=WebDriverWait(self.driver,self.timeout,self.poll_frequency).until(Ec.text_to_be_present_in_element(locator,text))
            return ele
        except:
            return False

    def text_to_be_in_element_value(self,locator,text):
        #判断文本是否在元素的值中
        try:
            ele=WebDriverWait(self.driver,self.timeout,self.poll_frequency).until(Ec.text_to_be_present_in_element_value(locator,text))
            return ele
        except:
            return False

    def switch_handle(self):
        handles=self.driver.window_handles
        handle=handles[-1]
        self.driver.switch_to_window(handle)


if __name__=="__main__":
    driver=webdriver.Firefox()
    url="https://www.baidu.com/"
    driver.get(url)
    locator=("id","su")
    af=Base(driver)
    print(af.text_to_be_in_element_value(locator,"百度"))
    driver.quit()




