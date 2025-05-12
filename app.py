from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome()






def login(driver,email,password):
   driver.get('https://in.linkedin.com/')
   wait = WebDriverWait(driver,10)

   button = wait.until(EC.element_to_be_clickable((By.XPATH,"""/html/body/main/section[1]/div/div/a""")))


   button.click()
   email_field = wait.until(EC.element_to_be_clickable((By.XPATH,"""/html/body/div/main/div[2]/div[1]/form/div[1]/input""")))
   email_field.send_keys(email)
   password_field = wait.until(EC.element_to_be_clickable((By.XPATH,"""/html/body/div/main/div[2]/div[1]/form/div[2]/input""")))
   password_field.send_keys(password)
   submit_login_button = wait.until(EC.element_to_be_clickable((By.XPATH,"""/html/body/div/main/div[2]/div[1]/form/div[4]/button""")))
   submit_login_button.click()

email = 'chsaimurali09@gmail.com'
password = 'SAI@8688346434'



def connections_info(driver):

  driver2 = driver.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')

def get_jobs_info(driver, job_title):
    driver.get('https://www.linkedin.com/feed/')

    wait = WebDriverWait(driver, 10)
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[6]/header/div/div/div/button/div""")))
    search_button.click()
    
    search_button_input = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[6]/header/div/div/div/div[1]/input""")))
    search_button_input.send_keys(job_title)
    search_button_input.send_keys(Keys.ENTER)
    
    posts_nav_button = wait.until(EC.element_to_be_clickable((By.XPATH, """/html/body/div[6]/div[3]/div[2]/section/div/nav/div/ul/li[2]/button""")))
    posts_nav_button.click()
    
    time.sleep(3)
    for _ in range(3):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

    more_buttons = driver.find_elements(By.XPATH, "//span[contains(text(), '…more')]")
    for button in more_buttons:
        driver.execute_script("arguments[0].click();", button)

    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    all_li_elements = soup.find_all('li', class_='artdeco-card mb2')
    
    for li in all_li_elements:
        # Find all span elements that contain job-related text inside each li
        span_tags = li.find_all('span', dir='ltr')
        for span in span_tags:
            text = span.get_text(strip=True)
            if text:
                print(text)




job_title = 'Python intern'
login(driver,email,password)
get_jobs_info(driver,job_title)
time.sleep(10)