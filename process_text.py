def process_text(file_path):
    with open(file_path, "r") as file:
        text = file.read()
    # Add any text processing here if needed
    return text

if __name__ == "__main__":
    text = process_text("extracted_text.txt")
    # Save processed text to a file (optional)
    with open("processed_text.txt", "w") as file:
        file.write(text)

