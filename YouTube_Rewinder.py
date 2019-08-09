from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromeDriver = webdriver.Chrome()
chromeDriver.get("https://www.youtube.com")
search_field = chromeDriver.find_element_by_id("search")
search_field.clear() # clears any character (if any) present in input field
search_field.send_keys("Abhishek Varma Bekhayali")
search_field.send_keys(Keys.RETURN)