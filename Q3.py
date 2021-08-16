from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

''' def get_captcha()    defining get_captcha
   .........'''
driver = webdriver.Chrome("D:\\chromedriver")
driver.get('https://parivahan.gov.in/rcdlstatus/?pur_cd=101')
d = driver.find_element_by_id("form_rcdl:tf_dlNO")
d.send_keys('DL-0420110149646')
do = driver.find_elements_by_id("form_rcdl:tf_dob_input")
dob = do[0]
dob.send_keys('09-02-1976')
dob.send_keys(Keys.ENTER)
#get_captcha()    calling of function get_captcha

status = driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt43"]/span')
status.click()

time.sleep(25)  #this sleep function to be removed when get_captcha function is added



for link in driver.find_elements_by_css_selector("#form_rcdl\:j_idt124"):
    print(link.text)