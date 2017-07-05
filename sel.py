from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.target.com/p/nintendo-switch-with-gray-joy-con/-/A-52052007')
print browser.page_source
