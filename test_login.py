import pytest
import openpyxl
from Baseclass import BaseClass
from selenium import webdriver

@pytest.mark.usefixtures("setup")
class Testguruproject():
    def test_guruproject(self):
        self.driver.implicitly_wait(10)
        path="/home/pi/Documents/project_Guru99/user credential.xlsx"
        
        rows=BaseClass.getrowcount(path, "Sheet1")
        
        for r in range(2,rows+1):
            username=BaseClass.readData(path,"Sheet1",r,2)
            password=BaseClass.readData(path,"Sheet1",r,3)
            self.driver.find_element_by_name('uid').send_keys(username)
            self.driver.find_element_by_name('password').send_keys(password)
            self.driver.find_element_by_xpath("//input[@name='btnLogin']").click()
            
            try:
                alertobj=self.driver.switch_to.alert
                message=alertobj.text
                alertobj.accept()
                BaseClass.writedata(path,"Sheet1",r,4,"Test Failed")
            except:
                welcomename=self.driver.find_element_by_class_name('heading3')
                assert "Welcome To Manager's Page of Guru99 Bank" in welcomename.text
                self.driver.get_screenshot_as_file("/home/pi/Documents/project_Guru99/image.png")
                self.driver.find_element_by_xpath("//a[contains(text(),'Log out')]").click()
                logoutalert=self.driver.switch_to.alert
                logoutalert.accept()
                BaseClass.writedata(path,"Sheet1",r,4,"Test Passed")
                
           
        


        
        
                
               


   