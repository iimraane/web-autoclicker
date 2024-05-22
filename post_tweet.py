from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from openai import *
import random

client = OpenAI(api_key="sk-proj-OEq74s8gIqNJwl7dkmQyT3BlbkFJBV7ivUpsgAJ8pYV89yaA")

def generate_response():
    # Appel à l'API pour générer une réponse
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
          {
            "role": "system", "content": "You must write only the tweet, not your theme or even your tone",
          "role": "system", "content": "You are Alex, a curious man with a love for mystery books, indie music, and painting watercolor landscapes. You enjoy philosophical discussions, care deeply about the environment, and have a soft spot for vintage video games. You're the proud owner of a cat named Ziggy, relish culinary experiments, and find solace in running and rainy autumn days. and you must response only the tweet, not anything else, JUST THE TWEET with no emoji !",
          "role": "user",
          "content": "Craft one engaging tweets within 180 characters in english, reflecting current trends or timeless wisdom. Keep it concise, avoid emojis. Focus solely on the tweet content.",
          }
        ],
      temperature=1.7,
      max_tokens=150
    )
    content = response.choices[0].message.content
    return content

liked = False
while not liked:
    tweet = generate_response()
    
    print("Tweet generé:", tweet)
    print()
    user_feedback = input("Publier ce tweet ? (oui/non): ")
    
    if user_feedback.lower() == 'oui':
        liked = True
        print("Tweet approuvé !")
    else:
        print("Generation d'un autre tweet...")
        print()

print("Lancement du script ...")
time.sleep(random.uniform(0.7, 3))

# Twitter credentials (replace with your own)=
username = 'WhisperEcho_'
password = 'imrane789'

# Create a new instance of the browser driver
driver = webdriver.Chrome()

# Open Twitter login page
driver.get('https://twitter.com/login')

time.sleep(random.randint(4, 7))

# Trouvez l'élément en utilisant l'attribut 'name'.
element = driver.find_element(By.NAME, 'text').send_keys(username + Keys.RETURN)

time.sleep(random.uniform(3.5, 7.5))

# Find the password field and enter the password
driver.find_element(By.NAME, 'password').send_keys(password + Keys.RETURN)

time.sleep(random.randint(4, 7))

# Find the tweet button on the main page and click it
driver.find_element(By.XPATH, "//a[@data-testid='SideNav_NewTweet_Button']").click()

time.sleep(random.randint(5, 8))

# Find the tweet text area, enter the text "test"
driver.find_element(By.XPATH, "//div[@data-testid='tweetTextarea_0'] | //div[@role='textbox']").send_keys(tweet)

time.sleep(random.uniform(0.3, 0.7))

driver.find_element(By.XPATH, "//div[@data-testid='tweetTextarea_0'] | //div[@role='textbox']").send_keys(".")

time.sleep(random.uniform(2, 4.5))

# Cliquez sur le bouton Poster en utilisant la classe CSS et data-testid
tweet_button = driver.find_element(By.XPATH, "//div[@data-testid='tweetButton']")
tweet_button.click()

time.sleep(random.uniform(2, 4.5))

# Close the browser
driver.quit()