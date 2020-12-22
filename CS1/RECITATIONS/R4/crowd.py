from face import Face

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
x = 20
y = 20

class Crowd:
    def __init__(self, number_of_faces):
        global x, y
        self.faces = []
        for i in range(number_of_faces):
            x += (60 + x / number_of_faces)
            if x >= WINDOW_WIDTH - x / number_of_faces:
                x -= WINDOW_WIDTH - x / number_of_faces
                y += 80 + y / number_of_faces
            self.faces.append(Face(x, y, 20))

    def lookat(self, lx, ly):
        for face in self.faces:
            face.lookat(lx, ly)

    def draw(self):
        for face in self.faces:
            face.draw()
