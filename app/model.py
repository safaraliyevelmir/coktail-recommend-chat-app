import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

index = faiss.read_index("cocktails_faiss.index") 
texts = np.load("cocktails_texts.npy", allow_pickle=True)

model = SentenceTransformer("sentence-transformers/multi-qa-mpnet-base-dot-v1")

def search_cocktail(query: str, top_k: int = 1):
    query_emb = model.encode(query, convert_to_numpy=True).reshape(1, -1)
    
    _, indices = index.search(query_emb, top_k)
    
    results = [{"name": texts[i][0], "description": texts[i][1]} for i in indices[0]]
    
    return results



def generate_text(name, description):
    return f"Name: {name}\nDescription: {description}"