from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from openai import *
# Initialisation du pilote Chrome
driver = webdriver.Chrome()
driver.get("https://accounts.google.com")

# Remplissez ici votre adresse e-mail Google
email = "double.dc789@gmail.com"

# Remplir l'adresse e-mail et cliquer sur "Suivant"
email_input = driver.find_element(By.ID, "identifierId")
email_input.send_keys(email)
driver.find_element(By.ID, "identifierNext").click()

# Attendre que le champ de mot de passe soit visible et remplir le mot de passe

# token openai : sk-proj-OEq74s8gIqNJwl7dkmQyT3BlbkFJBV7ivUpsgAJ8pYV89yaA

client = OpenAI(api_key="sk-proj-OEq74s8gIqNJwl7dkmQyT3BlbkFJBV7ivUpsgAJ8pYV89yaA")

def generate_response(comment, tweet):
    # Appel à l'API pour générer une réponse
    response = client.chat.completions.create(
      engine="gpt-3.5-turbo",
      messages=[
          {
          "role" : "user",
          "content": f"Voici un tweet, tu dois y repondre de facons a ajouter de la valeur a ton commentaire, la reponse ne peut pas exceder 280 caractere, la reponse a ce prompt dois UNIQUEMENT etre le commentaire, rien d'autre, tu dois repondre dans la meme langue que le tweet, voici le tweet: {tweet}"
          }
        ],
      temperature=1,
      max_tokens=256
    )
    response = comment
    return comment

# Attendre que la connexion soit terminée
time.sleep(15)

driver.get("https://twitter.com")

# Se connecter avec google
time.sleep(14)

# Attendre que la page se charge complètement
wait = WebDriverWait(driver, 30)
number = 0

while True:
    # Dezoommer la page
    driver.execute_script("document.body.style.zoom='45%'")

    # Trouver le premier tweet
    tweet = driver.find_element(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')

    tweet = tweet.text

    # Appelez la méthode de modération avec le texte du tweet
    moderation = client.moderations.create(input=tweet)

    comment = generate_response(comment, tweet)
    number += 1 
    print(f"Reponse n*{number}: {comment}")

    if moderation:
        comment = "Je suis pas dans sa moi"
    

    # Localiser l'élément du bouton des commentaires par sa classe CSS
    comment_button = driver.find_element(By.XPATH, '//*[@id="react-root"]')
    comment_button.click()

    time.sleep(3.5)

    # Localiser la zone de texte des commentaires
    comment_box = driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')

    # Commenter "test" et envoyer le commentaire
    comment_box.send_keys("test")
    comment_box.send_keys(Keys.RETURN)


    # Actualiser la page
    driver.refresh()

# Fermer le navigateur
driver.quit()
