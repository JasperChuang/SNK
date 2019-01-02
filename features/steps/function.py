from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def on_the_login_page():
    global driver
    driver = webdriver.Chrome()  # browser using chrome
    driver.get('http://www.alpha.snklab.com/')  # open SNK frontend website
    #driver.maximize_window()  # maximize the browser
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, '__next')), 'Can\'t load the login page.')     # Waiting for the page to load
    assert driver.current_url == 'http://www.alpha.snklab.com/', 'Can\'t open the login page.'


def display_the_element(element):
    if element == 'SNK favicon':
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'link[rel=\'shortcut icon\']'))), 'SNK favicon not found.'
        
    elif element == 'BRAND layout':
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#__next div:nth-of-type(2) div:nth-of-type(1)')))\
            , 'BRAND layout not found.'
        
    elif element == 'LOGIN layout':
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#__next div:nth-of-type(2) form:nth-of-type(1)')))\
            , 'LOGIN layout not found.'
        
    elif element == 'CONTACT layout':
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#__next div:nth-of-type(2) div:nth-of-type(2)')))\
            , 'CONTACT layout not found.'
        
    elif element == 'END layout':
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#__next div:nth-of-type(2) div:nth-of-type(3)')))\
            , 'END layout not found.'
        
    elif element == 'SNK logo':
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#__next div:nth-of-type(2) div:nth-of-type(1) img[src][class]')))\
            , 'SNK logo not found.'
        
    elif element == 'MEMBER label':
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#__next div:nth-of-type(2) form:nth-of-type(1) span[class]')))\
            , 'MEMBER label not found.'
        
    elif element == 'MESSAGE label':
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#__next div:nth-of-type(2) form:nth-of-type(1) div[class]')))\
            , 'MESSAGE label not found.'
        
    elif element == 'USERNAME label':
        assert WebDriverWait(driver, 10)\
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#__next div:nth-of-type(2) form:nth-of-type(1) label:nth-of-type(1) span')))\
            , 'USERNAME label not found.'
        
    elif element == 'USERNAME inputbox':
        assert WebDriverWait(driver, 10)\
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#__next div:nth-of-type(2) form label:nth-of-type(1) input[placeholder]')))\
            , 'USERNAME inputbox not found.'
        
    elif element == 'PASSWORD label':
        assert WebDriverWait(driver, 10)\
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#__next div:nth-of-type(2) form:nth-of-type(1) label:nth-of-type(2) span')))\
            , 'PASSWORD label not found.'
        
    elif element == 'PASSWORD inputbox':
        assert WebDriverWait(driver, 10)\
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#__next div:nth-of-type(2) form label:nth-of-type(2) input[placeholder]')))\
            , 'PASSWORD inputbox not found.'
        
    elif element == 'LOGIN button':
        assert WebDriverWait(driver, 10)\
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#__next div:nth-of-type(2) form:nth-of-type(1) button[type=\'submit\']')))\
            , 'LOGIN button not found.'
        
    elif element == 'EMAIL icon':
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div#__next div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(1) div:nth-of-type(1) div:nth-of-type(1) img[src]')))\
            , 'EMAIL icon not found.'
        
    elif element == 'EMAIL textlink':
        assert WebDriverWait(driver, 10)\
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#__next div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(1) a[href]')))\
            , 'EMAIL textlink not found.'
        
    elif element == 'CALL icon':
        assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div#__next > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > img[src]')))\
            , 'CALL icon not found.'
        
    elif element == 'CALL textlink':
        assert WebDriverWait(driver, 10)\
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#__next div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(2) a[href]')))\
            , 'CALL textlink not found.'


def the_element_is_displayed_correctly(element):
    if element == 'Website title': assert driver.title == 'SNK', 'Website title is incorrect.'
    
    elif element == 'SNK favicon':
        assert driver.find_element_by_css_selector('link[rel=\'shortcut icon\']')\
                   .get_attribute('href') == 'http://static.alpha.snklab.com/static/snk/favicon.ico', 'SNK favicon is incorrect.'
        
    elif element == 'SNK logo':
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) div:nth-of-type(1) img[src][class]')\
                   .get_attribute('src') == 'http://static.alpha.snklab.com/static/snk/logo/logo.png', 'SNK logo is incorrect.'
        
    elif element == 'MEMBER label':
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form:nth-of-type(1) span[class]').text == 'MEMBER', 'MEMBER label is incorrect.'
        
    elif element == 'MESSAGE label':
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form:nth-of-type(1) div[class]').text == 'Welcome Back!', 'MESSAGE label is incorrect.'
        
    elif element == 'USERNAME label':
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form:nth-of-type(1) label:nth-of-type(1) span')\
                   .text == 'USERNAME', 'USERNAME label is incorrect.'
        
    elif element == 'USERNAME inputbox':
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form label:nth-of-type(1) input[placeholder]')\
                   .get_attribute('placeholder') == 'enter username', 'USERNAME inputbox is incorrect.'
        
    elif element == 'PASSWORD label':
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form:nth-of-type(1) label:nth-of-type(2) span')\
                   .text == 'PASSWORD', 'PASSWORD label is incorrect.'
        
    elif element == 'PASSWORD inputbox':
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form label:nth-of-type(2) input[placeholder]')\
                   .get_attribute('placeholder') == 'enter password', 'PASSWORD inputbox is incorrect.'
        
    elif element == 'LOGIN button':
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form:nth-of-type(1) button[type=\'submit\']')\
                   .text == 'LOGIN', 'LOGIN button is incorrect.'
        
    elif element == 'EMAIL icon':
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(1) div:nth-of-type(1) div:nth-of-type(1) img[src]')\
                   .get_attribute('src') == 'http://static.alpha.snklab.com/static/snk/icon/png/mail-white.png', 'EMAIL icon is incorrect.'
        
    elif element == 'EMAIL textlink':
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(1) a[href]')\
                   .get_attribute('href') == 'mailto://matasales@protonmail.com', 'EMAIL link is incorrect.'
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(1) a[href]')\
                   .text == 'matasales@protonmail.com', 'EMAIL address is displayed incorrectly.'
        
    elif element == 'CALL icon':
        assert driver.find_element_by_css_selector\
                   ('div#__next > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > img[src]')\
                   .get_attribute('src') == 'http://static.alpha.snklab.com/static/snk/icon/png/phone-white.png', 'CALL icon is incorrect.'
        
    elif element == 'CALL textlink':
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(2) a[href]')\
                   .get_attribute('href') == 'tel://+44 7506 829565', 'CALL number link is incorrect.'
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) div:nth-of-type(2) div:nth-of-type(2) a[href]')\
                   .text == '+44 7506 829565', 'CALL number is displayed incorrectly.'


def after_loading_the_login_page():
    global driver
    driver = webdriver.Chrome()  # browser using chrome
    driver.get('http://www.alpha.snklab.com/')  # open SNK frontend website
    driver.maximize_window()  # maximize the browser
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, '__next')), 'Can\'t load the login page.')     # Waiting for the page to load
    assert driver.current_url == 'http://www.alpha.snklab.com/', 'Can\'t open the login page.'


def cursor_is_focusing_on_username_textbox():
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form:nth-of-type(1) div[class]').text != 'Welcome Back!'\
        , 'text is \'' + driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form:nth-of-type(1) div[class]').text + '\''
    
    
def typing_12345678901234567890_into_element_textbox(element):
    try:
        if element == 'USERNAME':       # typing 20 words into USERNAME textbox
            driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form label:nth-of-type(1) input[placeholder]').send_keys('12345678901234567890')
        elif element == 'PASSWORD':     # typing 20 words into USERNAME textbox
            driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form label:nth-of-type(2) input[placeholder]').send_keys('12345678901234567890')
    except: print('Can\'t typing words.')   # error message


def can_type_12345678901234567890_into_element_textbox(element):
    if element == 'USERNAME':
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form label:nth-of-type(1) input[placeholder]')\
                   .get_attribute('value') == '12345678901234567890', 'Can\'t type all text.'
    elif element == 'PASSWORD':
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form label:nth-of-type(2) input[placeholder]')\
                   .get_attribute('value') == '12345678901234567890', 'Can\'t type all text.'
        
        
def typing_123456789012345678901_into_element_textbox(element):
    try:
        if element == 'USERNAME':       # typing 20 words into USERNAME textbox
            driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form label:nth-of-type(1) input[placeholder]').send_keys('123456789012345678901')
        elif element == 'PASSWORD':     # typing 20 words into USERNAME textbox
            driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form label:nth-of-type(2) input[placeholder]').send_keys('123456789012345678901')
    except: print('Can\'t typing words.')   # error message
    

def can_only_type_12345678901234567890_into_element_textbox(element):
    if element == 'USERNAME':
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form label:nth-of-type(1) input[placeholder]')\
                   .get_attribute('value') == '12345678901234567890', 'USERNAME textbox input characters count is mismatched to spec.'
    elif element == 'PASSWORD':
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form label:nth-of-type(2) input[placeholder]')\
                   .get_attribute('value') == '12345678901234567890', 'PASSWORD textbox input characters count is mismatched to spec.'


def cursor_is_focused_on_element(element):
    try:
        if element == 'USERNAME textbox':
            driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form:nth-of-type(1) label:nth-of-type(1) input[placeholder]').click()
        elif element == 'PASSWORD textbox':
            driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form:nth-of-type(1) label:nth-of-type(2) input[placeholder]').click()
        elif element == 'LOGIN button':
            driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form button[type]').click()
    except: print('Can\'t focusing element.')   # error message

        
def press_the_Tab_key_on_the_keyboard():
    ActionChains(driver).send_keys(Keys.TAB).perform()
    
def move_the_focused_elements_to_next(next):
    if next == 'PASSWORD textbox':
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form:nth-of-type(1) label:nth-of-type(2) input[placeholder]')\
                   .get_attribute('placeholder') == 'enter password', 'Element is incorrect'
    
    elif next == 'LOGIN button':
        assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form button[type]')\
                   .get_attribute('type') == 'submit', 'Element is incorrect'
                
def pressed_the_Enter_key_on_the_keyboard():
    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    
def performing_login():
    assert driver.find_element_by_css_selector('div#__next div:nth-of-type(2) form div').text == 'Logging in...', 'on LOGIN button key Enter error'
    
