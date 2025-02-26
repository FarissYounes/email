#!/bin/bash

base_url="https://exemple.com"  # Remplacez par l'URL de départ
destination="fichiers_html"       # Dossier où stocker les fichiers

mkdir -p "$destination"

curl -s "$base_url" -o main.html

grep -oP '<a\s+href="[^"]+">.*?</a>' main.html | while read -r ligne; do
    # Extraire l'attribut href
    href=$(echo "$ligne" | grep -oP '(?<=href=")[^"]+')
    # Extraire le texte entre <a> et </a>
    texte=$(echo "$ligne" | sed -e 's/.*">//' -e 's/<\/a>.*//')
    
    # Si href est vide, passer à l'itération suivante
    [ -z "$href" ] && continue

    # Si le lien est relatif, on le transforme en URL absolue
    if [[ "$href" != http* ]]; then
        href="${base_url%/}/$href"
    fi

    # Vérifier que l'URL se termine par .html ou .htm
    if [[ "$href" =~ \.html?$ ]]; then
        # Si le texte est vide, utiliser le nom de fichier de l'URL (sans extension)
        if [ -z "$texte" ]; then
            texte=$(basename "$href")
            texte="${texte%.*}"
        fi

        # Nettoyer le nom pour qu'il ne contienne que des lettres, chiffres ou underscores
        nom_fichier=$(echo "$texte" | tr -cd '[:alnum:]_')
        [ -z "$nom_fichier" ] && nom_fichier="inconnu"

        # Définir le chemin complet du fichier à enregistrer
        sortie="${destination}/${nom_fichier}.html"

        echo "Téléchargement de $href -> $sortie"
        curl -s "$href" -o "$sortie"
    fi
done
