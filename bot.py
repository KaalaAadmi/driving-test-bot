import os
import sys
# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

def load_webpage(driver):
    driver.get("https://rsaie.queue-it.net/?c=rsaie&e=bsprodfeb&ver=v3-javascript-3.6.3&cver=37&man=Portal&t=https%3A%2F%2Fmyroadsafety.rsa.ie%2Fportal%2Fmy-goal%2F8efa0cc8-724e-ef11-af89-005056b9b50c&kupver=cloudflare-1.2.0")
    sleep(5)  # Wait for the page to load
    try:
        time_to_sleep=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[3]/div[1]/div[5]/div/p[3]/span[11]").text
    except NoSuchElementException:
        time_to_sleep = "less than a minute"
    print(f"Wait time for webpage to be accessible: {time_to_sleep}")
    if time_to_sleep == "less than a minute":
        time_to_sleep = 1
    else:
        time_to_sleep = int(time_to_sleep.split()[0])
    print(f"Sleeping for {time_to_sleep*1.5} minutes before proceeding...")
    sleep(int(time_to_sleep)*1.5* 60)  # Convert minutes to seconds and wait

def main():
    # options = Options()
    # options.add_argument(r"--user-data-dir=C:/Users/User01/AppData/Local/Google/Chrome/User Data")
    # options.add_argument(r'--profile-directory=Default')
    # driver = webdriver.Chrome(options=options)
    options=Options()
    options.add_argument(r"user-data-dir=/Users/arnavbhattacharya/Library/Application Support/Google/Chrome/Default")
    driver=webdriver.Chrome(options=options)
    load_webpage(driver)
    driver.refresh()
    print("Webpage loaded successfully. Refreshing...")
    sleep(5)
    print("Accepting cookies and closing warnings...")
    try:
        accept_cookies_button=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/div[3]/button").click()
    except NoSuchElementException:
        print("Accept cookies button not found.")
    sleep(1)
    print("Closing warning dialog...")
    try:
        close_warning_button=driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/mat-dialog-container/app-generic-dialog/div[1]/button").click()
    except NoSuchElementException:
        print("Close warning button not found.")
    sleep(1)
    username=os.getenv("USERNAME")
    password=os.getenv("PASSWORD")
    username_field=driver.find_element(By.XPATH,"/html/body/app-root/app-home/div/div/div[1]/div[2]/div/app-login/app-login-form/div/div[1]/div[2]/form/mat-form-field[1]/div/div[1]/div/input")
    password_field=driver.find_element(By.XPATH,"/html/body/app-root/app-home/div/div/div[1]/div[2]/div/app-login/app-login-form/div/div[1]/div[2]/form/mat-form-field[2]/div/div[1]/div[1]/input")
    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    sleep(5)
    print('Please enter otp in the browser and press Enter to continue...')
    otp=input()  # Wait for user to enter OTP in the browser
    for i in range(1,7):
        try:
            otp_field=driver.find_element(By.XPATH,f"/html/body/app-root/app-home/div/div/div/div[2]/div/app-two-factor/app-home-block/div/div[1]/div[6]/form/mat-form-field[{i}]/div/div[1]/div[3]/input")
            otp_field.send_keys(otp[i-1])  # Enter each digit of the OTP
            sleep(2) # Wait for a short time before entering the next digit
        except NoSuchElementException:
            print(f"OTP field {i} not found.")
    sleep(1)
    print("Submitting OTP...")
    submit_button=driver.find_element(By.XPATH,"/html/body/app-root/app-home/div/div/div/div[2]/div/app-two-factor/app-home-block/div/div[2]/div[2]/button")
    submit_button.click()
    sleep(5)
    print("OTP submitted successfully. Waiting for the next step...")
    
    sleep(60)
    
if __name__ == "__main__":
    main()