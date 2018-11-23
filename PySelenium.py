from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# create a new FireFox session

driver = webdriver.Chrome('C:/Users/JIDDENIL/Downloads/chromedriver_win32/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://mytime.tieto.com/')
#driver.find_element_by_name("q").send_keys("http://www.tieto.com/")
driver.find_element_by_xpath("//*[@id='login_windows_button']").click()
driver.save_screenshot('C:/Users/JIDDENIL/Desktop/Other files/screenshot.png')
#time.sleep(5) # Let the user actually see something!
#driver.quit()

