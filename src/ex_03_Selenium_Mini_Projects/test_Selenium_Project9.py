from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


def test_vwo_login_invalid_credentials():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(chrome_options)

    # Open VWO Login Page
    driver.get("https://app.vwo.com/#/login")

    # Locate Email field and enter email
    email_input = driver.find_element(By.ID, "login-username")
    email_input.send_keys("admin@admin.com")

    # Locate Password field and enter password
    password_input = driver.find_element(By.ID, "login-password")
    password_input.send_keys("admin")

    # Locate and click Login button
    login_button = driver.find_element(By.ID, "js-login-btn")
    login_button.click()

    # Wait for error message to appear
    time.sleep(3)

    # Locate error message
    error_msg = driver.find_element(By.CLASS_NAME, "notification-box-description")

    # Assertion
    assert "Your email, password, IP address or location did not match" in error_msg.text

    # Close browser
    driver.quit()














