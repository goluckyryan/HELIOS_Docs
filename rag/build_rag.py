#!/usr/bin/env python3
"""
Build RAG index from all *.md files in ~/HELIOS_MD/ (excluding rag/ subdir and INDEX.md).
Run this whenever any md file is added or updated.
"""

import os
import re
import chromadb
from chromadb.utils import embedding_functions
from pathlib import Path

MD_DIR = Path.home() / "HELIOS_MD"
RAG_DIR = MD_DIR / "rag"
CHROMA_DIR = RAG_DIR / "chroma_db"

CHUNK_SIZE = 300      # words per chunk (smaller than PDF — MD is denser)
CHUNK_OVERLAP = 40

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

EXCLUDE = {"INDEX.md"}  # don't index the index itself

def chunk_text(text: str, source: str, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    words = text.split()
    chunks = []
    i = 0
    chunk_idx = 0
    while i < len(words):
        chunk_words = words[i:i + chunk_size]
        chunks.append({
            'text': ' '.join(chunk_words),
            'source': source,
            'chunk_idx': chunk_idx,
            'word_start': i,
            'word_end': i + len(chunk_words),
        })
        chunk_idx += 1
        i += chunk_size - overlap
    return chunks

def build_index():
    CHROMA_DIR.mkdir(parents=True, exist_ok=True)

    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL
    )

    try:
        client.delete_collection("helios_md")
        print("Deleted existing collection.")
    except Exception:
        pass

    collection = client.create_collection(
        name="helios_md",
        embedding_function=ef,
        metadata={"hnsw:space": "cosine"}
    )

    md_files = [
        f for f in MD_DIR.glob("*.md")
        if f.name not in EXCLUDE and f.parent == MD_DIR
    ]

    if not md_files:
        print("No MD files found in", MD_DIR)
        return

    all_chunks = []

    for md in sorted(md_files):
        print(f"\nProcessing: {md.name}")
        text = md.read_text(encoding="utf-8")
        if not text.strip():
            print(f"  WARNING: empty file {md.name}")
            continue
        print(f"  {len(text.split())} words")
        chunks = chunk_text(text, md.name)
        print(f"  {len(chunks)} chunks")
        all_chunks.extend(chunks)

    if not all_chunks:
        print("No chunks to index!")
        return

    batch_size = 50
    for i in range(0, len(all_chunks), batch_size):
        batch = all_chunks[i:i + batch_size]
        collection.add(
            ids=[f"{c['source']}::chunk{c['chunk_idx']}" for c in batch],
            documents=[c['text'] for c in batch],
            metadatas=[{
                'source': c['source'],
                'chunk_idx': c['chunk_idx'],
                'word_start': c['word_start'],
                'word_end': c['word_end'],
            } for c in batch],
        )
        print(f"  Indexed batch {i//batch_size + 1}/{(len(all_chunks)-1)//batch_size + 1}")

    print(f"\n✅ Done! Indexed {len(all_chunks)} chunks from {len(md_files)} files.")
    print(f"   DB: {CHROMA_DIR}")

if __name__ == "__main__":
    build_index()
