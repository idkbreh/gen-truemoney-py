from importlib.resources import contents
from typing_extensions import Self
import requests
import ctypes
import string
import os
import time
import sys
import random, string
import json



def soom(letter_count, digit_count):
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))  
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))  
  
    sam_list = list(str1) 
    random.shuffle(sam_list) 
    final_string = ''.join(sam_list)  
    return final_string  

auto_gen  = True;

def auto_gene():

        while auto_gen == True:
            code = soom(16,2)
            success = 0
            url = 'https://gift.truemoney.com/campaign/?v=' + code
            get_url = (f"https://api.tanny.club/{code}/redeem/{mobile}")
      #Update Api Meowcdn บิดไปละ
            r = requests.post(get_url, data=json.dumps(data))
            if r.status_code != 200:
                success =+ float(1)
                ctypes.windll.kernel32.SetConsoleTitleA(success)
                print("[SUCCESS] " + url)
            else:
                print("[trash] "+url)
os.system('cls')

ctypes.windll.kernel32.SetConsoleTitleA("generate aungpao by SIMP#2712 discord https://discord.gg/XAmMUcCAJe")
print("generate aungpao by SIMP#2712 dont sell this shit ( your own risk ) ")
print('\n')
mobile = input("Enter Your Phone Number : ")

auto_gene()

