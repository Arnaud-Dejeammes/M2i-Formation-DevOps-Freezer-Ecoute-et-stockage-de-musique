# pip install psycopg2-binary
# import psycopg2
import sqlite3
import sys
import re

#con = psycopg2.connect("freezer3.db")
con = sqlite3.connect("freezer3.db")
cur = con.cursor()
args=sys.argv

# Lancement du programme :
# On efface tout et on recommence sur des bases saines
def init(cur):
	cur.execute("DROP TABLE IF EXISTS users")
	cur.execute("DROP TABLE IF EXISTS musics")
	cur.execute("DROP TABLE IF EXISTS joint")
	cur.execute("""CREATE TABLE users (
		id_u INTEGER PRIMARY KEY AUTOINCREMENT,
		ip TEXT NOT NULL,
		name TEXT NOT NULL,
		passwd TEXT NOT NULL)""")

	cur.execute("""CREATE TABLE musics (
		id_m INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		path TEXT NOT NULL)""")

# Table de relation
	cur.execute("""CREATE TABLE joint (
		idu INTEGER,
		idm INTEGER,
		PRIMARY KEY (idu, idm),
		FOREIGN KEY (idu) REFERENCES users(id_u),
		FOREIGN KEY (idm) REFERENCES musics(id_m)
		)""")

		# # #album TEXT,
		# # #FOREIGN KEY (album) REFERENCES album(id),
# init(cur)

def inscription(cur, nom, mdp, ip):
	cur.execute("INSERT INTO users (name, passwd, ip) VALUES (?,?,?)",(nom, mdp, ip))

def connection(cur, nom, mdp):
	resconn = cur.execute("SELECT * FROM users WHERE name=? AND passwd=?",(nom,mdp)).fetchall()
	if resconn:
		return True
	else:
		return False

def aff_library(cur):
	result = cur.execute("SELECT * FROM musics").fetchall()
	print(result)

def aff_user_playlist(cur, nom):
	### DOUBLE JOINTURE ###
	id_user = cur.execute("SELECT id_u FROM users WHERE name=" + nom).fetchall()
	res = cur.execute("SELECT idm FROM joint JOIN users on id_u=idu JOIN musics on id_m=idm WHERE id_u=?", (id_user,)).fetchall()
	print(res)
	# return res
	# ajouter tout ça en cgi

def add_music(cur, nom, titre, path):
	# on ajoute dans la bibliothèque principale si la chanson n'y est pas déjà
	exists = cur.execute("SELECT * FROM musics WHERE name=?",(titre,))
	if exists:
		cur.execute("INSERT INTO musics (name, path) VALUES (?,?)",(titre, path))
	# récup l'id de la musique
	IDM = cur.execute("SELECT id_m FROM musics WHERE name=?",(titre,)).fetchone()    #		fetchall()[0][0]
	# récup l'id de l'User 
	IDU = cur.execute("SELECT id_u FROM users WHERE name=?",(nom,)).fetchone()    #		fetchall()[0][0]
	# ajoute le couple id_u id_m dans la table join
	print(IDM, IDU)
	cur.execute("INSERT INTO joint VALUES (?,?)",(IDU,IDM))

def del_music(cur, nom, titre):
	# récup l'id de la musique
	IDM = cur.execute("SELECT id_m FROM musics WHERE name=?",(titre,))
	# récup l'id de l'User
	IDU = cur.execute("SELECT id_u FROM users WHERE name=?",(nom))
	# supprime le couple id_u id_m dans la table join
	cur.execute("DELETE FROM joint WHERE id_u=? AND id_m=?",(IDU,IDM))

def help():
	print("Bienvenue dans freezer !")
	print("Application d'écoute et de téléchargement de musiques")
	print("Mode d'emploi : ")
	print("Ajoutez ces options en argument pour lancer le programme :")
	print("--help				:		afficher l'aide")
	print("--init				:		reboot la BDD et créer de nouvelles tables vides")
	print("--signup				:		ajouter un nouvel utilisateur à la BDD")
	print("--connection			:		vérifer les identifiants/mdp et connecter l'utilisateur")
	print("--aff_library		:		afficher l'ensemble des chansons contenu dans la BDD de l'app")
	print("--aff_user_playlist	:		afficher la playlist de l'utilisateur")
	print("--add_music			:		ajouter une musique dans la playlist de l'utilisateur (et dans la bibliothèque principale si elle n'y est pas")
	print("--del_music			:		supprimer une musique de la playlist de l'utilisateur")

choix=input("Souhaitez vous vous inscrire ou vous connecter ? 1/2: ")
if choix =="2":
	print("connection:")
	identifiant = input("Nom d'utilisateur: ")
	mdp = input(" Mot de passe: ")
	if connection(cur, identifiant, mdp) == False:
		print("Impoossible de se connecter")
		exit()
elif choix == "1":
	print("inscription:")
	identifiant = input("Nom d'utilisateur: ")
	mdp = input(" Mot de passe: ")
	ip="0.0.0.0"
	inscription(cur, identifiant, mdp, ip)


if args[1] == "--init":
	init(cur)
elif args[1] == "--signup" and args[2] == "regex user_name" and args[3] == "regex mdp" and args[4] == "regex ip":
    inscription(cur, args[2], args[3])
elif args[1] == "--conection" and args[2] == "regex user_name" and args[3] == "regex mdp":
	connection(cur, args[2], args[3])
elif args[1] == "--aff_library":
    aff_library(cur)
elif args[1] == "--aff_user_playlist" and args[2] == "regex user_name":
	aff_user_playlist(cur, args[2])
elif args[1] == "--insert" and args[2] == "regex user_name" and args[3] == "regex titre" and args[4] == "regex path/to/music":
	add_music(cur, args[2], args[3], args[4])
elif args[1] == "--delete" and args[2] == "regex titre":
	del_music(cur, args[2])
elif args[1] == "--help":
	help()
	exit()
else:
	help()
	exit()

con.commit()
