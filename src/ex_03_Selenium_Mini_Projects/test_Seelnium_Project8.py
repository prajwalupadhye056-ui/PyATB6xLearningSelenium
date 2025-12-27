from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


def test_project_1_katalon_negative():
    chrome_options= Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)


    driver.get("https://katalon-demo-cura.herokuapp.com/")
    make_appointment_btn= driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_btn.click()

    time.sleep(5)

    user_input=driver.find_element(By.NAME,"username")
    user_input.send_keys("pramod")

    password_input=driver.find_element(By.NAME,"password")
    password_input.send_keys("ThisIs")

    login_button=driver.find_element(By.ID,"btn-login")
    login_button.click()
    time.sleep(2)

    p_error_message= driver.find_element(By.CLASS_NAME,"text-danger")
    print(p_error_message.text)

    assert   "Login failed! Please ensure the username and password are valid." == p_error_message.text



    time.sleep(5)
    driver.quit()
