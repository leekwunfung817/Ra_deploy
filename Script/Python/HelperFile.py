
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import Version
chrome_options = Options()
chrome_options.add_argument("--window-size=5,5")
def nextLine2sinLine(txt):
	for x in range(1,10):
		txt = txt.replace("\n\n\n", "\n\n")
	return txt

def Request(url):
	driver = Version.driver
	binary_path='./'+driver
	print('Use driver:',binary_path)
	print(url)
	try:
		driver = webdriver.Chrome(executable_path=binary_path,chrome_options=chrome_options)
		driver.get(url)
		print('Point 3')
		time.sleep(8)
		print('Point 4')
		txt=driver.page_source
		driver.close()
		return txt
	except Exception as e:
		print(e)
	exit()
	# return None

def saveUTF8File(filename,txt):
	if txt is None:
		print('Write None to ',filename,' fail')
		return
		pass
	f = open(filename, "wb")
	f.write(txt.encode("utf-8"))
	f.close()

def readUTF8File(filename):
	return open(filename,"rb").read().decode("utf-8")

import os, shutil

def DelteAllFilesInFolder(folder):
	for filename in os.listdir(folder):
		file_path = os.path.join(folder, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			print('Failed to delete %s. Reason: %s' % (file_path, e))