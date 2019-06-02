from selenium import webdriver
from testdata.data import *
import pytest
@pytest.fixture(scope="class")
def test_launch_browser(request):
    global driver
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080/login?from=%2F")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()



# //Note:We have removed the code from @pytest.fixture(scope='class') to driver.quit() and paste
# it in conftest file

        #     @pytest.fixture(scope='class')
        #     def test_launch_browser(self):
        #         global driver
        #         driver = webdriver.Chrome()
        #         driver.get("http://localhost:8080/login?from=%2F")
        #         driver.maximize_window()
        #         driver.implicitly_wait(10)
        #         yield
        #         driver.quit()
# In conftest file,we have added precondition and post-condition and used the fixture
# " test_launch_browser" .
#
# Line no 4:def test_launch_browser(request):>We have to give request in parenthesis
# and     request.cls.driver = driver  needs to be added before yield.(yield is a return kind of statement)


# Another note:---------------------------------------------------------
# # # Here as we are receiving the inputs from the data.py under testdata directory
# # # so we have to import file named as "data"  to this conftest
# Hence we write  : from testdata.data import *
# And therefore changing driver.get("http://localhost:8080/login?from=%2F") to driver.get(URL)