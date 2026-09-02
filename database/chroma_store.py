import os
import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="campus_iq_documents"
)

def store_documents(chunks, embeddings):
    """
    Store document chunks and their embeddings in ChromaDB.
    """
    ids = [
        f"doc_{i}"
        for i in range(len(chunks))
    ]

    collection.upsert(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

    print("\n========================================")
    print("Documents stored in ChromaDB!")
    print("========================================")

    print("Number of documents:", collection.count())


def search_documents(query_embedding, n_results=3):
    """
    Search ChromaDB using an embedding.
    """
    doc_count = collection.count()
    print(f"\n[ChromaDB Status] Total documents in collection: {doc_count}")

    if doc_count == 0:
        print("[WARNING] ChromaDB collection 'campus_iq_documents' is EMPTY inside the container!")
        return {"documents": [[]]}

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results


if __name__ == "__main__":
    print("ChromaDB initialized successfully!")
    print("Collection name:", collection.name)
    print("Documents currently stored:", collection.count())