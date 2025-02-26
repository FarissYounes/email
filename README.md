import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL de la page à parser
url = "https://exemple.com"  # Remplacez par l'URL de départ
response = requests.get(url)
if response.status_code != 200:
    raise Exception(f"Erreur lors de la récupération de la page : {url}")

# Parser le HTML de la page
soup = BeautifulSoup(response.text, 'html.parser')

# Répertoire où sauvegarder les fichiers téléchargés
dossier_destination = "fichiers_html"
if not os.path.exists(dossier_destination):
    os.makedirs(dossier_destination)

# Récupération de toutes les balises <a> avec un href
balises_a = soup.find_all('a', href=True)
for balise in balises_a:
    href = balise['href']
    # Reconstruire l'URL complète (au cas où href soit relatif)
    url_complet = urljoin(url, href)
    
    # Récupérer le texte entre <a> et </a> pour nommer le fichier
    nom_fichier = balise.get_text().strip()
    # Si le texte est vide, on utilise le dernier segment de l'URL (sans l'extension)
    if not nom_fichier:
        nom_fichier = os.path.splitext(os.path.basename(url_complet))[0]
        if not nom_fichier:
            nom_fichier = "inconnu"
    
    # On vérifie que l'URL se termine par .html (ou .htm selon vos besoins)
    if url_complet.lower().endswith((".html", ".htm")):
        try:
            page_html = requests.get(url_complet)
            if page_html.status_code == 200:
                # Construction du chemin complet pour enregistrer le fichier
                chemin_fichier = os.path.join(dossier_destination, f"{nom_fichier}.html")
                with open(chemin_fichier, "w", encoding="utf-8") as fichier:
                    fichier.write(page_html.text)
                print(f"Téléchargé : {url_complet} -> {chemin_fichier}")
            else:
                print(f"Erreur lors du téléchargement de {url_complet} : {page_html.status_code}")
        except Exception as e:
            print(f"Exception lors du téléchargement de {url_complet} : {e}")
