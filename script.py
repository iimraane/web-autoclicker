from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import emoji
from selenium.webdriver.common.keys import Keys

def element_interactable(element):
    try:
        return element.is_enabled() and element.is_displayed()
    except:
        return False

# Initialisation du pilote Chrome
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")

# Définir le script JavaScript pour faire défiler la page
scroll_script = "window.scrollBy(0, 100);"

# Attendre que la page de connexion soit entièrement chargée
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.NAME, "username")))

# Remplir le nom d'utilisateur et le mot de passe et cliquer sur le bouton de connexion
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

username_input.send_keys("YOUR EMAIL HERE")
password_input.send_keys("YOUR PASSWORD HERE")
login_button.click()

# Attendre que la page soit entièrement chargée après la connexion
time.sleep(3)

# URL du post vers lequel vous souhaitez naviguer
url_du_post = "URL OF YOUR POST HERE"
driver.get(url_du_post)

# Exécuter le script JavaScript pour faire défiler la page
driver.execute_script(scroll_script)

time.sleep(5)

text_zone = driver.find_element(By.CSS_SELECTOR, "textarea.x1i0vuye")
wait = WebDriverWait(driver, 10)
text_zone = wait.until(element_interactable(text_zone))

mot =[]

while True:
    # Générer un mot aléatoire
    letters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '^', '_', '`', '{', '|', '}', '~', 'a', 'b', 'c', 'd', 'e', 'f,' 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]
    mot = ''.join(random.choices(letters, k=12))

    time.sleep(3.5)

    # Saisir le mot généré dans la zone de texte
    text_zone.send_keys(mot, Keys.RETURN)

    # Attendre que le bouton de publication soit visible et cliquable
    # publish_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Publier')]")))
    # publish_button.click()

    # Attendre un court instant avant de cliquer sur le bouton "Post"



