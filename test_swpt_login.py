from selenium import webdriver
from page.login_swsp import Login_swsp
import unittest
import ddt


TesDate=[{"username":"wangnan","pws":"Aa123456"},{"username":"wudi","pws":"Aa123456"},{"username":"yangwensheng","pws":"Aa123456"}]

@ddt.ddt
class Swsp_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        url="http://10.3.108.25:9001/"
        cls.driver.get(url)
        #实例化
        cls.log=Login_swsp(cls.driver)

    @ddt.data(*TesDate)
    def test001(self,params):
        print(params)
        res=self.log.login(params["username"],params["pws"])
        except_res=True
        self.assertEqual(res,except_res)

    def tearDown(self):
        self.log.login_out()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=="__main__":
    unittest.main()