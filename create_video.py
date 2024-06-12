from manim import *

class Scene1(Scene):
    def construct(self):
        text = Text("Scene 1: Example Description")
        self.play(Write(text))
        self.wait(2)

if __name__ == "__main__":
    from manim import config
    config.background_color = WHITE
    scene = Scene1()
    scene.render()
