import time;
from selenium import webdriver;

#time to refresh page (sec)
Timer = 60

#youtube URL, dont remove the ' parts.
link = 'VideoLinkHere'

#number of views, type number of views u want below. :)
views = 1000

driver = webdriver.Chrome()
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
    print(i)
