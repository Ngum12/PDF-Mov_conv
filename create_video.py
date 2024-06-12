from manim import *

class Scene1(Scene):
    def construct(self):
        # Read processed text from file
        with open("processed_text.txt", "r") as file:
            text = file.read()

        # Create a Text object from the extracted text
        text_object = Text(text[:200])  # Display the first 200 characters for brevity
        
        # Display the text
        self.play(Write(text_object))
        self.wait(2)
        
        # Fade out the text
        self.play(FadeOut(text_object))

# Run the scene
if __name__ == "__main__":
    from manim import *
    config.media_width = "100%"
    Scene1().render()

