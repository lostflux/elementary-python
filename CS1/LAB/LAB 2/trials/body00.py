class Body:
    def _init_(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r
        self.g = g
        self.b = b
        self.pixel_radius = pixel_radius

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        s = sqrt(dx * dx + dy * dy)
        return s

    def update_position(self, timestep):
        self.x += self.vx * timestep
        self.y += self.vy * timestep

    def update_velocity(self, ax, ay, timestep):
        self.vx += ax * timestep
        self.vy += ay * timestep

    def draw(self, cx, cy, pixels_per_meter):
        set_fill_color(self.r, self.g, self.b)
        draw_circle(cx + self.x * pixels_per_meter, cy + self.y * pixels_per_meter, self.pixel_radius)