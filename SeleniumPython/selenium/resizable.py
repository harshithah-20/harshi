from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
#from idlelib.idle_test.test_colorizer import source
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://testautomationpractice.blogspot.com/")
#header=driver.find_element(By.XPATH,"//h3[@class='ui-widget-header']")
action=ActionChains(driver)
#action.click_and_hold(header).move_by_offset(100,0).perform()
resize=driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
action.scroll_to_element(resize).perform()
action.click_and_hold(resize).move_by_offset.perform()
#horizontal X value and vertically Y value
#offset means XY coordinates