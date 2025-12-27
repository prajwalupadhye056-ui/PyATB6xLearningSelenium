import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_idrive360_expired_trial_message():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    # Open URL
    driver.get("https://https://www.idrive360.com/enterprise/")

    # Enter Username
    username = wait.until(EC.presence_of_element_located((By.ID, "username")))
    username.send_keys("augtest_040823@idrive.com")

    # Enter Password
    password = driver.find_element(By.ID, "password")
    password.send_keys("123456")

    # Click Sign In
    sign_in_btn = driver.find_element(By.ID, "frm-btn")
    sign_in_btn.click()

    # Wait for red alert message
    alert_msg = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "idrive-red-alert")
        )
    )

    # Assertion
    assert "Your free trial has expired" in alert_msg.text

    driver.quit()












