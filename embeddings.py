import openai
from dotenv import load_dotenv
import os
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the strings
text1 = "hallo, mein Name ist Markus"
text2 = "hallo, mein Name ist Markus"
text3 = "asdasdas"

# Create embeddings for the strings
response1 = openai.Embedding.create(input=text1, model="text-embedding-ada-002")
response2 = openai.Embedding.create(input=text2, model="text-embedding-ada-002")
response3 = openai.Embedding.create(input=text3, model="text-embedding-ada-002")

embedding1 = response1['data'][0]['embedding']
embedding2 = response2['data'][0]['embedding']
embedding3 = response3['data'][0]['embedding']

# Compute cosine similarity
similarity12 = cosine_similarity([embedding1], [embedding2])
similarity13 = cosine_similarity([embedding1], [embedding3])

print(f"Similarity between text 1 and text 2: {similarity12[0][0]}")
print(f"Similarity between text 1 and text 3: {similarity13[0][0]}")