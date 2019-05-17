import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep


browser= webdriver.Firefox();
browser.get('https://finance.yahoo.com/quote/TSLA?');
sleep(5)

span_element = browser.find_element_by_xpath('//span[@class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"]')
print(span_element.text)

browser.close()
browser.quit()
