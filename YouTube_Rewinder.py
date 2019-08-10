from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# class element_has_class(object):
# 	def __init__(self, locator, css_class):
# 	self.locator = locator
# 	self.css_class = css_class

# 	def __call__(self, driver):
# 	element = driver.find_element()   # Finding the referenced element
# 	if self.css_class in element.get_attribute("class"):
#     	return element
# 	else:
#     	return False


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
except:
	print("It took longer than 10 seconds. Check your net connectivity!")
	chromeDriver.quit()

current_url = chromeDriver.current_url
print(current_url)
song = chromeDriver.find_element_by_xpath("//ytd-video-renderer[1]/div/ytd-thumbnail/a[1]")
song_link = song.get_attribute('href')
song.click()
print(song_link)

try:
	# need to wait until url changes. Only after that should I wait for the 'video' to be present!
	wait.until(EC.url_changes(current_url))
	# wait.until(EC.visibilityOfElementLocated(By.CLASS("ytp-play-button ytp-button")))
	# print("Current url -> "+str(chromeDriver.current_url))
except:
	print("It took longer than 10 seconds for the url to change. Check your net connectivity!")
	chromeDriver.quit()

while True:
	try:
		play_button = chromeDriver.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
	except:
		continue
	if play_button.get_attribute('title')=="Replay":
		play_button.click()
		break

# total_duration = chromeDriver.find_element_by_xpath("//span[@class='ytp-time-duration']")
# print(total_duration.getText())
# time.sleep(2)
# play_button.click()
# time_duration = chromeDriver.find_element_by_xpath("//span[@class='ytp-time-duration']").getText()
# print(time_duration)