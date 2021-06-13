class Object:
    def __init__(self, x, y, w, h, animation, game_play):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.dx = 0
        self.dy = 0
        self.active = True
        self.animation = animation.__copy__()
        self.animation.real_x = self.x
        self.animation.real_y = self.y
        self.render(game_play)
        game_play.entities.append(self)

    def set_x(self, x):
        self.x = x
        self.animation.texture.image.pos_hint = {"right": self.x, "top": self.y}

    def set_y(self, y):
        self.y = y
        self.animation.texture.image.pos_hint = {"right": self.x, "top": self.y}

    def update(self, game_play):
        if self.dx != 0:
            self.set_x(self.x + self.dx)
        if self.dy != 0:
            self.set_y(self.y + self.dy)

        if not self.active:
            self.animation.free(game_play)
            game_play.entities.remove(self)

    def render(self, game_play):
        self.animation.texture.image.size_hint = self.width, self.height
        self.animation.texture.image.pos_hint = {"right": self.x, "top": self.y}
        game_play.add_widget(self.animation.texture.image)

    def info(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.width) + " " + str(self.height)

    def collides_with(self, object_2, offset_x, offset_y):
        if object_2.x <= self.x + offset_x <= object_2.x + object_2.width and \
                object_2.y <= self.y + offset_y <= object_2.y + object_2.height:
            return True
        if self.x + offset_x <= object_2.x <= self.x + offset_x + self.width and \
                self.y + offset_y <= object_2.y <= self.y + offset_y + self.height:
            return True
        if object_2.x <= self.x + offset_x + self.width <= object_2.x + object_2.width and \
                object_2.y <= self.y + offset_y <= object_2.y + object_2.height:
            return True
        if self.x + offset_x <= object_2.x + object_2.width <= self.x + offset_x + self.width and \
                self.y + offset_y <= object_2.y <= self.y + offset_y + self.height:
            return True
        if self.x + offset_x <= object_2.x <= self.x + offset_x + self.width and \
                self.y + offset_y <= object_2.y + object_2.height <= self.y + offset_y + self.height:
            return True
        if object_2.x <= self.x + offset_x <= object_2.x + object_2.width and \
                object_2.y <= self.y + offset_y + self.height <= object_2.y + object_2.height:
            return True
        return False
