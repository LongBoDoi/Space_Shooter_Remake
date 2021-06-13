class Animation:
    def __init__(self, texture, x, y, w, h, row, col, speed):
        self.current_speed = 0.0
        self.speed = speed
        self.frames = []
        self.texture = texture.__copy__()
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.row = row
        self.col = col
        self.real_x = 0
        self.real_y = 0
        for i in range(row):
            for j in range(col):
                self.frames.append((x + j * w, y + (row - i - 1) * h, w, h))
        x1, y1, w1, h1 = self.frames[0]
        self.texture.set_rect(x1, y1, w1, h1)

    def is_end(self):
        return self.current_speed + self.speed >= len(self.frames)

    def update(self):
        if self.speed > 0:
            self.current_speed += self.speed
            size = len(self.frames)
            if self.current_speed >= size:
                self.current_speed -= size
            x, y, w, h = self.frames[int(self.current_speed)]
            self.texture.set_rect(x, y, w, h)

    def render(self, game_play):
        self.texture.image.size_hint = self.width / 1200, self.height / 800
        self.texture.image.pos_hint = {"right": self.x, "top": self.y}
        game_play.add_widget(self.texture.image)

    def free(self, game_play):
        self.texture.free(game_play)

    def __copy__(self):
        return Animation(self.texture, self.x, self.y, self.width, self.height, self.row, self.col,
                         self.speed)
