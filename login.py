from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://www.demo.guru99.com/V4/index.php")
driver.implicitly_wait(10)

#valid credential
driver.find_element_by_name('uid').send_keys("mngr28072444ftvgb")
driver.find_element_by_name('password').send_keys("nYpdddUjAq")
driver.find_element_by_xpath("//input[@name='btnLogin']").click()
try:
    alertobj=driver.switch_to.alert
    message=alertobj.text
    print("i am running")
    alertobj.accept()
                
except:
    print("Wrong credential")
'''
    welcomename=driver.find_element_by_class_name('heading3')
    assert "Welcome To Manager's Page of Guru99 Bank" in welcomename.text
    self.driver.find_element_by_xpath("//a[contains(text(),'Log out')]").click() 

#invalid credential
driver.find_element_by_name('uid').send_keys("80724")
driver.find_element_by_name('password').send_keys("ngb vgftr")
driver.find_element_by_xpath("//input[@name='btnLogin']").click()'''

