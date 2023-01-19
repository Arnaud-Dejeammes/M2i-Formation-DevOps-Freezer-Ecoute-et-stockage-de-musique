# pip install psycopg2-binary
# une fonction par fichier

import sqlite3

con = sqlite3.connect("freezer3.db")
cur = con.cursor()

# Lancement du programme :
# On efface tout et on recommence sur des bases saines

def init(cur):
#	cur.execute("DROP TABLE IF EXISTS users")
#	cur.execute("DROP TABLE IF EXISTS musics")
	cur.execute("""CREATE TABLE users (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		ip TEXT NOT NULL,
		name TEXT NOT NULL,
		passwd TEXT NOT NULL)""")

	cur.execute("""CREATE TABLE musics (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name NOT NULL,
		path TEXT NOT NULL)""")
		
		#album TEXT,
		#FOREIGN KEY (album) REFERENCES album(id),
# init(cur)

# Si nouvel utilisateur on init sa table et on ajoute à la table users. Si non on fait rien

def add_utable (cur, user):
	cur.execute("CREATE TABLE" + user + """ (
	id INTEGER PRIMARY KEY,
	id_music INTEGER, 
	FOREIGN KEY (id_music) REFERENCES musics(id));""")


def inscription(nom, mdp):
	#pas d'input
	cur.execute("INSERT INTO users (name, passwd) VALUES (nom, mdp)")
	add_utable(cur, "name")


def affichage_table_user(user_name):
	cur.execute("SELECT * FROM" + user_name)
	res = cur.execute("SELECT * FROM" + user_name).fetchall()
	#<p>print(res)</p> ## affichage HTML CGI
	#ajouter tout ça en cgi

def affichage_bibliotheque():
	cur.execute("SELECT * FROM musics")
	result = cur.execute("SELECT * FROM musics")

def add_music(cur, titre, chemin):
	cur.execute("INSERT INTO" + musics (name, path) + "VALUES (titre, chemin)")
	cur.execute("INSERT INTO" + utable (name, path) + "VALUES (titre, chemin)")
	#ajoute dans la table music
	#ajoute dans la table de l'user

def del_music(cur, id):
	cur.execute("DELETE FROM utable WHERE id=?")
	#supprime de la table user


con.commit()










#cur.execute("CREATE TABLE artist (
#	id INTEGER PRIMARY KEY AUTOINCREMENT,
#	style TEXT,
#	discography TEXT)");

#cur.execute("create table discography (
#	id INTEGER primary key AUTOINCREMENT,
#	artist TEXT NOT NULL,
#	album TEXT,
#	FOREIGN KEY (artist) REFERENCES artist(id)
#	FOREIGN KEY (album) REFERENCES album(id)
#	)");
#
#cur.execute("""create table album (
#	id INTEGER primary key AUTOINCREMENT,
#	style TEXT,
#	FOREIGN KEY (style) REFERENCES style(id)
#	)""");
#
#cur.execute("create table style (
#	id INTEGER PRIMARY KEY AUTOINCREMENT,
#	name_style TEXT NOT NULL)");
