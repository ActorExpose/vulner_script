# Admin Page Auto Check Program
# Dev Date : 19.04.24
# Developer : Zeromini
# Version 2.0.1

from selenium import webdriver
import os
import time
import sys

def auto_screen_shot_80():
    browser = webdriver.Chrome('/chromedriver.exe')
    #brower.set_page_load_timelout(15)
    r = open('/list_80.txt', mode='rt')
    for line in r:
        print('======= Starting Admin Checking ======')
        print(str(line)+' Read and Checking...........')
        browser.get('http://'+line)
        file_url = str(line)
        #time.sleep(2)
        browser.save_screenshot('/list_80/initial.png')
        #time.sleep(2)
        os.rename('/list_80/initial.png','/list_80/'+(file_url.replace('\n',''))+'_80.png')
    browser.quit()
    r.close()

def auto_screen_shot_443():
    browser = webdriver.Chrome('/chromedriver.exe')
    r = open('/list_443.txt', mode='rt')
    for line in r:
        print('======= Starting Admin Checking ======')
        print(str(line)+' Read and Checking(https)....')
        browser.get('https://'+line)
        file_url = str(line)
        overrideLink = browser.find_element_by_id('overridelink')
        #time.sleep(2)
        overrideLink.click()
        #time.sleep(2)
        browser.save_screenshot('/list_443/initial.png')
        #time.sleep(2)
        os.rename('/list_443/initial.png','/list_443/'+(file_url.replace('\n',''))+'_443.png')
    browser.quit()
    r.close()


def make_directroy():
    if not os.path.exists('/list_80'):
        os.mkdir('/list_80')
    if not os.path.exists('/list_443'):    
        os.mkdir('/list_443')


print('#####################################') 
print('### Admin Page Auto Check Program ###') 
print('### Dev By : Zeromini / Ver 2.0.1 ###') 
print('#####################################') 

print('-------------------------------------')
print(' PLZ MAKE TXT file In C:// ')
print('   Ex: list_80.txt / list_443.txt    ')
print('-------------------------------------')
print('  Do u wanna Start this Program ??   ')
print(' <<<< If u want press "Y" >>>> ')
print(' <<<< If u dont want press "ANY KEY" >>>> ')
print('-------------------------------------')

check = str(raw_input('>>'))

if check == 'Y':
    print(' Starting This Program .......')
    make_directroy()
    #auto_screen_shot_80()
    print(' Finish Admin Checking(HTTP).....')
    auto_screen_shot_443()
    print(' Finish Admin Checking(HTTPS).....')


else:
    print(' Exit This Program')
    sys.exit()


