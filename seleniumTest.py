from selenium import webdriver
user_agent = 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36'
pjs_path = 'node_modules/phantomjs/bin/phantomjs'
dcap = {
    "phantomjs.page.settings.userAgent" : user_agent,
    'marionette' : True
}
browser = webdriver.PhantomJS(executable_path=pjs_path, desired_capabilities=dcap)  # DO NOT FORGET to set path
browser.get("https://www.google.co.jp/") # enables to access page
print(browser.title)