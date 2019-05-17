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
# Switch tab to the new tab, which we will assume is the next one on the right
# browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + Keys.TAB)
# 转换到这个标签去
browser.switch_to.window(browser.window_handles[1])
print(browser.current_url)
print(browser.title)
sleep(1)
browser.close();
browser.switch_to.window(browser.window_handles[0])
sleep(1)

# Work on second round
second_link = first_result.find_element_by_tag_name('a')
second_link.send_keys(Keys.COMMAND + Keys.RETURN)
sleep(3)
browser.switch_to.window(browser.window_handles[1])
print(browser.current_url)
print(browser.title)
sleep(1)
browser.close();
browser.switch_to.window(browser.window_handles[0])

#browser.get('https://finance.yahoo.com')
#sleep(2)
#browser.get('https://www.cnn.com')

browser.close()
browser.quit()
