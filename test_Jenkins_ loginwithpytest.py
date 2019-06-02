# Step3:Install pytest package and change naming convention eg.Method name should start with
# test_ and  file name should start with test_
# and donot call the functions
# import time
#
# from selenium import webdriver
# def test_launch_browser():
#     global driver
#     driver = webdriver.Chrome()
#     driver.get("http://localhost:8080/login?from=%2F")
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#
# def test_login():
#     driver.find_element_by_id("j_username").send_keys("admin")
#     driver.find_element_by_name("j_password").send_keys("manager")
#     driver.find_element_by_name("Submit").click()
# def test_logout():
#     time.sleep(5)
#     driver.find_element_by_xpath("//b[text()='log out']").click()


# Advantage is that:Here no need to call the functions instead run the test scripts
# from terminal itself andtype run>>python -m pytest
# Note:It will show 3 test cases collected because we have 3 methods starting from test_


# Output is displayed as :DevTools listening on ws://127.0.0.1:61093/devtools/browser/534796fb-655b-4990-96a0-54103ac35e96
# ...                                                                                                       [100%]
#
# =========================================================== 3 passed in 13.24 seconds
# ******************************************************************************
# *****************************************************************************

# Step4:
# Write @pytest.fixture at the top of test_launchbrowser() method.Fixture is just like precondition
# and postcondition.
# Again we have 1.@pytest.fixture(scope='session')-In this test_launchbrowser() will be executed only once
# prior to all the test methods.For eg:If there are 100 test cases,it will execute only once
# Similarly we have 2.@pytest.fixture(scope='function')-In this test_launchbrowser() will be executed
# prior to all the test methods.
# For eg:test_launchbrowser()_> login()
# test_launchbrowser()>logout() and so on


# import time
# import pytest
#
# from selenium import webdriver
# @pytest.fixture(scope='function')
# def test_launch_browser():
#     global driver
#     driver = webdriver.Chrome()
#     driver.get("http://localhost:8080/login?from=%2F")
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#
# def test_login(test_launch_browser):
#     driver.find_element_by_id("j_username").send_keys("admin")
#     driver.find_element_by_name("j_password").send_keys("manager")
#     driver.find_element_by_name("Submit").click()
#
# def test_logout(test_launch_browser):
#     time.sleep(5)
#     driver.find_element_by_xpath("//b[text()='log out']").click()
# Note1:
# //@pytest.fixture(scope='function') is added above the Function test_launch_browser()
#  And we provide the "test_launch_browser" inside the parenthesis of the other two functions
# eg:
# def test_login(test_launch_browser): and def test_logout(test_launch_browser):
#
# Note2:
# It should be noticed that it will collect only 2 items as of now on execution since
# "test_launch_browser" is not testcase now instead it is precondition:
# Also when scope is session its 100 percentr passed and only one browser will be opened
# For eg:launch>login>logout,but in function its 50 percent pass and 50 percent fail and we
#can see two browsers opened.launch>login and launch>logout

# Note3:For execution,we open in terminal and type python -m pytest -v
#

# Step 5:
# import time
# import pytest
# from pages.login impor nju======================00t Loginpage
# from pages.home import Homepage
# from selenium import webdriver
# @pytest.fixture(scope='session')
# def test_launch_browser():
#     global driver
#     driver = webdriver.Chrome()
#     driver.get("http://localhost:8080/login?from=%2F")
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#
# def test_login(test_launch_browser):
#     lp=Loginpage(driver)
#     lp.enterusername()
#     lp.enterpassword()
#     lp.clicksigninbutton()
# def test_logout(test_launch_browser):
#     time.sleep(5)
#     hp=Homepage(driver)
#     hp.logout_method()
#
# # Note:
# In steps 5,we will keep all the locators at one place so that any changes,it will reflect everywhere
# from it.
# So,we are creating page wise python file eg:Login apge ,Home page

 #And in the test file,we will remove the locators line and craete an object of the class and access
# the methods of respective pages by calling it over here

# # Step6:-----------

# import time
# import pytest
# from pages.login import Loginpage
# from pages.home import Homepage
# from selenium import webdriver
# class Testjenkinslogin:
#     @pytest.fixture(scope='class')
#     def test_launch_browser(self):
#         global driver
#         driver = webdriver.Chrome()
#         driver.get("http://localhost:8080/login?from=%2F")
#         driver.maximize_window()
#         driver.implicitly_wait(10)
#
#     def test_login(self,test_launch_browser):
#         lp = Loginpage(driver)
#         lp.enterusername()
#         lp.enterpassword()
#         lp.clicksigninbutton()
#
#     def test_logout(self,test_launch_browser):
#         time.sleep(5)
#         hp = Homepage(driver)
#         hp.logout_method()
# Introduce class into test file and place all the test methods inside a class.Class name should
# start the class with test_ and change its scope to test.
# Put self argument for all the methods:
#     def test_launch_browser(self):
#     def test_login(self, test_launch_browser):
#     def test_logout(self, test_launch_browser):

# Step7:

# import time
# import pytest
# from pages.login import Loginpage
# from pages.home import Homepage
# from selenium import webdriver
# class Testjenkinslogin:
#     @pytest.fixture(scope='class')
#     def test_launch_browser(self):
#         global driver
#         driver = webdriver.Chrome()
#         driver.get("http://localhost:8080/login?from=%2F")
#         driver.maximize_window()
#         driver.implicitly_wait(10)
#         yield
#         driver.quit()
#
#     def test_login(self,test_launch_browser):
#         lp = Loginpage(driver)
#         lp.enterusername()
#         lp.enterpassword()
#         lp.clicksigninbutton()
#
#     def test_logout(self,test_launch_browser):
#         time.sleep(5)
#         hp = Homepage(driver)
#         hp.logout_method()


# At the bottom of the method "test_launchbrowser()" add a key word "yield"
# # # any statements under yield will be considered as a post condition

# Step8:
# Step8 is adding a conftest file where ,We have removed the code from step 7 ie.starting from
# @pytest.fixture(scope='class') to driver.quit() and paste
#  it in conftest file
# Step9:
# Basically we are saying usefixture ie "test_launch_browser" which is in conftest file
import time
import pytest
from pages.login import Loginpage
from pages.home import Homepage
@pytest.mark.usefixtures("test_launch_browser")
class Testjenkinslogin:

    def test_login(self):
        driver=self.driver
        lp = Loginpage(driver)
        lp.enterusername()
        lp.enterpassword()
        lp.clicksigninbutton()

    def test_logout(self):
        driver=self.driver
        time.sleep(5)
        hp = Homepage(driver)
        hp.logout_method()

# Note:In step 9:
# On the top of testclass ie Testjenkinslogin:,write the below fixture as @pytest.mark.usefixture("test_launch_browser")
# Now, write the code as below:
# @pytest.mark.usefixture("test_launch_browser")
# class Testjenkinslogin:
#
#     def test_login(self):
#         driver=self.driver
# since we are using the fixture,"test_launch_browser" so remove it from parenthesis of
#  def test_login and test_logout methods
#  and then initialize the decalre driver=self.driver

# Step10:Install allure pytest pacakge.Download allure pytest bat file in local system and set the environment
# variable for it.Note allure is a 3rd party reporting tool

# Find the below steps for the same.
# Step1:Install allure-pytest package
# Step2:http://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.7.0/>Go to this url>3rd link>2.7.0zip Download iter()
# Step3:we will get 4 options:

# Now select the 3rd option>allure-2.7.0.zip.Extract the file .open the folder>Go to bin>copy path
# from header section.Right click on My computer>properties>Advance system properties>Environment
# variables>system variable>path>edit>paste it.
#
# Go to command prompt>Type allure --version>>Restart the system
# Again do allure --version
# We get the error as:ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.
#
# Please set the JAVA_HOME variable in your environment to match the
# location of your Java installation.
#
# Hence,install java and set its path now(Google it).
# Go to cmd and type java -version>12.0.1
# and javac -version>12.01
# Now we do allure --version in cmd>>We get 2.7.0

# Step11:Create a report directory or folder
# Step12:To generate allure report,execute below command-
# Go to the project>Right click on project name provided in left pane>Open in terminal>>
# then type the command as given below:
# 1.python -m pytest --alluredir reports
# Then wait for the code to get executed.And after that type the another command....
# Hence once the execution is done,to see the HTML report,execute the below command
# # 2.allure serve reports

# HTML report generation...............
# Create rep.html under reports folder.
# Now Select project>Show in exlorer>>Select the project(Anuradha POM framework level 1)>>
# then in address bar>>type cmd.So we are in cmd and execute
# python -m pytest -v --html=reports/rep.html.
# Execution of script is done.
# Go to pycharm>>Project>>reports>>rep.html>>open in browser and see the html report



# This is all about label 1 framework....Thanks