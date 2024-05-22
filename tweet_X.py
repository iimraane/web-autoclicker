from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from openai import *
import mysql.connector
from mysql.connector import Error
import  datetime
import random
import pyautogui

# Paramètres de connexion à la base de données
connection = mysql.connector.connect(
    host='localhost',       # L'adresse du serveur, généralement 'localhost' pour un serveur local
    user='root',      # Votre nom d'utilisateur MySQL
    password='imrane789',  # Votre mot de passe MySQL
    database='my_twitter_data'      # Le nom de la base de données que vous souhaitez utiliser
)
cursor = connection.cursor()

# token openai : sk-proj-OEq74s8gIqNJwl7dkmQyT3BlbkFJBV7ivUpsgAJ8pYV89yaA

client = OpenAI(api_key="sk-proj-OEq74s8gIqNJwl7dkmQyT3BlbkFJBV7ivUpsgAJ8pYV89yaA")

def generate_response(tweet_text):
    # Appel à l'API pour générer une réponse
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
          {
          "role": "system", "content": "You are a twitter user and you give a response at a tweet. You must write only the response",
          "role": "user",
          "content": f"Respond concisely to the tweet, within 100 characters, in the same language. Focus solely on its content. Avoid emojis. Here's the tweet: {tweet_text}."
        
          }
        ],
      temperature=1,
      max_tokens=180
    )
    content = response.choices[0].message.content
    return content

def move_and_click(x, y):
  """Move the mouse to an element and click it using PyAutoGUI."""
  pyautogui.moveTo(x, y, duration=random.uniform(1.5, 3))  # Move the cursor to the x, y position over 1 second
  pyautogui.click()

# Initialisation du pilote Chrome
driver = webdriver.Chrome()

# Twitter credentials (replace with your own)
username = 'WhisperEcho_'
password = 'imrane789'

driver.get("https://twitter.com/login")

time.sleep(random.randint(6, 8))

# Trouvez l'élément en utilisant l'attribut 'name'.
element = driver.find_element(By.NAME, 'text').send_keys(username)

move_and_click(x=800, y=850)

time.sleep(random.uniform(3.5, 7.5))

# Find the password field and enter the password
driver.find_element(By.NAME, 'password').send_keys(password)

move_and_click(x=800, y=800)

time.sleep(random.randint(4, 8))

# Attendre que la page se charge complètement
wait = WebDriverWait(driver, 60)
number = 0

while True:
    # Dezoommer la page
    driver.execute_script("document.body.style.zoom='40%'")

    time.sleep(random.uniform(0.7, 1.6))

    timeout = 70
    # Wait until the element identified by the data-testid 'tweet' is present and displayed
    tweet = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, "//article[@data-testid='tweet']")))
    # Localiser l'élément par 'data-testid'
    tweet_element = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetText"]')

    # Localiser l'élément link par son attribut rel="canonical"
    tweet_link_element = driver.find_element(By.CSS_SELECTOR, 'article [role="link"][dir="ltr"]')
    # Extraire l'URL du tweet
    tweet_url = tweet_link_element.get_attribute('href')

    # Check if the URL is already in the database
    cursor.execute("SELECT COUNT(*) FROM tweets WHERE twitter_link = %s", (tweet_url,))
    result = cursor.fetchone()

    if result[0] > 0:
      # If the tweet URL is already in the database, refresh the page
      driver.refresh()
      time.sleep(random.uniform(0.7, 1.7))
      continue  # Skip to the next iteration of the loop
    
    # Extraire le texte du tweet
    tweet_text = tweet_element.text
    comment = generate_response(tweet_text)

    def remove_emojis(text):
      return ''.join(char for char in text if ord(char) <= 0xFFFF)
    
    clean_comment = remove_emojis(comment)

    number += 1 
    print()
    print()
    print(f"Tweet n*{number}: {tweet_text}")
    print()
    print(f"Reponse n*{number}: {clean_comment}")
    print()
    print()

    # Cliquer sur le bouton de réponse représenté par le petit logo commentaire
    reply_button = driver.find_element(By.CSS_SELECTOR, "div[data-testid='reply']")
    driver.execute_script("arguments[0].click();", reply_button)

    time.sleep(random.uniform(0.9, 2.3))

    # Localiser l'élément time par son tag
    time_element = driver.find_element(By.CSS_SELECTOR, 'time[datetime]')
    # Extraire l'attribut 'datetime' de l'élément <time>
    tweet_datetime = time_element.get_attribute('datetime')
    # Obtenir la date d'aujourd'hui
    today_date = datetime.date.today()


    # Extraire le nom d'utilisateur du lien
    username = tweet_url.split('/')[3]  # Divise l'URL par '/' et récupère le 4ème élément
    username.startswith("@")
    
    scroll_command = "window.scrollBy(0, arguments[0]);"
    # Randomly scroll up or down
    scroll_distance = random.randint(-100, 100)
    driver.execute_script(scroll_command, scroll_distance)
    time.sleep(random.uniform(0.2, 1))  # Pause after scrolling

    # Localiser la zone de texte des commentaires
    comment_box = driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]')
    time.sleep(random.uniform(0.5, 1.2))
    # Commenter et envoyer le commentaire

    for char in comment:
      comment_box.send_keys(char)

    time.sleep(random.uniform(0.5, 1.5))
    comment_box.send_keys(Keys.CONTROL + Keys.ENTER)
    time.sleep(random.uniform(3.5, 5))

    # Convertir la chaîne de date/heure en un objet datetime
    tweet_datetime_obj = datetime.datetime.strptime(tweet_datetime, '%Y-%m-%dT%H:%M:%S.%fZ')
    # Formater tweet_datetime_obj au format 'YYYY-MM-DD HH:MM:SS'
    formatted_tweet_datetime = tweet_datetime_obj.strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute("INSERT INTO tweets (tweet_text, user_handle, twitter_link, tweet_date) VALUES (%s, %s, %s, %s)", (tweet_text, username, tweet_url, formatted_tweet_datetime))
    cursor.execute("INSERT INTO comments (comment_text, comment_date) VALUES (%s, %s)", (comment, today_date))

    connection.commit()

    # Actualiser la page
    driver.refresh()

    time.sleep(random.uniform(3.5, 5.5))

