from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

def test_add_zero_tickets():
    driver=webdriver.Chrome()
    
    driver.get(str("file:///C:/Users/CobzaruCosmina/ticketing_project/ticketing_website.html"))
    
    time.sleep(2)
    
    tickets=driver.find_element(By.ID, "tickets")
    
    tickets.send_keys("0")
    
    button=driver.find_element(By.ID, "add")
    button.click()
    
    time.sleep(2)
    
    message=driver.find_element(By.ID, "message")
    assert "please enter" in message.text.lower()
    
    
    
    time.sleep(3)
    
def test_add_two_tickets():
    driver=webdriver.Chrome()
    
    driver.get(str("file:///C:/Users/CobzaruCosmina/ticketing_project/ticketing_website.html"))
    
    time.sleep(2)
    
    tickets=driver.find_element(By.ID, "tickets")
    
    tickets.send_keys("2")
    
    button=driver.find_element(By.ID, "add")
    button.click()
    
    time.sleep(2)
    
    
    message=driver.find_element(By.ID, "message")
    assert "added to cart" in message.text.lower()
    
    time.sleep(3)
    
    
def test_empty_tickets():
     driver=webdriver.Chrome()
    
     driver.get(str("file:///C:/Users/CobzaruCosmina/ticketing_project/ticketing_website.html"))
     time.sleep(2)
     
     tickets=driver.find_element(By.ID, "tickets")
     
    #simulate user not entering any ticket
     
     button=driver.find_element(By.ID, "add")
     button.click()
     
     time.sleep(2)
     
     message=driver.find_element(By.ID, "message")
     assert "please enter" in message.text.lower()
     
     time.sleep(3)
     driver.quit()
    
  