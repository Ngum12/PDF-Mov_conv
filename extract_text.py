import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

if __name__ == "__main__":
    pdf_path = "book.pdf"
    text = extract_text_from_pdf(pdf_path)
    with open("book_text.txt", "w") as f:
        f.write(text)
