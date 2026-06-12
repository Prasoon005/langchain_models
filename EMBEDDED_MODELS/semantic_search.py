from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from pathlib import Path
from sklearn.metrics.pairwise import cosine_similarity

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

embedding_model = OpenAIEmbeddings(
    model='text-embedding-3-large',
    dimensions=300
)

embedding_doc = [
    "Virat Kohli is an Indian cricketer who is famous for his batting.",

    "MS Dhoni is a former Indian cricket captain whose jersey number is 7.",

    "Rohit Sharma is known as the Hitman of Indian cricket.",

    "Sachin Tendulkar is called the God of Cricket.",

    "Jasprit Bumrah is one of the best fast bowlers in the world.",

    "The capital of India is New Delhi.",

    "Mumbai is known as the financial capital of India.",

    "Python is a popular programming language used in AI and Machine Learning."
]

embedding_query = "who is Virat Kohli"

# Generate embeddings
doc_embeddings = embedding_model.embed_documents(embedding_doc)

query_embedding = embedding_model.embed_query(embedding_query)

# Calculate similarity scores
scores = cosine_similarity(
    [query_embedding],
    doc_embeddings
)[0]

# Attach index with score
indexed_score = list(enumerate(scores))

# Sort by similarity score (highest first)
sorted_score = sorted(
    indexed_score,
    key=lambda x: x[1],
    reverse=True
)

# Best matching document
index, score = sorted_score[0]

print("Query:")
print(embedding_query)

print("\nMost Similar Document:")
print(embedding_doc[index])

print("\nSimilarity Score:")
print(score)