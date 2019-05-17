import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep


browser= webdriver.Firefox();
browser.get('https://www.google.com?q=python#q=python');


first_result = ui.WebDriverWait(browser, 5).until(lambda browser: browser.find_element_by_class_name('rc'))
main_window = browser.current_window_handle


first_link = first_result.find_element_by_tag_name('a')
# save the window opener (current window, do not mistaken with tab... not the same)
# Open the link in a new tab by sending key storkes on the element
# use: Keys.CONTRL + Keys.SHIFT + Keys.RETURN to open tab on top of the stack
# use: (MAC) Keys.COMMAND + Keys.SHIFT + Keys.RETURN to open tab on top of the stack
# 打开一个新的标签
first_link.send_keys(Keys.COMMAND + Keys.RETURN)
sleep(3)
browser.switch_to.window(browser.window_handles[1])
sleep(2)
browser.close()

# This has to be the last opening tab in the browser to make
# the quit() work
browser.switch_to.window(browser.window_handles[0])
browser.quit()
