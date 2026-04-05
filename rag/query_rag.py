#!/usr/bin/env python3
"""
Query the HELIOS_MD RAG index.
Usage: python3 query_rag.py "your question" [--n 5]
"""

import argparse
import chromadb
from chromadb.utils import embedding_functions
from pathlib import Path

CHROMA_DIR = Path.home() / "HELIOS_MD" / "rag" / "chroma_db"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

def query(question: str, n_results: int = 5):
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL
    )
    collection = client.get_collection("helios_md", embedding_function=ef)

    results = collection.query(
        query_texts=[question],
        n_results=n_results,
        include=["documents", "metadatas", "distances"]
    )

    docs = results['documents'][0]
    metas = results['metadatas'][0]
    dists = results['distances'][0]

    print(f"\n🔍 Query: {question}\n")
    print("=" * 70)

    for i, (doc, meta, dist) in enumerate(zip(docs, metas, dists)):
        similarity = 1 - dist
        print(f"\n[{i+1}] {meta['source']} | chunk {meta['chunk_idx']} | similarity: {similarity:.3f}")
        print("-" * 70)
        preview = doc[:400].strip()
        if len(doc) > 400:
            preview += "..."
        print(preview)

    print("\n" + "=" * 70)

def main():
    parser = argparse.ArgumentParser(description="Query HELIOS_MD RAG index")
    parser.add_argument("question", nargs="+", help="Question to ask")
    parser.add_argument("--n", type=int, default=5, help="Number of results (default: 5)")
    args = parser.parse_args()
    query(" ".join(args.question), n_results=args.n)

if __name__ == "__main__":
    main()
