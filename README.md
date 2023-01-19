# FREEZER #

# M2i-Formation-DevOps-Freezer-Ecoute-et-stockage-de-musique #

#################
# Développement #
#################

* Hayet Yefsah
[hayetyefsah](https://github.com/hayetyefsah)
* Charles Ramade
[smogg22](https://github.com/Smogg22)
* Yassine Nassiri
[Yvss059](https://github.com/Yvss059)
* Julio Aspajo Durand
[jaspajod](https://github.com/jaspajod)
* Arnaud Dejeammes
[Arnaud-Dejeammes](https://github.com/Arnaud-Dejeammes)

###############
# Supervision #
###############

* Loup Fourment
[bkoj-arch](https://github.com/bkoj-arch)

###############
# Description #
###############

Service pour stocker et écouter de la musique gratuitement.

Sur un serveur distant, création de plusieurs utilisateurs.

Chaque utilisateur possède dans son répertoire personnel un dossier "Freezer_Music", où se trouvent stockés les morceaux de musique qu'il pourra récupérer et lire chez lui.

[CÔTÉ UTILISATEUR]

Lorsque l'utilisateur lance le programme Freezer :

- demande des identifiants pour se connecter,
- liste de tous ses morceaux de musique par ordre alphabétique,
- et demande de celui qu'il veut écouter.

Si le morceau de musique est déjà présent dans le répertoire distant, la musique est téléchargée sur la machine locale, dans le dossier "Freezer_Music" de l'utilisateur, puis elle est lue localement.

Si le morceau de musique n'est pas présent dans le répertoire distant, la musique est téléchargée depuis Youtube sur la machine de l'utilisateur, elle est lue localement, et est ajoutée au répertoire "Freezer_Music" distant de l'utilisateur pour la prochaine fois.

L'utilisateur répète ces requêtes autant de fois qu'il le souhaite avant de quitter le programme Freezer.

La connexion doit être sécurisée.



