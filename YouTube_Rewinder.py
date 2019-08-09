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
except:
	print("It took longer than 10 seconds. Check your net connectivity!")
	chromeDriver.quit()

song = chromeDriver.find_element_by_xpath("//ytd-video-renderer[1]/div/ytd-thumbnail/a[1]")
song.click()

# try:
# 	# need to wait until url changes. Only after that should I wait for the 'video' to be present!
# 	video = wait.until(EC.presence_of_element_located("//video[1]"))
# except:
# 	print("2nd wala. It took longer than 10 seconds. Check your net connectivity!")
# 	chromeDriver.quit()

# time_duration = chromeDriver.find_element_by_xpath("//span[@class='ytp-time-duration']").getText()
# print(time_duration)