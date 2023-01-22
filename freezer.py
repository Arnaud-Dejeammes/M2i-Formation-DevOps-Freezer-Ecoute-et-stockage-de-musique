from ftplib import FTP
import os
from pytube import YouTube
#import playsound
import ftplib
import webbrowser
import vlc
import time

login=input("Quel est votre login")
mdp=input("Quel est votre mot de passe")
server=input("Quel est votre serveur")


try:
    os.mkdir(login+'_musiques')

except:
    print('')


#Création des dossiers
#os.mkdir('nos_musiques')
#connect=FTP(server,login,mdp)
dir=login+'_musiques'
print(dir)
os.chdir(dir)
try:
    connect = FTP('192.168.56.102','guest1','guest1')

    #connect = FTP('192.168.56.102',login,mdp)
#    connect.mkd(login+'_musiques')
    #connect.login(login,mdp)
    #connect.sendcmd('USER login') # '331 Please specify the password.'
    #connect.sendcmd('PASS mdp')
except ftplib.error_perm as error:
    print ('error')


try:
   connect.mkd('nos_musiques')
except:
    print('')
boucle=True
while (boucle==True):
    #os.mkdir('nos_musiques')
    #os.mkdir('user_musiques')
    #Pour se connecter au serveur
    rep = connect.nlst('nos_musiques')
    print (rep)

    #[f for f in listdir(nos_musiques) if isfile(join(nos_musiques, f))]
    #fichiers=os.listdir(login+'_musiques')
    fichiers=os.listdir()
    print(fichiers)
    choix_mus=input("Quelle musique voulez-vous écouter ?")
    choix_mus=choix_mus+'.mp3'
    lien='nos_musiques/'+choix_mus
    if choix_mus in fichiers :
        #shutil.move(choix_mus,'user_musiques')
       # file = open(choix_mus, 'rb')
        webbrowser.open(login+'_musiques\/'+choix_mus)

    elif lien in rep:

        #commande = raw_input('Tapez la commande à effectuer :

        print(lien)
        connect = FTP('192.168.56.102','guest1','guest1')
        #with open(lien, 'rb'): # ici, j'ouvre le fichier
        #connect.storbinary('STOR '+choix_mus, user_musiques)
        connect.voidcmd('TYPE I')
        #f=open('/home/guest1/nos_musiques/sodade.mp3' , 'rb')
        #t=connect.transfercmd('RETR '+lien)
        cmd="lftp {0}:{1}@{2} -e 'get {3};quit'".format(login,mdp,server,lien)
        os.popen(cmd)
        #time.sleep(5)
    #    os.replace(lien,login+'_musiques')

        #media=vlc.MediaPlayer( choix_mus)
        #media.play()
        webbrowser.open(login+'_musiques/'+ choix_mus)
    else:
        # requete  demande de telechargement de la music

        cmd="lftp {0}:{1}@{2} -e 'put {3};quit'".format(login,mdp,server,lien)
        os.popen(cmd)
        webbrowser.open(login+'_musiques/'+ choix_mus)

    reponse=input("Voulez-vous continuer ? (O/n)").upper()
    if reponse == "N":
        boucke = False

    #ftp.storbinary('STOR ' + mp3.title + '.mp3', open(mp3.title + '.mp3', 'rb'))
#                    playsound.playsound('user_musiques/'+ choix_mus)



