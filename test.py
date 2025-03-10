base_url="http://example.com"
curl -sL "$base_url" | grep -oP '(?<=href=")[^"]*' | while read -r url; do
    # Vérifier si l'URL est relative
    if [[ "$url" =~ ^/ ]]; then
        url="$base_url$url"  # Ajouter le domaine
    fi

    # Vérifier si c'est une URL valide (HTTP/HTTPS)
    if [[ "$url" =~ ^https?:// ]]; then
        echo "Téléchargement de : $url"
        curl -O "$url"
    fi
done
