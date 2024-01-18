from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class WhatsAppAutomation:
    def __init__(self):
        self.driver = webdriver.Chrome()  # You need to have ChromeDriver installed and in your PATH
        self.driver.get("https://web.whatsapp.com")
        input("Scan the QR code on the browser, then press Enter.")

    def send_message(self, contact_name, message):
        search_box = self.driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
        search_box.clear()
        search_box.send_keys(contact_name)
        time.sleep(2)  # Wait for the contact list to load
        search_box.send_keys(Keys.ENTER)

        message_box = self.driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="6"]')
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    wa_bot = WhatsAppAutomation()

    contact_name = input("Enter the contact name: ")
    message = input("Enter the message: ")

    wa_bot.send_message(contact_name, message)

    wa_bot.close()
