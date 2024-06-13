# process_text.py

from PIL import Image, ImageDraw
import random

def generate_colored_image(width, height, output_path):
    # Create a new image with RGB mode
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    # Generate random colors and draw shapes (example: rectangles)
    num_rectangles = random.randint(3, 6)
    for _ in range(num_rectangles):
        x1 = random.randint(0, width - 50)
        y1 = random.randint(0, height - 50)
        x2 = x1 + random.randint(20, 50)
        y2 = y1 + random.randint(20, 50)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.rectangle([x1, y1, x2, y2], fill=color)

    # Save the image
    image.save(output_path)

    return output_path

def process_content_for_animation(extracted_content):
    # Process content here as needed for animations
    processed_content = []
    for page_content in extracted_content:
        text = page_content.strip()  # Assuming text is read from extracted_text.txt
        generated_images = []

        # Generate 2-4 images per page
        for _ in range(random.randint(2, 4)):
            width = random.randint(200, 400)
            height = random.randint(150, 300)
            img_path = generate_colored_image(width, height, f"generated_image_{random.randint(1000, 9999)}.png")
            generated_images.append(img_path)

        processed_content.append((text, generated_images))

    return processed_content

if __name__ == "__main__":
    # Example usage
    with open("extracted_text.txt", "r") as file:
        extracted_content = file.readlines()

    processed_content = process_content_for_animation(extracted_content)
    
    with open("processed_content.txt", "w") as file:
        for content in processed_content:
            text = content[0]
            images = ", ".join(content[1])
            file.write(f"Text: {text}\tImages: {images}\n")

