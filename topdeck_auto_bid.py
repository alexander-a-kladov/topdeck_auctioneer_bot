# This is a sample Python script.

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

topdeck_auctions_root = "https://topdeck.ru/apps/toptrade/auctions/"
topdeck_login = "https://topdeck.ru/login"
auction = ""


class TopdeckBid(object):
    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get(topdeck_login)
        username_edit = self.driver.find_element(By.XPATH, "//input[@type='email']")
        username_edit.send_keys("")
        sleep(1)
        password_edit = self.driver.find_element(By.XPATH, "//input[@type='password']")
        password_edit.send_keys("")
        sleep(1)
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

    def bid(self, max_bid):
        self.driver.get(topdeck_auctions_root + auction)
        current_price = self.driver.find_element(By.XPATH, "//span[@class='label label-default']")
        if not len(current_price.text):
            current_price = self.driver.find_element(By.XPATH, "//span[@class='label label-success']")
        if not len(current_price.text):
            return
        price = current_price.text
        print(price)

        if int(price) > int(max_bid):
            return

        price_field = self.driver.find_element(By.NAME, "bid")
        price_field.send_keys(max_bid)
        sleep(1)

        bid_button = self.driver.find_element(By.XPATH, "//button[@data-toggle='confirmation']")
        print(bid_button.text)
        bid_button.click()
        sleep(5)

        actions = ActionChains(self.driver)
        actions.move_by_offset(1050, 400).click().perform()
        sleep(3)
        price = current_price.text
        print(price)


if __name__ == "__main__":
    topdeck_bid = TopdeckBid()
    topdeck_bid.login()
    topdeck_bid.bid("815")
