import spacy

def process_text(text_path):
    nlp = spacy.load("en_core_web_sm")
    with open(text_path, "r") as f:
        text = f.read()
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    return sentences

if __name__ == "__main__":
    text_path = "book_text.txt"
    sentences = process_text(text_path)
    with open("sentences.txt", "w") as f:
        for sentence in sentences:
            f.write(sentence + "\n")
