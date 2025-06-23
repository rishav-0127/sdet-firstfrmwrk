from selenium import webdriver
from selenium.webdriver.common.by import By

class Pim():
    pim_button='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    delete_button= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div[1]/div/div/div[1]/div[2]/div/div/button[2]'
    confirm_button='//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'
    def __init__(self, driver):
        self.driver = driver

    def click_pim(self):
        self.driver.find_element(By.XPATH,self.pim_button).click()

    def click_del(self):
        self.driver.find_element(By.XPATH,self.delete_button).click()

