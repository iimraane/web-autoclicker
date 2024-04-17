from instagrapi import Client
import sys
import json
from post_insta_hater_com import liste_commentaire

nombre1 = 0
nombre2 = 0

# Fonction pour commenter sur toutes les publications d'un utilisateur
def commenter_publications(client, username, commentaire, nombre1):
    user_id = client.user_id_from_username(username)
    # Récupérer toutes les publications de l'utilisateur
    publications = client.user_medias(user_id)
    for publication in publications:
        media_id = publication.pk
        # Poster un commentaire sur la publication
        client.post_comment(media_id, commentaire)
        nombre1 += 1
        print(f"Commentaire posté sur la publication {media_id}, c'est le {nombre1} ème !")

# Fonction pour commenter sur tous les reels d'un utilisateur
def commenter_reels(client, username, commentaire, nombre2):
    user_id = client.user_id_from_username(username)
    # Récupérer tous les reels de l'utilisateur
    reels = client.user_reels(user_id)
    for reel in reels:
        reel_id = reel.pk
        # Poster un commentaire sur le reel
        client.post_comment(reel_id, commentaire)
        nombre2 += 1
        print(f"Commentaire posté sur le reel {reel_id}, c'est le {nombre2} ème !")


print("Voulez vous lancer le bot ? (Oui/Non)")
while True:   
    choix = input("Votre choix :")

    if choix == "oui":
        break
    
    elif choix == "non":
        sys.exit()
    
    else:
        print("Veuillez entrer un choix valide...")

print()
print("Voulez vous parametrer vous meme les commentaires ou laisser le script faire ? (1/2)")
print()

choix2 = input("Entrez 1 ou 2 :")

if choix2 == "1":
    print("Veuillez entrer le/les commentaires voulu/s sous la forme ci-dessous:")
    print("['commentaire 1', 'commentaire 2', 'commentaire 3']")
    print()

    while True:
        liste_json = input("Entrez une liste Python au format JSON: ")

        try:
            # Convertir la chaîne JSON en une liste Python
            liste_python = json.loads(liste_json)
            break

        except json.JSONDecodeError:
            print("Erreur de décodage JSON. Assurez-vous d'entrer une liste au format JSON valide.")

    print()
    print("Lancement du script...")
    print()

    # Initialisation du client Instagrapi
    client = Client()

    # Connexion à un compte Instagram
    print()
    username = input("Nom d'utilisateur Instagram: ")
    password = input("Mot de passe Instagram: ")
    client.login(username, password)
    print()

    # Nom d'utilisateur du profil à commenter
    profile_username = input("Nom d'utilisateur du profil à commenter: ")

    # Commentaire à poster
    commentaire = liste_commentaire

    # Commenter toutes les publications et reels du profil
    commenter_publications(client, profile_username, commentaire)
    commenter_reels(client, profile_username, commentaire)

    # Déconnexion du compte Instagram
    client.logout()
    print("Déconnexion réussie")

elif choix2 == "2":
    print()
    print("Lancement du script...")
    print()

    # Initialisation du client Instagrapi
    client = Client()

    # Connexion à un compte Instagram
    print()
    username = input("Nom d'utilisateur Instagram: ")
    password = input("Mot de passe Instagram: ")
    client.login(username, password)
    print()

    # Nom d'utilisateur du profil à commenter
    profile_username = input("Nom d'utilisateur du profil à commenter: ")

    # Commentaire à poster
    commentaire = liste_commentaire

    # Commenter toutes les publications et reels du profil
    commenter_publications(client, profile_username, commentaire, nombre1)
    commenter_reels(client, profile_username, commentaire, nombre2)

    # Déconnexion du compte Instagram
    client.logout()
    print("Déconnexion réussie")
             

