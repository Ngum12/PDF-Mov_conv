# extract_text.py

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    extracted_text = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        extracted_text.append(text)

    return extracted_text

if __name__ == "__main__":
    pdf_path = "One story.pdf"  # Update this path
    extracted_text = extract_text_from_pdf(pdf_path)
    
    with open("extracted_text.txt", "w") as file:
        for text in extracted_text:
            file.write(text + "\n")

