curl -X PUT "localhost:9200/vector_store" -H 'Content-Type: application/json' -d '
{
  "mappings": {
    "properties": {
      "page_content": {
        "type": "text"
      },
      "metadata": {
        "type": "object"
      },
      "embedding": {
        "type": "dense_vector",
        "dims": 384
      }
    }
  }
}'
