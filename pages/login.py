from testdata.data import *
class Loginpage:
    def __init__(self,driver):
        self.driver=driver
        self.username="j_username"
        self.password="j_password"
        self.submitbtn="Submit"

    def enterusername(self):
        self.driver.find_element_by_id(self.username).send_keys(UN)

    def enterpassword(self):
         self.driver.find_element_by_name("j_password").send_keys(PW)
    def clicksigninbutton(self):
         self.driver.find_element_by_name("Submit").click()

# Step5:
# In steps 5,we will keep all the locators at one place so that any changes,it will reflect everywhere
# from it.
# So,we are creating page wise python file eg:Login apge ,Home page

# Create a class
# Now,place all the locators in constructor(declare it)
# Also,put the locators in different methods over here for respective pages

# Another note:---------------------------------------------------------
# # # Here as we are receiving the inputs from the data.py under testdata directory
# # # so we have to import file named as "data"  to this login page
# Hence we write  : from testdata.data import *
# and make changes from  self.driver.find_element_by_id(self.username).send_keys("admin") to
# self.driver.find_element_by_id(self.username).send_keys(UN)
# Similarly for password as well ie:
# self.driver.find_element_by_id(self.username).send_keys(PW)




