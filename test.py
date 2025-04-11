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
condition = df[['champ1', 'champ2', 'champ3']].apply(lambda x: x.str.strip() == '', axis=1).all(axis=1)

{
  "size": 0,
  "query": {
    "range": {
      "created_at": {
        "gte": "2025-04-09",
        "lt": "2025-04-10"
      }
    }
  },
  "aggs": {
    "duplicate_uuids": {
      "terms": {
        "field": "uuid.keyword",
        "size": 100000,
        "min_doc_count": 2
      }
    }
  }
}


from elasticsearch import Elasticsearch

# --- Config ---
ES_HOST = 'http://localhost:9200'
INDEX_NAME = 'your_index_name'
UUID_FIELD = 'uuid.keyword'

es = Elasticsearch(ES_HOST)

def count_duplicate_uuids_composite(index, uuid_field):
    duplicate_count = 0
    after_key = None

    while True:
        agg_query = {
            "size": 0,
            "aggs": {
                "duplicate_uuids": {
                    "composite": {
                        "size": 1000,
                        "sources": [
                            {"uuid": {"terms": {"field": uuid_field}}}
                        ],
                        **({"after": after_key} if after_key else {})
                    },
                    "aggs": {
                        "uuid_count": {
                            "value_count": {"field": uuid_field}
                        }
                    }
                }
            }
        }

        response = es.search(index=index, body=agg_query)
        buckets = response['aggregations']['duplicate_uuids']['buckets']
        
        for bucket in buckets:
            if bucket['doc_count'] > 1:
                duplicate_count += 1

        if 'after_key' in response['aggregations']['duplicate_uuids']:
            after_key = response['aggregations']['duplicate_uuids']['after_key']
        else:
            break

    return duplicate_count

# --- Run ---
if __name__ == '__main__':
    count = count_duplicate_uuids_composite(INDEX_NAME, UUID_FIELD)
    print(f"Total duplicated UUIDs: {count}")




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
