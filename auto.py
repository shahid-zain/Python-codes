from selenium import webdriver

driver=webdriver.Chrome()

driver.get('https://www.youtube.com')

n=input("enter what you want to search : ")

search=driver.find_element_by_xpath('//*[@id="search"]') #find search box

searchpath=search.send_keys(n) #enter the key

searchbutton=driver.find_element_by_xpath('//*[@id="search-icon-legacy"]') # point on search button

searchbutton.click()

