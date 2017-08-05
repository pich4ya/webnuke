import time
import thread
from libs.utils.WebDriverUtil import *

paused = False

class FollowmeCommands:
	def __init__(self, webdriver, debug, proxy_host, proxy_port, logger):
		self.version = 0.1
		self.driver = webdriver
		self.debug = debug
		self.proxy_host = proxy_host
		self.proxy_port = proxy_port
		self.logger = logger
	
	def start_new_instance(self):
		browser = self.create_browser_instance()
		newthread = thread.start_new_thread(self.linkbrowsers, (self.driver, browser))
		
	def pause_all(self):
		global paused
		paused = True

	def resume_all(self):
		global paused
		paused = False
		
	def get_paused(self):
		return paused

	def create_browser_instance(self):
		self.webdriver_util = WebDriverUtil()
		self.webdriver_util.setDebug(self.debug)
		if self.proxy_host is not '' and int(self.proxy_port) is not 0:
			return self.webdriver_util.getDriverWithProxySupport(self.proxy_host, int(self.proxy_port))
		else:
			return self.webdriver_util.getDriver(self.logger)	

	def linkbrowsers(self, maindriver, followmedriver):
		global paused
		while(True):
			if(paused == False):
				try:
					main_url = maindriver.current_url
					if followmedriver.current_url != main_url:
						followmedriver.get(main_url)
				except:
					pass
				finally:
					time.sleep(0.5)
