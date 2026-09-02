from embeddings.embedding_model import generate_embedding
from database.chroma_store import search_documents


def retrieve_documents(question, n_results=3):
    """
    Search ChromaDB for documents relevant to the user's question.
    """

    print("\nUser question:")
    print(question)

    # Convert the question into a vector
    question_embedding = generate_embedding(question)

    print("\nQuestion embedding generated!")
    print("Embedding dimensions:", len(question_embedding))

    # Search ChromaDB
    results = search_documents(
        query_embedding=question_embedding,
        n_results=n_results
    )

    return results


if __name__ == "__main__":

    question = "What is the difference between Docker and a virtual machine?"

    results = retrieve_documents(question, n_results=3)

    print("\n========================================")
    print("RETRIEVED DOCUMENTS")
    print("========================================")

    documents = results.get("documents", [[]])[0]

    for index, document in enumerate(documents, start=1):

        print(f"\nRESULT {index}")
        print("----------------------------------------")
        print(document)
