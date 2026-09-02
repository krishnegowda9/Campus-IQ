from chunker.text_chunker import extract_pdf_text, split_into_chunks
from embeddings.embedding_model import generate_embedding


PDF_PATH = "data/pdfs/Docker 1.pdf"


def create_document_embeddings(pdf_path):
    """
    Extract the PDF, split it into chunks,
    and generate an embedding for every chunk.
    """

    print("\nReading PDF...")

    # 1. Extract text
    document_text = extract_pdf_text(pdf_path)

    print("PDF text extracted successfully!")

    # 2. Create chunks
    chunks = split_into_chunks(document_text)

    print(f"Number of chunks: {len(chunks)}")

    # 3. Generate embeddings
    embeddings = []

    for index, chunk in enumerate(chunks, start=1):

        print(f"\nGenerating embedding {index}/{len(chunks)}...")

        embedding = generate_embedding(chunk)

        embeddings.append(embedding)

    print("\n========================================")
    print("Embedding generation completed!")
    print("========================================")

    print("Number of chunks:", len(chunks))
    print("Number of embeddings:", len(embeddings))
    print("Embedding dimensions:", len(embeddings[0]))

    return chunks, embeddings


if __name__ == "__main__":

    chunks, embeddings = create_document_embeddings(PDF_PATH)

    print("\nFirst chunk:")
    print(chunks[0])

    print("\nFirst embedding - first 10 values:")
    print(embeddings[0][:10])
