from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


def test_project_1_katalon_positive():
    chrome_options= Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)


    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_btn= driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_btn.click()

    time.sleep(5)

    user_input=driver.find_element(By.NAME,"username")
    user_input.send_keys("John Doe")

    password_input=driver.find_element(By.NAME,"password")
    password_input.send_keys("ThisIsNotAPassword")

    login_button=driver.find_element(By.ID,"btn-login")
    login_button.click()
    time.sleep(2)

    assert driver.current_url =="https://katalon-demo-cura.herokuapp.com/#appointment"
    time.sleep(5)
    driver.quit()




