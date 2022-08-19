from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import os 
import wget

browser = webdriver.Chrome("./chromedriver")

browser.get("https://instagram.com")