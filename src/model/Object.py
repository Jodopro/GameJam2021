class Object:
    position = [0.0,0.0]
    speed = [0.0,0.0]


    def draw(self):
        pass

    def update(self, delta_t):
        self.position += delta_t * self.speed