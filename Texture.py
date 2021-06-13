from kivy.uix.image import Image


class Texture:
    def __init__(self, source, x, y, w, h):
        self.image = Image(source=source, allow_stretch=True, keep_ratio=False)
        self.source_img = Image(source=source, allow_stretch=True, keep_ratio=False)
        self.source = source
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        if x != -1:
            new_image = self.image.texture.get_region(x, y, w, h)
            self.image = Image(texture=new_image, allow_stretch=True, keep_ratio=False)

    def set_rect(self, x, y, w, h):
        self.image.texture = self.source_img.texture.get_region(x, y, w, h)

    def set_pos(self, x, y):
        self.image.pos_hint = {"right": x, "top": y}

    def set_size(self, w, h):
        self.image.size_hint = w, h

    def render(self, game_play, x, y, w, h):
        self.image.size_hint = w, h
        self.image.pos_hint = {"right": x, "top": y}
        game_play.add_widget(self.image)

    def contains_pos(self, x, y):
        return self.x <= x <= self.x + self.w and self.y <= y <= self.y + self.h

    def free(self, game_play):
        game_play.remove_widget(self.image)

    def __copy__(self):
        return Texture(self.source, self.x, self.y, self.w, self.h)
