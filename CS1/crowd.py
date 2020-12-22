from face import Face

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
x = 0
y = 0


class Crowd:
    def __init__(self, number_of_faces):
        global x, y
        self.faces = []
        for i in range(number_of_faces):
            x += 5 + x / number_of_faces
            if x >= WINDOW_WIDTH:
                x -= WINDOW_WIDTH
                y += y / number_of_faces
            self.faces.append(Face(x, y, 20))
