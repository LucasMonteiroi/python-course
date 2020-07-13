from selenium import webdriver
browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
browser.get('https://dolarhoje.com/')
elem = browser.find_element_by_css_selector('#nacional')
print(elem)