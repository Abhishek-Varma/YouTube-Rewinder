from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromeDriver = webdriver.Chrome()
chromeDriver.get("https://www.youtube.com")
search_field = chromeDriver.find_element_by_xpath("//input[@id='search']")
search_field.clear() # clears any character (if any) present in input field
song_to_search = "Abhishek Varma Bekhayali"
search_field.send_keys(song_to_search)
search_field.send_keys(Keys.RETURN)

wait = WebDriverWait(chromeDriver, 10)
try:
	wait.until(EC.title_contains(song_to_search))
	song_link = chromeDriver.find_element_by_xpath("//ytd-video-renderer[1]/div/ytd-thumbnail/a[1]")
	print(song_link.get_attribute('href'))
except:
	print("It took longer than 10 seconds. Check your net connectivity!")
	chromeDriver.quit()