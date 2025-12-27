
from selenium import webdriver
import pytest
import allure
import driver
import time

@allure.title("Print the page source")

def test_selenium():
   driver=webdriver.Edge()
   driver.get("https://katalon-demo-cura.herokuapp.com/")
   page_source_as_html= driver.page_source
   print(driver.title)
   print(driver.current_url)
   assert "CURA Healthcare Service" in page_source_as_html
   driver.quit()