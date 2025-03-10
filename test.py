#!/bin/bash
#
# Usage : ./brute_force_child_urls.sh <BASE_URL> <WORDLIST>
# Exemple : ./brute_force_child_urls.sh http://exemple.com wordlist.txt
#
# Le script parcourt chaque ligne du wordlist et construit une URL 
# en ajoutant le fragment (fichier ou répertoire) à l'URL de base.
# Pour chaque URL, il réalise une requête HEAD (via curl) pour vérifier son existence.
# En cas de code HTTP 200, 301 ou 302, il affiche l'URL trouvée.
#

if [ "$#" -ne 2 ]; then
    echo "Usage : $0 <BASE_URL> <WORDLIST>"
    exit 1
fi

BASE_URL="$1"
WORDLIST="$2"

if [ ! -f "$WORDLIST" ]; then
    echo "Fichier wordlist '$WORDLIST' introuvable !"
    exit 1
fi

echo "Démarrage du test sur $BASE_URL avec le wordlist $WORDLIST..."
echo "-------------------------------------------------------------"

# Pour chaque ligne du wordlist
while IFS= read -r fragment; do
    # Nettoyer les espaces éventuels et ignorer les lignes vides
    fragment=$(echo "$fragment" | xargs)
    if [ -z "$fragment" ]; then
        continue
    fi

    # Construction de l'URL complète
    if [[ "$BASE_URL" == */ ]]; then
        URL="${BASE_URL}${fragment}"
    else
        URL="${BASE_URL}/${fragment}"
    fi

    # Réaliser une requête HEAD pour obtenir le code HTTP
    status=$(curl -s -o /dev/null -w "%{http_code}" -L "$URL")

    # Afficher l'URL si le code HTTP indique une ressource trouvée
    if [[ "$status" == "200" || "$status" == "301" || "$status" == "302" ]]; then
        echo "Trouvé : $URL (HTTP $status)"
        # Si vous souhaitez télécharger le contenu, décommentez la ligne suivante :
        # curl -L -o "download_${fragment//\//_}.html" "$URL"
    fi

done < "$WORDLIST"

echo "Test terminé !"
