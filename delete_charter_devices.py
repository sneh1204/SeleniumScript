from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://charter.guestinternet.com/")

sleep(1.0)

driver.find_element(value='Username').send_keys('ut-36866')
driver.find_element(value='Password').send_keys('5945')
driver.find_element(value='Location').click()
driver.find_element(by=By.XPATH, value="//*[contains(text(), 'William Douglas')]").click()
driver.find_element(by=By.CLASS_NAME, value='btn').click()

sleep(1.0)

safe_mac = ['80-45-DD-74-B8-73', '5C-52-30-2E-31-9D', '34-AF-B3-FB-B0-EB', 'B0-E5-F9-A3-9B-53', 'AC-BC-32-5F-A3-44', '0E-27-71-26-EC-3C', '04-ED-33-F7-B8-D1', '04-ED-33-F7-B8-D5']
cur_del = 1
for i in range(1000):
    mac = driver.find_element(by=By.XPATH, value='//table/tbody/tr['+str(cur_del)+']/td[2]').text
    name = driver.find_element(by=By.XPATH, value='//table/tbody/tr[' + str(cur_del) + ']/td[1]').text
    if mac not in safe_mac and not name.lower().startswith('ip'):
        driver.find_element(by=By.XPATH, value="//table/tbody/tr["+str(cur_del)+"]/td[4]/a").click()
        driver.find_element(by=By.CLASS_NAME, value='btn-danger').click()
    else:
        cur_del += 1
    sleep(1.5)

driver.quit()
