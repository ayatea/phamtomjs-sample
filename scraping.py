from selenium import webdriver

driver_path = '/usr/local/bin/phantomjs'

# PhamtomJS Driverを起動する
driver = webdriver.PhantomJS(executable_path = driver_path)

driver.get('https://www.yahoo.co.jp/') 

data = driver.page_source.encode('utf-8')

print(data)

# PhamtomJS Driverを終了する
driver.quit()
