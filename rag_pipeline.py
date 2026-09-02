from database.retriever import retrieve_documents
from generator.text_generator import generate_answer


def ask_rag(question):
    """
    Complete RAG pipeline.

    Returns:
        answer
        sources
    """

    if not question.strip():
        return (
            "Please enter a question.",
            "No sources available."
        )

    print("\n========================================")
    print("RAG PIPELINE")
    print("========================================")

    # ========================================
    # STEP 1: RETRIEVAL
    # ========================================

    print("\n1. Searching ChromaDB...")

    results = retrieve_documents(
        question,
        n_results=3
    )

    documents = results.get("documents", [[]])[0]

    if not documents:
        return (
            "I could not find relevant information in the documents.",
            "No relevant documents found."
        )

    print(f"Found {len(documents)} relevant documents.")

    # ========================================
    # STEP 2: BUILD CONTEXT
    # ========================================

    context = "\n\n".join(documents)

    print("\n2. Context prepared.")

    # ========================================
    # STEP 3: GENERATION
    # ========================================

    print("\n3. Generating answer with Hugging Face...")

    answer = generate_answer(
        question,
        context
    )

    print("\n4. Answer generated successfully!")

    # ========================================
    # STEP 4: PREPARE SOURCES
    # ========================================

    sources = "### Retrieved Sources\n\n"

    for index, document in enumerate(documents, start=1):

        sources += f"**Source {index}**\n\n"
        sources += document
        sources += "\n\n---\n\n"

    return answer, sources
