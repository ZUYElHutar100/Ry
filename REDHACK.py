#! /usr/bin/env python3
# Author by @Anonymousproofficial
# Support me with follow my facebook page https://www.facebook.com/anonymousproo1
# Disclaimer: please dont re-edit or recode the original source code !
# Last update: 01/04/2024 - version 2.0

import os, re, sys, time, json, requests, textwrap, socket
from email_validator import validate_email, EmailNotValidError
from googlesearch import search
#from lxml.html import fromstring
from getpass import getpass
from shutil import which

r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
b = "\033[34m"
p = "\033[35m"
d = "\033[2;37m"
w = "\033[0m"

W = f"{w}\033[1;47m"
R = f"{w}\033[1;41m"
G = f"{w}\033[1;42m"
Y = f"{w}\033[1;43m"
B = f"{w}\033[1;44m"

home = os.getenv("HOME")
cokifile = ".cookies"
space = "         "
lines = space + "-"*44
apihack = "https://api.hackertarget.com/{}/?q={}"
mbasic = "https://mbasic.facebook.com{}"
graph = "https://graph.facebook.com{}"
headers = {"User-Agent":"Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.334; U; id) Presto/2.5.25 Version/10.54"}
logo = f"""{b}
██████╗ ███████╗██████╗ ██╗  ██╗ █████╗  ██████╗██╗  ██╗
██╔══██╗██╔════╝██╔══██╗██║  ██║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝█████╗  ██║  ██║███████║███████║██║     █████╔╝ 
██╔══██╗██╔══╝  ██║  ██║██╔══██║██╔══██║██║     ██╔═██╗ 
██║  ██║███████╗██████╔╝██║  ██║██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                        

                       {w}[ R.E.D.H.A.C.K ]{b}
           {d}REDHACK Information Gathering Tools{w}
               {d}Author by {w}{r}Anonymous Pro{w}"""

def menu():
    os.system("clear")
    print(logo)
    print(f"""
         {W}\033[2;30m Choose number of Perform Tools {w}
    
        {G}{b}  01{B} User Name Recon    {B} 
        {G}{b}  02{B} Facebook Hacking   {B} 
        {G}{b}  03{B} Email/Mail Finder     {B} 
        {G}{b}  04{B} Google Dork Hack    {B} 
        {G}{b}  05{B} Phone Number Track With NID Card {B} 
        {G}{b}  06{B} DNSLookup info   	 {B} 
        {G}{b}  07{B} Whoislookup info  	{B} 
        {G}{b}  08{B} SubnetLckup  info     {B} 
        {G}{b}  09{B} Hostfinder  info		  {B} 
        {G}{b}  10{B} DNSfinder info		    {B} 
        {G}{b}  11{B} Reverse ip   				 {B} 
        {G}{b}  12{B} Ip Location Track       {B} 
        """)
    mainmenu()

def mainmenu():
    while True:
        try:
            cmd = str(input(f"{space}{w}{b}>{w} choose:{b} "))
            if int(len(cmd)) < 6:
                if cmd in ("exit","Exit"): exit(r+space+"* Exiting !"+w)
                elif cmd in ("1","01"): userrecon()
                elif cmd in ("2","02"): fb.facedumper()
                elif cmd in ("3","03"): mailfinder()
                elif cmd in ("4","04"): godorker()
                elif cmd in ("5","05"): phoneinfo()
                elif cmd in ("6","06"): infoga("dnslookup")
                elif cmd in ("7","07"): infoga("whois")
                elif cmd in ("8","08"): infoga("subnetcalc")
                elif cmd in ("9","09"): infoga("hostsearch")
                elif cmd in ("10"): infoga("mtr")
                elif cmd in ("11"): infoga("reverseiplookup")
                elif cmd in ("12"): iplocation()
                else: continue
            else: continue
        except KeyboardInterrupt:
            exit(f"{r}\n{space}* Aborted !")


            except KeyboardInterrupt:
                break
        f.close()
        print(w+lines)
        print(f"{space}{b}>{w} {str(len(listloc))} retrieved as: {y}dump_location.txt{w}")
        getpass(space+"press enter for back to previous menu ")
        menu()

if __name__ == "__main__":
    arg = sys.argv
    fb = Facebook()
    if len(arg) == 1: menu()
    elif len(arg) == 2:
        if arg[1] in ("update"):
            if which("termux-setup-storage"): path = "$PREFIX/bin/REDHACK"
            else:
                if os.path.isdir("/usr/local/bin/"): path = "/usr/local/bin/REDHACK"
                else: path = "/usr/bin/REDHACK"
                  print(f"{b}>{w} the script have been updated")
        else: exit(r+"* no command found for: "+str(arg[1:]).replace("[","").replace("]",""))
    else: exit(r+"* no command found for: "+str(arg[1:]).replace("[","").replace("]",""))