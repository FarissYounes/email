import torch
from transformers import AutoTokenizer, AutoModel
import faiss
import numpy as np
from langchain.docstore.document import Document  # Import du type Document LangChain

# Charger le modèle et le tokenizer "bge-base"
model_name = "chemin/vers/bge-base"  # Remplacez par le chemin ou l’ID du modèle
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def embed_text(document: Document):
    """
    Prend en paramètre un objet Document (LangChain),
    extrait le contenu textuel et renvoie l'embedding normalisé.
    """
    text = document.page_content  # Extraction du contenu du document
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    # Utilisation du token [CLS] pour l'embedding
    embedding = outputs.last_hidden_state[:, 0, :].numpy()
    # Normalisation pour utiliser la similarité cosinus avec IndexFlatIP
    embedding = embedding / np.linalg.norm(embedding, axis=1, keepdims=True)
    return embedding

# Création d'une liste de documents LangChain
documents = [
    Document(page_content="Texte du document 1", metadata={"id": 1}),
    Document(page_content="Contenu du document 2", metadata={"id": 2}),
    Document(page_content="Autre exemple de document", metadata={"id": 3})
]

# Calcul des embeddings pour chaque document
document_embeddings = np.vstack([embed_text(doc) for doc in documents])

# Définir la dimension de l’embedding
embedding_dim = document_embeddings.shape[1]

# Créer un index Faiss basé sur le produit scalaire (pour la similarité cosinus si normalisé)
index = faiss.IndexFlatIP(embedding_dim)
# Ajouter les embeddings à l'index
index.add(document_embeddings)

print("Ingestion terminée, {} documents indexés.".format(index.ntotal))

# Partie Retrieval : recherche des documents similaires à une requête

def retrieve(query: str, k: int = 5):
    """
    Encode la requête, effectue une recherche dans l'index Faiss
    et renvoie les indices des k documents les plus proches ainsi que leurs scores.
    """
    # Encoder la requête directement avec le tokenizer et le modèle
    inputs = tokenizer(query, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    query_embedding = outputs.last_hidden_state[:, 0, :].numpy()
    query_embedding = query_embedding / np.linalg.norm(query_embedding, axis=1, keepdims=True)
    scores, indices = index.search(query_embedding, k)
    return indices[0], scores[0]

# Exemple d'utilisation de la fonction de récupération
query = "Votre requête ici"
doc_indices, similarity_scores = retrieve(query, k=2)
print("Documents récupérés :")
for idx, score in zip(doc_indices, similarity_scores):
    print(f"Document ID {documents[idx].metadata.get('id')} - Score: {score:.4f}")
    print("Contenu :", documents[idx].page_content)

\\\\\\\\\\\\\\\\\\\\\\\\\\\\

from elasticsearch import Elasticsearch

# Connexion à l'instance Elasticsearch
es = Elasticsearch("http://localhost:9200")  # Change l'URL si nécessaire

# Définir le mapping de l'index
index_name = "mon_index"
mapping = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 1
    },
    "mappings": {
        "properties": {
            "titre": {"type": "text"},
            "description": {"type": "text"},
            "date_creation": {"type": "date"}
        }
    }
}

# Vérifier si l'index existe déjà
if not es.indices.exists(index=index_name):
    # Créer l'index avec le mapping
    es.indices.create(index=index_name, body=mapping)
    print(f"Index '{index_name}' créé avec succès.")
else:
    print(f"L'index '{index_name}' existe déjà.")

