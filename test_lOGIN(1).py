# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLOGIN():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tESTCASE1(self):
    self.driver.get("http://blackrockdigital.github.io/startbootstrap-sb-admin/dist/login.html")
    self.driver.set_window_size(892, 728)
    self.driver.find_element(By.ID, "inputEmailAddress").click()
    self.driver.find_element(By.ID, "inputEmailAddress").send_keys("diego@prueba.com")
    self.driver.find_element(By.ID, "inputPassword").click()
    self.driver.find_element(By.ID, "inputPassword").send_keys("0000")
    self.driver.find_element(By.CSS_SELECTOR, ".custom-control-label").click()
    self.driver.find_element(By.LINK_TEXT, "Login").click()
  
