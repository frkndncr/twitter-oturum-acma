import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("#######################################################")
print("                                                       ")
print("                                                       ")
print("                                                       ")
print("            BOZKURT TWİTTER OTURUM AÇMA ARAÇI          ")
print("                İnstagram: @b3zkurt                    ")
print("      Web Site: https://bozkurthub.blogspot.com/       ")
print("                                                       ")
print("                                                       ")
print("                                                       ")
print("#######################################################")
print()

username = input("Kullanıcı Adı: ")

password = input("Şifrenizi Giriniz: ")
class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def singIn(self):
         self.browser.get("https://twitter.com/login")
         time.sleep(2)

         usernameInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
         passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")

         usernameInput.send_keys(self.username)
         passwordInput.send_keys(self.password)
         passwordInput.send_keys(Keys.ENTER)
         time.sleep(2)

    def dm(self):
        dm = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div")
        dm.click()

instgrm = Instagram(username, password)
instgrm.singIn()
instgrm.dm()
