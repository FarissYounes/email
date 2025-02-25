import os
from langchain_community.document_loaders import ReadTheDocsLoader
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pathlib import Path

load_dotenv()

def ingest_docs() -> None :

    path = Path("langchain-docs/fastapi.tiangolo.com/fr")
    # path = "D:\LLM_RAG\demo\langchain-docs\\fastapi.tiangolo.com\\fr"

    print("__Loading__")
    loader = ReadTheDocsLoader(
        path = str(path),
        custom_html_tag = ("main", {"class": "md-main"}),
        encoding="utf8",
    )
    
    raw_documents = loader.load()
    print("Number of Documents generated : " + str(len(raw_documents)))
    print("content : " + str(raw_documents[0].page_content) + "\n" + "metadonnees : " + str(raw_documents[0].metadata))
    
    print("__Splitting__")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", ""]
    )
    texts = text_splitter.split_documents(documents = raw_documents)
    print("Number of splits generated : " + str(len(texts)))

    for doc in texts :
        old_path = doc.metadata["source"]
        new_url = old_path.replace("langchain-docs", "http://")
        doc.metadata.update({"source" : new_url})

    embeddings = HuggingFaceInferenceAPIEmbeddings(
        api_key = os.environ.get("INFERENCE_API_KEY"), model_name = "sentence-transformers/all-MiniLM-l6-v2"
    )
    print
    print("__Storing__")
    PineconeVectorStore.from_documents(texts, embeddings, index_name = os.environ["INDEX_NAME"])
    print("Done")

if __name__== "__main__":
    ingest_docs()
