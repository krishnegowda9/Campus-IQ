import re
import pymupdf


def extract_pdf_text(pdf_path):
    """
    Extract text from every page of a PDF.
    """

    pdf = pymupdf.open(pdf_path)

    all_text = []

    for page in pdf:
        text = page.get_text("text")
        all_text.append(text)

    pdf.close()

    return "\n".join(all_text)


def split_into_chunks(text):
    """
    Split the document into question-and-answer chunks.
    """

    # Fix question numbers broken by PDF extraction.
    # Example:
    # 1
    # 0. What is Copy-on-Write?
    #
    # becomes:
    # 10. What is Copy-on-Write?

    text = re.sub(
        r"(?m)^(\d+)\s*\n\s*(\d+\.)",
        r"\1\2",
        text
    )

    # Find question numbers at the beginning of a line.
    pattern = r"(?m)(?=^\d+\.\s)"

    chunks = re.split(pattern, text)

    # Remove empty chunks and extra whitespace.
    chunks = [
        chunk.strip()
        for chunk in chunks
        if chunk.strip()
    ]

    # Remove the document title.
    # The first chunk is not a numbered question.
    if chunks and not re.match(r"^\d+\.\s", chunks[0]):
        chunks = chunks[1:]

    return chunks


if __name__ == "__main__":

    # Location of our PDF
    pdf_path = "data/pdfs/Docker 1.pdf"

    print("Reading PDF...")

    # Step 1: Extract PDF text
    document_text = extract_pdf_text(pdf_path)

    print("PDF text extracted successfully!")

    # Step 2: Split text into chunks
    chunks = split_into_chunks(document_text)

    print("Number of chunks:", len(chunks))

    # Step 3: Display chunks
    for i, chunk in enumerate(chunks, start=1):

        print("\n" + "=" * 60)
        print(f"CHUNK {i}")
        print("=" * 60)

        print(chunk)
