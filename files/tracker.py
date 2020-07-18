#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import requests
import json
import time
import urllib
import os

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'

class config:
	key = "2dfa8e4851add96619e675427cdb72f1" #go to https://numverify.com/ and sign up if if get error. This API token is mine so after 100 use of this token this tool will not work. So you have to wait for next update or ask at my Telegram Group: http://t.me/linux_repo

def banner():
	os.system('clear')
	print  (color.BLUE + """
████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
   ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
	Version: 1.6-DEV by @AbirHasan2005                 
	""" + color.END)

def main():
	banner()
	if len(sys.argv) == 2:
		number = sys.argv[1]
		api = "http://apilayer.net/api/validate?access_key=" + config.key + "&number=" + number + "&country_code=&format=1"
		output = requests.get(api)
		content = output.text
		obj = json.loads(content)
		country_code = obj['country_code']
		country_name = obj['country_name']
		location = obj['location']
		carrier = obj['carrier']
		line_type = obj['line_type']

		print (color.BLUE + "[+] " + color.END + "Phone number information gathering")
		print ("--------------------------------------")
		time.sleep(0.2)

		if country_code == "":
			print (" - Getting Country		[ " + color.RED + "FAILED " + color.END + "] ")
		else:
			print (" - Getting Country		[ " + color.GREEN + "OK " + color.END + "]")

		time.sleep(0.2)
		if country_name == "":
			print (" - Getting Country Name		[ " + color.RED + "FAILED " + color.END + "]")
		else:
			print (" - Getting Country Name		[ " + color.GREEN + "OK " + color.END + "]")

		time.sleep(0.2)
		if location == "":
			print (" - Getting Location		[ " + color.RED + "FAILED " + color.END + "]")
		else:
			print (" - Getting Location		[ " + color.GREEN + "OK " + color.END + "]")

		time.sleep(0.2)
		if carrier == "":
			print (" - Getting Carrier		[ " + color.RED + "FAILED " + color.END + "]")
		else:
			print (" - Getting Carrier		[ " + color.GREEN + "OK " + color.END + "]")

		time.sleep(0.2)
		if line_type == None:
			print (" - Getting Device		[ " + color.RED + "FAILED " + color.END + "]")
		else:
			print (" - Getting Device		[ " + color.GREEN + "OK " + color.END + "]")

		print ("")
		print (color.BLUE + "[+] " + color.END + "Information Output")
		print ("--------------------------------------")
		print (" - Phone number: " +str(number))
		print (" - Country: " +str(country_code))
		print (" - Country Name: " +str(country_name))
		print (" - Location: " +str(location))
		print (" - Carrier: " +str(carrier))
		print (" - Device: " +str(line_type))
	else:
		print ("[TRACKER] Usage:")
		print ("./%s <phone-number>" % (sys.argv[0]))
		print ("./%s +13213707446" % (sys.argv[0]))

main()