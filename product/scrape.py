from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

class Scraper:

    def get_table(self, site):
        self.site = site
        self.driver_path = "C:\minuuuur\chromedriver-win64\chromedriver.exe"
        self.service = Service(executable_path=self.driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(self.site)
        self.driver.implicitly_wait(10000)
        time.sleep(5)
        table = self.driver.find_element(By.CLASS_NAME, "dOwBOc")
        table_data = table.get_attribute('outerHTML')
        return table_data