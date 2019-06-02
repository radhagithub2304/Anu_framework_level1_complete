# Step1:Create plain python file for login and logout to jenkins
# This code is for login into jenkins and logout from it
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://localhost:8080/login?from=%2F")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_id("j_username").send_keys("admin")
driver.find_element_by_name("j_password").send_keys("manager")
driver.find_element_by_name("Submit").click()
driver.find_element_by_xpath("//b[text()='log out']").click()


