#coding=utf-8
import os, sys, platform

os.system('rm -rf KASHI.cpython-311.so KASHI.so')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf KASHI.cpython-311.so KASHI.so')
except:
    pass


bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('KASHI.cpython-311.so'):
        os.system('curl -L https://raw.githubusercontent.com/TECH-KASHIF/KASHI-009/main/KASHI.cpython-311.so') 
        import KASHI
    else:
        import KASHI

elif bit == '32bit':
    if not os.path.isfile('KASHI.so'):
        os.system('curl -L https://raw.githubusercontent.com/TECH-KASHIF/KASHI-009/main/KASHI.so') 
        import Kashi
    else:
        import Kashi
