#!/bin/bash

# Site à télécharger
site="https://exemple.com"

# Télécharger la page principale
curl -O "$site"

# Extraire les liens internes et les télécharger
curl -s "$site" | grep -oP '(?<=href=")[^"#?]*' | while read link; do
    # Vérifier que le lien est relatif
    if [[ "$link" =~ ^/ ]]; then
        link="$site$link"
    fi
    # Télécharger les pages
    curl -O "$link"
done

