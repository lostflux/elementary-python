G = 6.67384e-11 #Gravitational constant

class System:
    def _init_(self, body_list):
        self.body_list = body_list

    def compute_acceleration(self):
        dx = self.body_list[0].x - self.body_list[1].x  # x-distance between earth and moon
        dy = self.body_list[0].y - self.body_list[1].y  # y-distance between earth and moon.
        dis = self.body_list[0].distance(self.body_list[1]) #distance between earth and moon
        a = G * self.body_list[0].mass / (dis * dis) #acceleration
        ax = a * dx / dis #aceleration in x direction
        ay = a * dy / dis #acceleration in y direction
        return (ax, ay)

    def update(self, timestep):
        (ax, ay) = self.compute_acceleration()
        self.body_list[1].update_velocity(ax, ay, timestep)  #updating moon's velocity using the acceleration
        self.body_list[1].update_position(timestep)  # updating moon's position


    def draw(self, cx, cy, pixels_per_meter):
        for i in range(len(self.body_list)):
            self.body_list[i].draw(cx, cy, pixels_per_meter)