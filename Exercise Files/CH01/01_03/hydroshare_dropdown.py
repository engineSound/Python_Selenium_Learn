from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("http://www.hydroshare.org")

elem_my_rsc = driver.find_element_by_id("dropdown-menu-my-resources")
elem_my_rsc.click()
time.sleep(2)
elem_user = driver.find_element_by_id("id_username")
elem_user.send_keys("hzhang@cuahsi.org")
elem_pwd = driver.find_element_by_id("id_password")
elem_pwd.send_keys("Vcxfds$32")
elem_submit_button=driver.find_elements_by_xpath("//input[@type='submit' and @value='Sign In']")[0]
elem_submit_button.click()
time.sleep(8)

driver.close()
