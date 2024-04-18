from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialisation du pilote Chrome
driver = webdriver.Chrome()
driver.get("https://accounts.google.com")

# Remplissez ici votre adresse e-mail Google
email = "double.dc789@gmail.com"
password = "imrane789"

# Remplir l'adresse e-mail et cliquer sur "Suivant"
email_input = driver.find_element(By.ID, "identifierId")
email_input.send_keys(email)
driver.find_element(By.ID, "identifierNext").click()

# Attendre que le champ de mot de passe soit visible et remplir le mot de passe

# Attendre que la connexion soit terminée
time.sleep(15)

driver.get("https://twitter.com")

# Se connecter avec google
time.sleep(14)

# Attendre que la page se charge complètement
wait = WebDriverWait(driver, 30)

# Dezoommer la page
driver.execute_script("document.body.style.zoom='45%'")

# Trouver le premier tweet
tweet = driver.find_element(By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]')

# Cliquer sur le bouton commentaire
comment_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="reply"]')
comment_button.click()

# Attendre que la zone de commentaire soit visible
comment_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='tweetTextarea_0']")))

# Commenter "test" et envoyer le commentaire
comment_box.send_keys("test")
comment_box.send_keys(Keys.RETURN)

# Attendre un court instant
time.sleep(2)

# Actualiser la page
driver.refresh()

# Attendre que la page se charge à nouveau
wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='tweet']")))

# Répéter le processus de commentaire
tweet = driver.find_element(By.XPATH, "//div[@data-testid='tweet']")
comment_button = tweet.find_element(By.XPATH, ".//div[@data-testid='reply']")
comment_button.click()

comment_box = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='tweetTextarea_0']")))
comment_box.send_keys("test")
comment_box.send_keys(Keys.RETURN)

# Fermer le navigateur
driver.quit()
