Mini-PoC Step 1: Try out embedding a single sentence
	•	Write a tiny Python script or use a Jupyter notebook cell that loads the embedding model and generates an embedding for one sentence like:
“Met John, Arsenal fan.”
	•	Print out the resulting vector (just numbers!) and marvel at the AI magic

Mini-PoC Step 2: Embed a small list of notes
	•	Expand your script to embed 3-5 notes about your connections
	•	Store these vectors in a simple Python list or dict (no DB yet)
	•	Print out the embeddings with their notes side by side

Mini-PoC Step 3: Simple similarity search with cosine similarity
	•	Given a new query sentence like “Who likes football?”, embed it
	•	Write a simple function to compute cosine similarity between this query vector and your stored note vectors
	•	Print the top matching note with similarity scores

Mini-PoC Step 4: Wrap it into a function
	•	Package the embedding + search code into reusable functions like embed_text(text) and search_notes(query, notes)
	•	Try different queries and see what pops up

Mini-PoC Step 5: Add a basic text input UI (optional)
	•	Use a very simple Python UI tool like Streamlit or even a command line prompt to input queries interactively
	•	See results live without changing code
