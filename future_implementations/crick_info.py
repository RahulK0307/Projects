# This file will show the pop up box that will show information regarding your time of work
# time to leave and the lunch time reminder for you to go for the lunch in office. This will work
# and pop up the reminders for each and everything on the users screen.

import os
import time
import urllib2
from bs4 import BeautifulSoup
import bs4


url = "http://timesofindia.indiatimes.com/"
res = urllib2.urlopen(url)
print res.info()
