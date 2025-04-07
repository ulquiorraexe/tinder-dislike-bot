from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[@id="s1524772468"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()
sleep(5)
by_number = driver.find_element(By.XPATH, value='//*[@id="s1746112904"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button')
by_number.click()
sleep(2)
number_input = driver.find_element(By.NAME, value="phone_number")
number_input.send_keys("", Keys.ENTER)
sleep(5)
number_code = input("Please type the code that they sent you: ")
for index in range(0, 7):
    code_inputs = driver.find_elements(By.XPATH, '//*[@id="s1746112904"]/main/div/div[1]/div/div[2]/div/div[1]/div[2]/input')
    if index < len(code_inputs):
        code_inputs[index].send_keys(number_code[index])
    else:
        print("Not enough code input boxes found.")
go_to_mail = driver.find_element(By.XPATH, value='//*[@id="s1746112904"]/main/div/div[1]/div/div[4]/button')
go_to_mail.click()
sleep(2)
mail_auth = driver.find_element(By.XPATH, value='//*[@id="s1746112904"]/main/div/div/div[1]/div/div[2]/button')
mail_auth.click()
sleep(2)
mail_code = input("Please type the code: ")
