"""
Created on Thu Feb 25 20:30:30 2021

@author: Dimitris Vervitis
"""
import os 
import random

chars = 'abcdefghiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ12345678910!@#$%^&*()'

while 1:
    password_len = int(input('What length would your password to be : '))
    password_count = int(input("How many passwords would you like :"))

    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("Here is your password! :" ,password)
        
os.system("PAUSE")
