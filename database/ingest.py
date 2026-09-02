from pathlib import Path

from embeddings.embed_documents import create_document_embeddings
from database.chroma_store import store_documents


# Folder containing all PDF files
PDF_FOLDER = Path("data/pdfs")


def ingest_all_pdfs():
    """
    Ingest every PDF inside data/pdfs/.

    PDF files
        ↓
    Text extraction
        ↓
    Chunking
        ↓
    Hugging Face embeddings
        ↓
    ChromaDB
    """

    print("\n========================================")
    print("       CAMPUS-IQ DOCUMENT INGESTION")
    print("========================================")

    # Check whether the PDF folder exists
    if not PDF_FOLDER.exists():
        print(f"\n❌ Folder not found: {PDF_FOLDER}")
        return

    # Find all PDF files
    pdf_files = list(PDF_FOLDER.glob("*.pdf"))

    if not pdf_files:
        print("\n❌ No PDF files found.")
        print(f"Please add PDF files to: {PDF_FOLDER}")
        return

    print(f"\nFound {len(pdf_files)} PDF file(s).")

    # Process every PDF
    for index, pdf_path in enumerate(pdf_files, start=1):

        print("\n========================================")
        print(f"Processing PDF {index}/{len(pdf_files)}")
        print("========================================")

        print(f"File: {pdf_path.name}")

        try:
            # Generate chunks and embeddings
            chunks, embeddings = create_document_embeddings(
                str(pdf_path)
            )

            # Store in ChromaDB
            store_documents(
                chunks,
                embeddings
            )

            print(f"✅ Successfully stored: {pdf_path.name}")

        except Exception as e:

            print(f"❌ Failed to process: {pdf_path.name}")
            print(f"Error: {e}")

    print("\n========================================")
    print("       INGESTION FINISHED")
    print("========================================")


if __name__ == "__main__":
    ingest_all_pdfs()
