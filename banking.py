from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import random
import os
import getpass

def driver_init(headless = True):
    if not headless:
        return webdriver.Firefox()
    fop = Options()
    fop.add_argument('--headless')
    fop.add_argument('--window_size1920x1080')
    return webdriver.Firefox(options = fop)


def rbfcu(driver, your_name):
    driver.get('https://www.rbfcu.org/')
    os.system('clear')
    print('<<<<<<<<<<|LOGIN|>>>>>>>>>>')
    user = getpass.getpass(prompt = '>>ENTER_USER>> ')
    password = getpass.getpass(prompt = '>>ENTER_PASSWORD>> ')
    try:
        driver.find_element_by_id('username').send_keys(user)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_class_name('btn').click()
        time.sleep(2)
        driver.find_element_by_id('password')
    except:
        error = input('<<!LOGIN_FAILED!>>')
        driver.quit()
        return
    try:
        security = getpass.getpass(prompt = '>>SECURITY_CODE>> ')
        driver.find_element_by_id('password').send_keys(security)
        driver.find_element_by_class_name('btn-block').click()
        time.sleep(2)
    except:
        error = input('<<!SECURITY_QUESTION_FAILED!>>')
        driver.quit()
        return
    elements = driver.find_elements_by_class_name('float-left')
    e = [e for e in elements if your_name in e.get_attribute('innerHTML')]
    while True:
        names = driver.find_elements_by_css_selector('span.f5.rb-semi-black.fw5.fs-block')
        accounts = driver.find_elements_by_css_selector('span.f5.rb-semi-black.fw3.pl2.left-acnt-space.fs-block')
        balance = driver.find_elements_by_css_selector('span.f3.rb-subnav-blue.fw3')
        titles = driver.find_elements_by_tag_name('h5')
        os.system('clear')
        print('<><><><><><><><><><><><>')
        first = True
        for i in range(len(accounts)):
            if not first:
                print('-----------------------------')
            if first:
                first = not first
            print('ACCOUNT ' + str(i))
            print(names[i].get_attribute('innerHTML'))
            print(accounts[i].get_attribute('innerHTML'))
            print(balance[i].get_attribute('innerHTML'))
        print('<><><><><><><><><><><><>')
        command = input('>>ENTER_COMMAND>> ')
        if command == 'CHECKING':
            os.system('clear')
            names[0].click()
            time.sleep(3)
            p_tags = driver.find_elements_by_tag_name('mat-panel-title')
            p_amounts = driver.find_elements_by_class_name('trsn-payroll')
            for i in range(len(p_tags)):
                p = p_tags[i].get_attribute('innerHTML')
                pp = p_amounts[i].get_attribute('innerHTML')
                print("{:60} : {:10}".format(p[p.index('/mat-icon') + 11::], pp))
            plcae = input('<<>>')
        if command == 'C':
            continue
        if command == 'S':
            continue
        if command == 'Q':
            break
        if command == '!DEV_RETURN_DRIVER':
            return driver
    driver.quit()
    return
        
    


