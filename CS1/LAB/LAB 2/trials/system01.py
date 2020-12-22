import math
from body import Body


G = 6.67384e-11

class System:
    def __init__(self, list_of_bodies):
        self.bodies = list_of_bodies

        # for body_details in list_of_bodies:
        #     mass = body_details[0]
        #     x = body_details[1]
        #     y = body_details[2]
        #     vx = body_details[3]
        #     vy = body_details[4]
        #     pixel_radius = body_details[5]
        #     r = body_details[6]
        #     g = body_details[7]
        #     b = body_details[8]
        #     self.bodies.append(Body(mass, x, y, vx, vy, pixel_radius, r, g, b))

    def draw(self, half_width, half_height, scale):
        for body in self.bodies:
            body.draw(half_width, half_height, scale)

    def update(self, time_step):
        x_operator = y_operator = 1
        for body in self.bodies:
            for other_body in self.bodies:
                if self.bodies.index(body) == self.bodies.index(other_body):
                    continue
                else:
                    dx = body.x - other_body.x
                    dy = body.y - other_body.y

                    distance = self.distances[f"{self.bodies.index(body)} and {self.bodies.index(other_body)}"]
                    if abs(dy) >= distance:
                        body.x = dx = 0
                        if dy > 0:
                            body.y = dy = distance
                            y_operator = -1
                        elif dy < 0:
                            body.y = dy = 0 - distance
                            y_operator = 1
                        # y_operator = 0 - y_operator
                        # print("y inverted")
                    if abs(dx) >= distance:
                        body.y = dy = 0
                        if dx > 0:
                            body.x = dx = distance
                            dx = distance
                            x_operator = -1
                        elif dx < 0:
                            body.x = dx = 0 - distance
                            x_operator = 1
                        # x_operator = 0 - x_operator
                        # print("x inverted")
                    # print(distance)
                    # print(ax, ay)
                    # distance = math.sqrt((dx ** 2) + (dy ** 2))
                    acceleration = G * other_body.mass / distance ** 2
                    ax = acceleration * dx / distance
                    ay = acceleration * dy / distance
                    # print(f"dx: {dx}, dy: {dy}, ax: {ax}, ay: {ay}")
                    # body.update(ax, ay, time_step)
                    displacement = body.update(ax, ay, time_step)
                    # print(displacement)
                    body.x += x_operator * displacement[0] * time_step
                    body.y += y_operator * displacement[1] * time_step
                    body.vx += x_operator * ax * time_step
                    body.vy += y_operator * ay * time_step
