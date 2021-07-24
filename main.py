import random

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

from Boss import Boss
from Constants import background_img, life_bar_img, overheat_frame_texture, overheat_bar_texture
from Player import Player
from Rock import Rock


class GamePlay(FloatLayout):
    def __init__(self, **kwargs):
        super(GamePlay, self).__init__(**kwargs)
        # keyboard events
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

        # Draw background
        self.add_widget(background_img.image)

        # List of all entities in the game
        self.entities = []

        # Draw life bar
        life_bar_img.render(self, 0.135, 0.99, 0.13, 0.04)
        overheat_frame_texture.render(self, 0.135, 0.94, 0.13, 0.03)
        overheat_bar_texture.render(self, 0.134, 0.937, 0.128, 0.024)

        # Add a player (main player)
        self.player = Player(self)

        # Boss creating
        self.boss_appearing = False
        self.boss_appearing_time = 0.0

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'd':
            self.player.dx = 0.005
        else:
            if keycode[1] == 'a':
                self.player.dx = -0.005
        if keycode[1] == 'w':
            self.player.dy = 0.005
        else:
            if keycode[1] == 's':
                self.player.dy = -0.005
        if keycode[1] == 'spacebar':
            self.player.is_shooting = True
        return True

    def _on_keyboard_up(self, keyboard, keycode):
        if keycode[1] == 'd':
            if self.player.dx > 0:
                self.player.dx = 0
        if keycode[1] == 'a':
            if self.player.dx < 0:
                self.player.dx = 0
        if keycode[1] == 'w':
            if self.player.dy > 0:
                self.player.dy = 0
        if keycode[1] == 's':
            if self.player.dy < 0:
                self.player.dy = 0
        if keycode[1] == 'spacebar':
            self.player.is_shooting = False
        return True

    def update(self, dt):
        for e in self.entities:
            e.update(self)

        rock_chance = random.randint(0, 200)
        if rock_chance < 3:
            Rock(self)

        if not self.boss_appearing:
            self.boss_appearing_time += 0.2
            if self.boss_appearing_time > 420:
                self.boss_appearing_time = 0
                self.boss_appearing = True
                Boss(self)

        overheat_bar_texture.set_rect(0, 0, 1200 * self.player.overheat_lvl / 1500, 70)
        overheat_bar_texture.set_size(0.128 * self.player.overheat_lvl / 1500, 0.024)
        overheat_bar_texture.set_pos(0.005 + 0.128 * self.player.overheat_lvl / 1500, 0.937)


class SpaceShooter(App):
    def build(self):
        game = GamePlay()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == "__main__":
    SpaceShooter().run()
