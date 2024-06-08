#!/usr/bin/env python3
import hashlib
from hashlib import *
import os
import time
from time import sleep
from pystyle import *

os.system('clear')
Write.Print("""
           SUPER HASHING TOOLS V.1.0
           .........................
             Please Choose Option
           .........................

  1] Hash checker <-_->  2] Hash length  <-_->

  3] Hash type    <-_->  4] Md5 encrypt  <-_->

  5] Md5 decrypt  [-_-] >>> @Ousmane team@Coder

                00] to exit\n""",Colors.white_to_red,interval=0.02)

print(" ")
print(" ")
choose = input('        \033[31mroot\033[32m@>>>\033[1;37mEnterOption:\033[32m~\033[37m# ')

def checker():
    os.system('clear')
    print(" ")
    Write.Print("""
        =====================================
        [   This option for Hash Checker    ]
        =====================================
    """,Colors.red_to_blue,interval=0.02)
    print(" ")
    hash1 = input('[+] Enter hash1 >>> ')
    print(" ")
    hash2 = input('[+] Enter hash2 >>> ')
    print(" ")
    if hash1 == hash2:
        print('\033[32mThe Hash is Clean <-_->')
    else:
        print('\033[31m[-]Wrong the Hash is Virus ×_×')
#checker()

#Hash Length def()
def length():
    os.system('clear')
    Write.Print("""
   =================================================
  (       This option for Hash length Checker      )
  ==================================================
  """,Colors.blue_to_red,interval=0.02)
    print(" ")
    length = input('[+] Enter the hash :\033[32m')
    print(" ")
    print('\033[37m[+] The hash length is : \033[31m', len(length))
    print(" ")
#length()

#hash type 

def type():
    os.system('clear')
    Write.Print("""
    ===========================================
    [       This option for hash type         ]
    ===========================================
    """,Colors.white_to_blue,interval=0.02)
    print(" ")
    hash_type = input('[!] Enter Hash \033[1;31m:>>\033[1;37m')
    print(" ")
    length = len(hash_type)
    if length == 32:
        print('[=] The hash is \033[32m md5\033[37m')
        print(" ")
    if length == 40:
        print('[=] The hash is \033[32m sha1\033[37m')      
        
    if length == 56:
        print('[=] The hash is \033[32m sha224\033[37m')        
    if length == 64:
        print('[=] The hash is \033[32m sha256\033[37m')              
    if length == 96:
        print('[=] The hash is \033[32m sha384\033[37m')              
    if length == 128:
        print('[=] The hash is \033[32m sha512\033[37m')              
#type()

#text to md5
def text_md5():
    os.system('clear')
    Write.Print("""
     ===========================================
     {      This option for text to md5        }
     ===========================================
   """,Colors.green_to_white,interval=0.02)
    print(" ")
    word = input('[+] Enter txt_md5 >> ')
    print("")
    md5 = hashlib.md5(word.encode())
    print(md5.hexdigest())
#text_md5()

#decrypt

def decrypt():
    os.system('clear')
    Write.Print("""
    ===========================================
    #    This option for hash decrypt         #
    ===========================================
    """,Colors.green_to_red,interval=0.02)
    print(" ")
    try:

        hashh = input("[#] Enter hash : ")
        print(" ")
        file = input("[#] Enter file : ")
        print(" ")
        with open(file, mode='r') as f:
            for line in f:
                line = line.strip()
                if md5(line.encode()).hexdigest() == hashh:
                    print("[-] Password Found : \033[1;32m" +line)
                #else:
                    #print("\033[1;37m[!] Password Not !")
    except:
        Write.Print("Please enter the hash and file path >_<",Colors.red,interval=0.1)
        decrypt()
#decrypt()

if choose == "1":
    checker()
    print(" ")
    input('\033[1;37mpress enter ...')
    print(" ")
    os.system('python3 hash.py')
elif choose == '2':
    length()
    print(" ")
    input("press enter ...")
    os.system('python3 hash.py')
elif choose == '3':
    type()
    print(" ")
    input("press enter ...")
    os.system('python3 hash.py')
elif choose =='4':
    text_md5()
    print(" ")
    input("press enter ...")
    os.system('python3 hash.py')
elif choose == '5':
    decrypt()
    print(" ")
    input("press enter ...")
    os.system('python3 hash.py')
elif choose == '00' or choose == '0':
    os.system('clear')
    Write.Print("""
    Thank you for using my tools have a good daye

    @Ousmane_team@Coder_Cyber_Security_Tools -_-
    """,Colors.blue_to_white,interval=0.1)
    print(" ")
    print("\t\033[1;32m  ", time.ctime(),'\033[37m')
    os.system('exit')
else:
    os.system('clear')
    Write.Print("""
     Please choose option ×_× \n""",Colors.red,interval=0.1)
    time.sleep(1)
    os.system('python3 hash.py')
