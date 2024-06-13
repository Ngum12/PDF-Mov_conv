# create_video.py

from manim import *

class BookAnimation(Scene):
    def construct(self):
        with open("processed_content.txt", "r") as file:
            processed_content = file.readlines()

        for page_content in processed_content:
            text = page_content.split("Text: ")[1].split("Images: ")[0].strip()
            images = page_content.split("Images: ")[1].strip().split(", ")

            # Display text
            self.play(Write(Text(text)))

            # Display images/animations
            for img_path in images:
                img = ImageMobject(img_path)
                self.play(FadeIn(img))

            self.wait(1)  # Adjust as needed for timing between pages

if __name__ == "__main__":
    scene = BookAnimation()
    scene.render()

