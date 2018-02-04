from selenium import webdriver
driver = webdriver.PhantomJS()  # DO NOT FORGET to set path
driver.get("https://www.google.co.jp/") # enables to access page
print(driver.title)