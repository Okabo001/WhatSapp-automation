from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")

input("Scan the QR code and press Enter to continue...")

search_box = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
search_box.send_keys("Jontee")
search_box.send_keys(Keys.RETURN)

message_box = driver.find_element_by_xpath('//div[@class="_3uMse"]')
message_box.send_keys("lets try automation using Python!")
message_box.send_keys(Keys.RETURN)
driver.quit()
