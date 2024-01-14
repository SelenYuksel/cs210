from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
login_url = "https://www.trendyol.com/giris"
purchases_url = "https://www.trendyol.com/hesabim/siparislerim"

#used environment variables for privacy
email = os.environ.get('TRENDYOL_EMAIL')
password = os.environ.get('TRENDYOL_PASSWORD') 

driver = webdriver.Chrome()

try:
    # Navigate to the login page
    driver.get(login_url)

    # Find the email and password input fields, and submit the login form
    email_input = driver.find_element(By.ID, "login-email")
    password_input = driver.find_element(By.ID, "login-password-input")
    email_input.send_keys(email)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(3)
    # Locate and click on the link to "Tüm Siparişlerim" page
    driver.get(purchases_url)

    # Wait for dynamic content to load (adjust the wait time as needed)
    time.sleep(3)

    # Get the page source after dynamic content is loaded
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')
    image_wrapped_elements = soup.find_all('a', class_='image-wrapper')
    time_info = soup.find_all('div',class_='order-header-info')
    date_values = []
    for element in time_info:
        # Check if the element contains "Sipariş Tarihi"
        if "Sipariş Tarihi" in element.get_text():
            # Extract the date value
            date_value = element.find_next('b').get_text().strip()
            date_values.append(date_value)

    # Get all href values and save them to a file
    hrefs = [element.get('href') for element in image_wrapped_elements]
    base_url = "https://www.trendyol.com"
    hrefs = [f"{base_url}{element.get('href')}" for element in image_wrapped_elements]
    with open('hrefs.txt', 'w') as file:
        for href in hrefs:
            file.write(f"{href}\n")

    print("Hrefs saved to 'hrefs.txt'.")
    print(date_values)
finally:
    # Close the browser window
    driver.quit()