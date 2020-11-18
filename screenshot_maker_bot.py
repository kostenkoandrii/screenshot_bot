from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import time

def make_screenshot(url):
	"""
	Method witch take screenshot of website
	:param url: url of website
	:return: screenshot in png format
	"""
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument("--disable-notifications")
	driver = webdriver.Chrome(chrome_options=chrome_options)
	try:
		driver.get(url)
		time.sleep(1)
	except WebDriverException:
		return False

	size = driver.find_element_by_tag_name('body').size
	driver.set_window_size(1920, size.get('height'))
	size = driver.find_element_by_tag_name('body').size

	driver.set_window_size(size.get('width'), size.get('height'))
	screenshot = driver.get_screenshot_as_png()
	driver.quit()
	return screenshot
