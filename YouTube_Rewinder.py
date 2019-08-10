from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def YouTube_Rewind():
	chromeDriver = webdriver.Chrome()
	chromeDriver.get("https://www.youtube.com")
	for song_to_search in song_list:
		search_field = chromeDriver.find_element_by_xpath("//input[@id='search']")
		search_field.clear() # clears any character (if any) present in input field
		search_field.send_keys(song_to_search)
		search_field.send_keys(Keys.RETURN)

		wait = WebDriverWait(chromeDriver, 10)
		try:
			wait.until(EC.title_contains(song_to_search))
		except:
			print("It took longer than 10 seconds. Check your net connectivity!")
			chromeDriver.quit()

		current_url = chromeDriver.current_url
		song = chromeDriver.find_element_by_xpath("//ytd-video-renderer[1]/div/ytd-thumbnail/a[1]")
		song_link = song.get_attribute('href')
		song.click()

		try:
			# need to wait until url changes. Only after that should I wait for the 'video' to be present!
			wait.until(EC.url_changes(current_url))
		except:
			print("It took longer than 10 seconds for the url to change. Check your net connectivity!")
			chromeDriver.quit()

		rewind = replay_count
		while rewind > 0:
			try:
				play_button = chromeDriver.find_element_by_xpath("//button[@class='ytp-play-button ytp-button']")
			except:
				continue
			if play_button.get_attribute('title')=="Replay":
				play_button.click()
				rewind = rewind - 1
	chromeDriver.quit()


total_songs = int(input("How many songs? : "))
song_list = []
for i in range(total_songs):
	search_phrase = input("Enter the song no."+ str(i+1)+" : ")
	song_list.append(search_phrase)
replay_count = int(input("How long do you want to replay each song? : "))
YouTube_Rewind()