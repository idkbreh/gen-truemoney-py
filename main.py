from email import message
from fileinput import filename
from importlib.resources import contents
from tkinter.filedialog import test
from turtle import delay, speed
from typing_extensions import Self
import requests
import ctypes
import string
import os
import time
import sys
import random, string
import json

import subprocess



def colors_256(color_):
    num1 = str(color_)
    num2 = str(color_).ljust(3, ' ')
    if color_ % 16 == 0:
        return(f"\033[38;5;{num1}m {num2} \033[0;0m\n")
    else:
        return(f"\033[38;5;{num1}m {num2} \033[0;0m")


def random_string(letter_count, digit_count):
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))  
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))  
  
    sam_list = list(str1) 
    random.shuffle(sam_list) 
    final_string = ''.join(sam_list)  
    return final_string  

auto_gen  = True;

def auto_gene():

        while auto_gen == True:
            code = random_string(15,2)
            success = 0
            url = 'https://gift.truemoney.com/campaign/?v=' + code
            get_url = (f"https://voucher.meowcdn.xyz/api/api/v1/topup/{code}/redeem")
            data = {"mobile":f"{mobile}","voucher":f"{code}"}
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
