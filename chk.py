#!/usr/bin/python2
# coding=utf-8

import os
import sys
import time
import datetime
import re
import threading
import json
import random
import requests
import hashlib
import cookielib
import uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
__author__ = 'Rana-MZ'
__copyright = 'All rights reserved . Copyright  Rana-MZ'
os.system('termux-setup-storage')

try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)

header = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
os.system('git pull')
os.system('clear')


#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#Dev:Rana-MZ
#### LOGO ####
logo = """  
\033[1;32m########     ###    ##    ##    ###       ##     ## ######## 
\033[1;31m##     ##   ## ##   ###   ##   ## ##      ###   ###      ##  
\033[1;33m##     ##  ##   ##  ####  ##  ##   ##     #### ####     ##   
\033[1;37m########  ##     ## ## ## ## ##     ##    ## ### ##    ##    
\033[1;33m##   ##   ######### ##  #### #########    ##     ##   ##     
\033[1;31m##    ##  ##     ## ##   ### ##     ##    ##     ##  ##      
\033[1;32m##     ## ##     ## ##    ## ##     ##    ##     ## ######## 
                      {NAM TU SUNA HUGA}
                                 
\033[1;37m    ||||||||||||||||||||| 
\033[1;32m    Author iZ : Rana MZ
\033[1;32m    Facebook : Rana MZ
\033[1;32m    Youtube   : Rana MZ
\033[1;32m    Author2 iZ : Sunny              
\033[1;37m    |||||||||||||||||||||
\033[1;31m        =====
\033[1;31m        NOtE :
\033[1;31m        =====
 \033[1;32m      ==================
\033[1;33m       DONt TRY TO COPY ME
\033[1;33m       BECz itz iMPOSSiBLE
\033[1;32m       ==================
"""

def reg():
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1m Welcom-----!'
    print ''
    time.sleep(1)
    
    try:
        to = open('/sdcard/.zee.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/RANAMZ-zeshi/mz-0ld/main/mz.txt').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(2)
        ip()
    else:
        os.system('clear')
        print logo
        print '\tApproved Failed'
        print ' \033[1;92m Sory Id Is Not Approved Already '
        print ' \033[1;92m NotE : '
        print ' \033[1;92m  USE VPN FOR APRVAL '
        print ' \033[1;92m  AFTER APRVAL DONE U CAN DC VPN '
        print ' \033[1;92m Copy the id and send me'
        print ' \033[1;92m Your id: ' + to
        raw_input('\033[1;93m Press ener to send id')
        os.system('xdg-open https://wa.me/+923414547149')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\tApproval not OK TRY AGAIN'
    print ' \033[1;92m Copy kr k send kro Whatsapp py to continue'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' Press enter to go to MY Page ')
    os.system('xdg-open https://wa.me/+923414547149')
    sav = open('/sdcard/.zee.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\033[1;92m Press enter to check Approval ')
    reg()


def ip():
    os.system('clear')
    print logo
    print '\tCollecting info w8!'
    
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\033[1;92m Your ip: ' + ips
    time.sleep(2)
    print '\033[1;92m Your country: ' + country
    time.sleep(2)
    print '\033[1;92m Your region: ' + regi
    time.sleep(2)
    print ' \033[1;92mYour network: ' + network
    time.sleep(2)
    print ' Loading ...'
    time.sleep(2)
    log_menu()
	

def log_menu():
    
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\033[1;90m Login menu\033[1;94m'
	print 47 * '-'
        print '\033[1;92m[1]  with FaceBook'
        print '\033[1;92m[2]  with token'
        print '\033[1;92m[3]  Contct with Owner'
        print ''
        log_menu_s()



def log_menu_s():
    s = raw_input(' \033[1;97m╰─Rana-MZ➤ ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        os.system('xdg-open https://facebook.com/quyyam.jafar/')
    else:
        print ''
        print '\\ Select valid option '
        print ''
        log_menu_s()


def log_fb():
    os.system('clear')
    print logo
    print '\033[1;31;1mLogin with id/pass'
    print 47 * '-'
    lid = raw_input('\033[1;92m Id/mail/no: ')
    pwds = raw_input(' \033[1;93mPassword: ')
    
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ' User must verify account before login'
            raw_input('\033[1;92m Press enter to try again ')
            log_fb()
        else:
            print ' Id/Pass may be wrong'
            raw_input(' \033[1;92mPress enter to try again ')
            log_fb()
    except:
        print ''
        print 'Exiting tool'
        os.system('exit')



def log_token():
    os.system('clear')
    print logo
    print '\033[1;93mLogin with token\033[1;91m'
    print 47 * '-'
    tok = raw_input(' \033[1;92mPaste token here: \033[1;91m')
    print 47 * '-'
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()


def menu():
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print '\033[1;31;1mLogin FB id to continue'
        time.sleep(1)
        log_menu()

    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t Account Cheekpoint\x1b[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t Turn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \033[1;92mPress enter after turning on mobile data/wifi ')
        menu()

    os.system('clear')
    print logo
    tok = open('/sdcard/.zee.txt', 'r').read()
    print '  \033[1;92mLogged in user: \033[1;94m' + z
    print 47 * '-'
    print ' \033[1;90m Active token : \033[1;94m' + tok
    print ' ------------------------------------------ '
    print '\033[1;92m[1] Start Cloning' 
    print '\033[1;92m[2] Follow OWNER'
    print '\033[1;92m[3] View token'
    print '\033[1;92m[4] Logout'
    print '\033[1;92m[5] Delete trash files'
    menu_s()


def menu_s():
    ms = raw_input('\033[1;97m╰─RANA-MZ➤ ')
    if ms == '1':
        os.system('python2 chk.py')
        menu_s()
    elif ms == '2':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100054325534287') 
    elif ms == '3':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100054325534287') 
    elif ms == '4':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100054325534287') 
    elif ms == '5':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100054325534287') 
        
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_s()
	


if __name__ == '__main__':
    reg()
