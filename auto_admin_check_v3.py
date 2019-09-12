# Admin Page Auto Check Program
# Dev Date : 19.09.13
# Developer : Zeromini
# Version 3.0.1

from selenium import webdriver
import os
import time
import sys

# function section

def main_display():
    print('#########################################################################') 
    print('### Admin Page Auto Check Program #######################################') 
    print('### Dev By : Zeromini / Ver 3.0.1 #######################################') 
    print('#########################################################################') 

    print('                      /^--^\     /^--^\     /^--^\                       ')
    print('                      \____/     \____/     \____/                       ')
    print('                     /      \   /      \   /      \                      ')
    print('                    |        | |        | |        |                     ')
    print('                     \__  __/   \__  __/   \__  __/                      ')
    print('|^|^|^|^|^|^|^|^|^|^|^|^\ \^|^|^|^/ /^|^|^|^|^\ \^|^|^|^|^|^|^|^|^|^|^|^|')
    print('| | | | | | | | | | | | |\ \| | |/ /| | | | | | \ \ | | | | | | | | | | |') 
    print('| | | | | | | | | | | | / / | | |\ \| | | | | |/ /| | | | | | | | | | | |')
    print('| | | | | | | | | | | | \/| | | | \/| | | | | |\/ | | | | | | | | | | | |')
    print('#########################################################################')
    print('| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |')
    print('| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |')
    print('-------------------------------------------------------------------------')
    print('-------------------------------------------------------------------------')
    print('  Do u wanna Start this Program ??   ')
    print(' <<<< If u want press "Y" >>>> ')
    print(' <<<< If u dont want press "ANY KEY" >>>> ')
    print('-------------------------------------')

def auto_screen_shot(port_check,directory,read_ip_file):
    browser = webdriver.Chrome('chromedriver.exe')
    #brower.set_page_load_timelout(15)
    r = open(read_ip_file, mode='rt')
    for line in r:
        print('======= Starting Admin Checking ======')
        print(str(line)+' Read and Checking...........')
        browser.get('http://'+line+':'+port_check)
        file_url = str(line)
        #print(file_url)
        browser.save_screenshot(directory+'/initial.png')
        os.rename(directory+'/initial.png',directory+'/'+(file_url.replace('\n',''))+'.png')
    browser.quit()
    r.close()
    

def auto_screen_shot_443(port_check,directory,read_ip_file):
    browser = webdriver.Chrome('/chromedriver.exe')
    r = open(read_ip_file, mode='rt')
    for line in r:
        print('======= Starting Admin Checking ======')
        print(str(line)+' Read and Checking(https)....')
        browser.get('https://'+line)
        file_url = str(line)
        overrideLink = browser.find_element_by_id('overridelink')
        overrideLink.click()
        browser.save_screenshot(directory+'/initial.png')
        os.rename(directory+'/initial.png',directory+'/'+(file_url.replace('\n',''))+'.png')
    browser.quit()
    r.close()


def make_directroy(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


## Starting Section 

main_display()

check = str(raw_input('>>'))

if check == 'Y':
    while(1):
        print('Starting This Program .......')
        print('PLZ input port for checking admin page..!! ')
        port_check = str(raw_input('>>'))
        print('PLZ input Read ip file Directory')
        print(' EX) C:/ip_list.txt')
        read_ip_file = str(raw_input('>>'))
        print('PLZ input you want to save direcory ..!!')
        print(' EX) C:/screen_shot')
        directory = str(raw_input('>>'))
        print(' IS IT CORRECT ...? (Y/N)')
        print('SCAN PORT : '+port_check)
        print('Directory : '+directory)
        print('READ_IP_FILE Directory :'+read_ip_file)
        flag = str(raw_input('>>'))
        if flag == 'Y':
            if port_check == '443':
                print('Chekcing Port : '+ port_check)
                make_directroy(directory)
                auto_screen_shot_443(port_check,directory,read_ip_file)
                print('Finish Admin Check :'+ port_check)
                break
            else: 
                print('Chekcing Port : '+ port_check)
                make_directroy(directory)
                auto_screen_shot(port_check,directory,read_ip_file)
                print('Finish Admin Check :'+ port_check)
                break
        else:
            print('Oops..! U hav mistake..!')


else:
    print('Exit This Program')
    sys.exit()
