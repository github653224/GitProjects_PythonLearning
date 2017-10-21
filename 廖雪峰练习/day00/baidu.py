from selenium import webdriver
driver= webdriver.Chrome(executable_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("周杰伦")
driver.find_element_by_id("su")
driver.maximize_window()