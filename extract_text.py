import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

if __name__ == "__main__":
    pdf_path = "One story.pdf"  # Replace this with the name of your uploaded PDF file
    text = extract_text_from_pdf(pdf_path)
    
    # Save extracted text to a file
    with open("extracted_text.txt", "w") as file:
        file.write(text)

