from selenium import webdriver
import pytest
import allure

@allure.title("Print the page source")

def test_selenium():
   driver=webdriver.Chrome()
   driver.get("https://thetestingacademy.com")
   print(driver.page_source)
