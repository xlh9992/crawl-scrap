from selenium import webdriver
browser = webdriver.PhantomJS()

loginUrl= "https://www.hatena.ne.jp/login"
browser.get(loginUrl)

username = "xlh9992"
password = "flat5081"

userNameField = browser.find_element_by_xpath("//*[@id='login-name']")
userNameField.send_keys(username)

passwordField = browser.find_element_by_xpath("//*[@id='container']/div/form/div/div[2]/div/input")
passwordField.send_keys(password)

submitButton = browser.find_element_by_class_name("submit-button")
submitButton.click()

profile = "profile.hatena.ne.jp"
browser.get(profile)

browser.title