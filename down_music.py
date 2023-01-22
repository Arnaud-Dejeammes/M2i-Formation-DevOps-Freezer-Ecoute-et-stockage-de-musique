from pytube import Search
from pytube import YouTube
import os
import webbrowser
choix_mus="billie jean"
s=Search(choix_mus)
recherche=s.results[0]
yt=YouTube (f"{recherche.watch_url}")
of=yt.streams.filter(only_audio=True).first().download()
nf=choix_mus+'.mp3'
os.rename(of,nf)
webbrowser.open(nf)
