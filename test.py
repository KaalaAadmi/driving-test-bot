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

USER_DIR=os.getenv("USER_DIR")
USER_PROFILE=os.getenv("USER_PROFILE")
options=Options()
options.add_argument(f"--user-data-dir={USER_DIR}")
#Here you specify the actual profile folder    
options.add_argument(f"--profile-directory={USER_PROFILE}")
# options.add_argument("--remote-debugging-port=9222")
options.add_argument('ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver=webdriver.Edge(options=options)
driver.get("https://yahoo.com")
sleep(5)  # Wait for the page to load
sleep(60)