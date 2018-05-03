# coding:utf-8
from common.base import Base
from selenium import webdriver
from page.login_swsp import Login_swsp
import time
class New_doc_swsp(Base):
    #财务流程
    cwbt=("xpath",".//*[@id='quanxian']/ul[1]/li[2]")
    #调整预算
    tzys=("xpath","//*[@id='quanxian']/ul[1]/li[2]/div[2]/ul/li[2]/span[1]")
    #多个拟稿部门提示框
    ngdw=("css selector","#ui-id-1")
    sure_but=("css selector",".buttonCon>button")

    #表单信息================
    #标题字段
    title=("id","OA_FIN_HFYSTZSPB-PROJECT_NAME")
    #概要字段
    gaiyao=("id","OA_FIN_HFYSTZSPB-DIGEST")
    #新建保存按钮
    new_savebut=("xpath",".//*[@id='OA_FIN_HFYSTZSPB-save']")
    #下一任务按钮
    send_next=("id","OA_FIN_HFYSTZSPB-cmSaveAndSend")

    #下一任务提交页面
    clr=("css selector",".rh-combobox-input")
    sel_clr=("css selector",".rh-menu-item-wrapper")
    sel_but=("css selector",".buttonCon>button")

    #启动任务
    def start_doc(self):
        self.moveto_element(self.cwbt)
        self.click_element(self.tzys)
    def inner_doc(self,titlestr,gaiyaostr):
        #判断是否为多部门
        try:
            self.text_to_be_in_element_value(self.ngdw,"请选择拟稿单位")
            self.click_element(self.sure_but)
        except:
            pass
        self.sendkeys(self.title,titlestr)
        self.sendkeys(self.gaiyao,gaiyaostr)
    #第一次保存
    def new_save_doc(self):
        self.click_element(self.new_savebut)
    #点击下一任务按钮
    def send_next_doc(self):
        print("点击下一任务")
        self.click_element(self.send_next)
        print("点击完成")
    #下一任务选择人员和环节
    def sel_ry(self):
        print(self.clr)
        self.driver.find_element_by_css_selector('.rh-combobox-input')
        print("找到了")
        self.find_element(self.clr)
        print("zd")
        self.click_element(self.clr)
        self.click_elements(self.sel_clr,0)
        self.click_elements(self.sel_but,0)

if __name__=="__main__":
    profileDir=r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\l74gyfwz.default-2109139698818"
    profile=webdriver.FirefoxProfile(profileDir)
    driver=webdriver.Firefox(profile)
    url="http://10.3.108.25:9001/"
    driver.get(url)
    log=Login_swsp(driver)
    log.login("wangnan","Aa123456")
    #切换handle到个人门户
    log.switch_handle()
    #启动任务-调整预算
    newdoc=New_doc_swsp(driver)
    newdoc.start_doc()
    #切换handle调整预算表单窗口
    log.switch_handle()
    newdoc.inner_doc("自动化0013","自动化002")
    #点击保存按钮
    newdoc.new_save_doc()
    #========time.sleep(10)
    #点击下一任务按钮
    newdoc.send_next_doc()
    time.sleep(5)
    newdoc.sel_ry()

    print("ok")

    driver.quit()