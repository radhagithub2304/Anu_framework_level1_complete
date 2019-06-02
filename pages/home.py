class Homepage:
    def __init__(self,driver):
        self.driver=driver
        self.logout="//b[text()='log out']"
    def logout_method(self):
        self.driver.find_element_by_xpath(self.logout).click()

# Step5:
# In steps 5,we will keep all the locators at one place so that any changes,it will reflect everywhere
# from it.
# So,we are creating page wise python file eg:Login apge ,Home page

# Create a class
# Now,place all the locators in constructor(declare it)
# Also,put the locators in different methods over here for respective pages

