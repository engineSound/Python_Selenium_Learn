################################################
################################################

# This example shows how to handle error

################################################
################################################
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep


browser= webdriver.Firefox();
browser.get('https://www.google.com?q=python#q=python');


first_result = ui.WebDriverWait(browser, 5).until(lambda browser: browser.find_element_by_class_name('rc'))
main_window = browser.current_window_handle


first_link = first_result.find_element_by_tag_name('a')
first_link.send_keys(Keys.COMMAND + Keys.RETURN)

sleep(2)

# set focus on the tab just opened.
browser.switch_to.window(browser.window_handles[1])

try:
    assert "Python titile" in browser.title
    print('Assertion test pass')

except Exception as e:
    print('Assertion test failed', format(e))

browser.quit()
