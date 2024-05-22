import subprocess
import json
import os
import glob
import requests
import base64

# Fonction pour télécharger la dernière story Snapchat et vérifier le type de média
def download_latest_snapchat_story(username, output_dir="output_directory"):
    # Créer le répertoire de sortie s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)
    
    # Commande pour télécharger les stories et sauvegarder les métadonnées JSON
    command = [
        'snapchat-dl',
        '-d',  # Dump JSON
        '-P', output_dir,  # Output directory
        '-l', '1',  # Limit to 1 story (latest)
        username
    ]
    
    # Exécuter la commande
    subprocess.run(command, check=True)
                        
# Nom d'utilisateur de la story Snapchat
username = input("Veuillez entrer le nom d'utilisateur de la personne a sniper : ")

date = input("Entrez la date d'aujourd'hui sous le format suivant : YYYY-MM-DD : ")

# Répertoire de sortie
output_directory = "C:/Users/windos 10/Desktop/Storys"

# Télécharger la dernière story et détecter le type de contenu
download_latest_snapchat_story(username, output_dir=output_directory)

import requests


def upload_image_to_imgbb(api_key, image_path):
    global image_url
    url = "https://api.imgbb.com/1/upload"
    with open(image_path, "rb") as file:
        image_data = file.read()
        encoded_image = base64.b64encode(image_data).decode('utf-8')
    
    payload = {
        "key": api_key,
        "image": encoded_image
    }
    
    response = requests.post(url, data=payload)
    response_json = response.json()
        
    image_url = response_json["data"]["url"]
    
    print(f"Image URL: {image_url}")
        

try:
    folder_path = f"C:/Users/windos 10/Desktop/Storys/{username}/{date}"
    # List all files in the given directory
    files = os.listdir(folder_path)
    
    # Filter for files with .jpg extension
    jpg_files = [file for file in files if file.lower().endswith('.jpg')]
    
except Exception as e:
    print(f"An error occurred: {e}")
  
        
            
# Clé API Imgbb
api_key = "ad1c22b3a476cb83a87254ebfe8dd11f"

# Chemin vers l'image à télécharger
image_path = f"C:/Users/windos 10/Desktop/Storys/{username}/{date}/{jpg_files[0]}"

# Appel de la fonction pour télécharger l'image
upload_image_to_imgbb(api_key, image_path)



url = f"https://api.apilayer.com/image_to_text/url?url={image_url}"

payload = {}
headers= {
  "apikey": "JkrewFDXfIvzMjBNr9cbL7uUhEhSkV8O"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text

print(result)