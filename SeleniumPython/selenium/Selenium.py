from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("http://www.amazon.com")
#driver.find_element_by_name('q').send_keys("selenium tutorial")
#driver.find_element("name","field-keywords").send_keys("Kurtas")
#driver.find_element("name","q").send_keys("Selenium tutorials python")
driver.maximize_window()
driver.find_element(By.XPATH,"//img[@alt='Spring summer']").send_keys("mobile")
#driver.find_element(Gmail.LINK_TEXT, 'Login').click()
send=driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()



