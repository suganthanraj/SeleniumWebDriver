from selenium import webdriver

#initializing the webdriver with the relative path
driver = webdriver.Chrome("drivers/chromedriver.exe")

# implicitly wait for 10 seconds
driver.implicitly_wait(10)

# maximize the chrome window
driver.maximize_window()

# getting the web url to open
driver.get("https://google.com")

# finding the element by name and sending key value in order to search content 
# in the google page
driver.find_element_by_name("q").send_keys("suganthan raj")

# clicking the search button in the google search page
driver.find_element_by_name("btnK").click()



