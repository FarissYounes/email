1. Data Collection (Shell Script)
	- Parse the homepage to extract content.
	- Retrieve all href links from the page.
	- Download the HTML files corresponding to each extracted link.
	- Rename the downloaded files based on their titles from the wiki documentation.
2. Preprocessing
	- Remove unnecessary elements such as headers and footers.
	- Clean up tags and format the text.
	- Define an appropriate chunk size with overlap for better context retention.
	- Split documents into smaller, manageable chunks.
	- Generate embeddings for each chunk.
	- Store the processed chunks in a vector database.

RAG :

3. Retrieval
	- Convert the user’s query into an embedding.
	- Use cosine similarity to find the most relevant document chunks.
	- Combine retrieved chunks with the initial query and developer prompt to create context.
4. Generation
	- Send the constructed context to the LLM for response generation.


Requirements :
	- Embedding model	: Pending
	- LLM Model 		: Successfully tested
