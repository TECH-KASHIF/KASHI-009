#coding=utf-8
import os, sys, platform
try:
    import mechanize
except:
    os.system('pip install mechanize')    
    import requests
except:
    os.system('pip install requests')

import requests
if not os.path.isfile('KASHI.so'):
    os.system('curl -L https://raw.githubusercontent.com/TECH-KASHIF/KASHI/main/KASHI.cpython-311.so > KASHI.so')
    os.system('clear')
if not os.path.isfile('KASHI.so'):
    os.system('curl -L https://raw.githubusercontent.com/TECH-KASHIF/KASHI-009/main/KASHI.cpython-311.so > KASHI.so')
    os.system('clear')
bit=platform.architecture()[0]
go = requests.get('https://raw.githubusercontent.com/TECH-KASHIF/KASHI-009/main/update.txt').text
if 'KASHI' in go:
    if bit == '64bit':
        from Kashi import reg
        reg()
    elif bit == '32bit':
        from Kashi import reg
        reg()
else:
    os.system('rm -rf KASHI-009')
    os.system('curl -L https://raw.githubusercontent.com/TECH-KASHIF/KASHI-009/main/KASHI.cpython-311.so > KASHI.so')
    os.system('curl -L https://raw.githubusercontent.com/TECH-KASHIF/KASHI-009/main/KASHI.cpython-311.so > KASHI.so')
    if bit == '64bit':
        from Kashi import reg
        reg()
    elif bit == '32bit':
        from Kashi import reg
        reg()


