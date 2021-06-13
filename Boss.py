import random

from kivy.uix.label import Label

from Object import Object
from Constants import boss_anim, health_frame_texture, health_bar_texture


# self.health_bar_img.set_pos(self.x - 0.208 + self.width / 3, self.y + 0.02)
# top: 1.22
# down: 0.23
# left 0.21, right: 1
class Boss(Object):
    def __init__(self, game_play):
        max_health = random.randint(1, 10)
        move_speed = (int((11 - max_health) / 2) + 1) / 1200
        self.health_frame_img = health_frame_texture.__copy__()
        self.health_bar_img = health_bar_texture.__copy__()
        self.health_text = Label(text=str(max_health * 100))
        pos_x = random.randint(21, 100) / 100.0
        super().__init__(pos_x, 1.22, 250 / 1200, 180 / 800, boss_anim, game_play)
        self.max_health = max_health * 100
        self.current_health = self.max_health
        self.move_speed = move_speed
        self.dx = 0
        self.dy = -(1/800)
        self.special_attack = False
        self.special_attack_charge = 0.0
        self.intro = True
        self.vibrate_delay = 0.0

    def render(self, game_play):
        super().render(game_play)
        self.health_frame_img.render(game_play, self.x, self.y + 0.02, self.width, 20 / 800)
        self.health_bar_img.render(game_play, self.x, self.y + 0.02, self.width, 20 / 800)

        self.health_text.size_hint = self.width, 20/800
        self.health_text.pos_hint = {"right": self.x, "top": self.y + 0.02}
        game_play.add_widget(self.health_text)

    def update(self, game_play):
        # Check movement
        super().update(game_play)
        if self.x < 0.21:
            self.dx = self.move_speed
        if self.x > 1:
            self.dx = -self.move_speed
        self.health_frame_img.set_pos(self.x, self.y + 0.02)
        self.health_bar_img.set_pos(self.x + self.width * (self.current_health / self.max_health - 1), self.y + 0.02)
        self.health_text.pos_hint = {"right": self.x, "top": self.y + 0.02}

        # Check intro
        if self.intro:
            if self.y < 0.975:
                self.set_y(0.975)
                self.intro = False
                self.dy = 0
                self.dx = self.move_speed
        else:
            # Randomly change direction
            if random.randint(0, 200) == 0:
                self.dx = -self.dx

            # Check special attack
            if self.special_attack:
                self.special_attack_charge += 0.2
                if self.special_attack_charge > 30:
                    if self.dx != 0:
                        self.dx = 0
                    if self.dy != (-13 / 800) and self.dy != 13 / 800:
                        self.dy = (-13 / 800)
                    if self.y < 0.2:
                        self.set_y(0.2)
                        self.dy = -self.dy
                    if self.y > 0.975:
                        self.set_y(0.975)
                        self.dx = self.move_speed * random.choice((-1, 1))
                        self.dy = 0
                        self.special_attack = False
                        self.special_attack_charge = 0
                else:
                    # Vibration to prepare to attack
                    self.vibrate_delay += 0.3
                    if self.vibrate_delay > 1:
                        self.vibrate_delay = 0
                        self.dx = -self.dx
            else:
                # Randomly perform special attack
                if random.randint(0, 300) == 0:
                    self.dx = -(6 / 1200)
                    self.dy = 0
                    self.special_attack = True
