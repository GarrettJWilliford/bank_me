from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import random
import os
import getpass
import re

def driver_init(headless = True):
    if not headless:
        return webdriver.Firefox()
    fop = Options()
    fop.add_argument('--headless')
    fop.add_argument('--window_size1920x1080')
    return webdriver.Firefox(options = fop)



def login(driver):
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
        return '!'
    try:
        security = getpass.getpass(prompt = '>>SECURITY_CODE>> ')
        driver.find_element_by_id('password').send_keys(security)
        driver.find_element_by_class_name('btn-block').click()
        time.sleep(2)
    except:
        error = input('<<!SECURITY_QUESTION_FAILED!>>')
        driver.quit()
        return '!'


def display_transactions(driver):
    os.system('clear')
    remove_html = re.compile('<.*?>')
    time.sleep(5)
    p_tags = driver.find_elements_by_tag_name('span')
    p_amounts = driver.find_elements_by_class_name('trsn-payroll')
    p_tag = [p.get_attribute('innerHTML') for p in p_tags]
    p_tag = [p for p in p_tag if 'AccountNumber' not in str(p) and 'RoutingNumber' not in str(p) and \
              p.strip() not in ['Number','|', '&nbsp;$', '', 'menu', 'Hi Garrett', 'Privacy Policy', \
                                                           'User Agreement', 'Security', '2020.','Federally Insured by NCUA.', \
                                                           ' Equal Housing Lender. '] and 'or manage requests for your' not in p \
              and 'View or download monthly' not in p and 'Protect yourself from ID theft' not in p and 'More control and convenience' not in p]
    p_tag = p_tag[7::]
    print('----------------------------------------------------------------------------------------')
    for i in range(len(p_tag)):
        p = p_tag[i]
        p = re.sub(remove_html, '', p)
        p = re.sub('keyboard_arrow_down ', '', p)
        try:
            pp = p_amounts[i].get_attribute('innerHTML')
            print("{:60} : {:10}".format(p, pp))
        except:
            continue
    print('----------------------------------------------------------------------------------------')
    plcae = input('<<!PRESS_ENTER_TO_CONTINUE!>>')




def bank(driver, your_name = 'Garrett'):
    driver.get('https://www.rbfcu.org/')
    os.system('clear')
    log = login(driver)
    if log == '!':
        return
    first = True
    while True:
        if first == False:
            driver.get(url)
        if first:
            url = driver.current_url
            first = not first
        time.sleep(1)
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
            print(names[i].get_attribute('innerHTML'))
            print(accounts[i].get_attribute('innerHTML'))
            print(balance[i].get_attribute('innerHTML'))
        print('<><><><><><><><><><><><>')
        command = input('>>ENTER_COMMAND>> ')
        if command == 'CHECKING':
            names[0].click()
            display_transactions(driver)
        if command == 'SAVINGS':
            names[1].click()
            display_transactions(driver)
        if command == 'QUIT':
            break
        if command == '!DEV_RETURN_DRIVER':
            return driver
    driver.quit()
    return

    
    








