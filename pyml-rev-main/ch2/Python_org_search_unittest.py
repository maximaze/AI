# 단위 테스트
# 파일이름 : Python_org_search_unittest.py
# 사이트 : https://selenium-python.readthedocs.io/getting-started.html

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME,"q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No result found.", driver.page_source)
        
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()