import pymupdf

pdf_path = "data/pdfs/Docker 1.pdf"

pdf = pymupdf.open(pdf_path)

print("PDF opened successfully!")
print("Number of pages:", len(pdf))

# Read every page
for page_number, page in enumerate(pdf, start=1):

    text = page.get_text()

    print("\n" + "=" * 60)
    print(f"PAGE {page_number}")
    print("=" * 60)

    print(text)

pdf.close()
