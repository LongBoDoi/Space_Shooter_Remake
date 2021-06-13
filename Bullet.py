import random

from Bonus import Bonus
from Boss import Boss
from Explosion import Explosion
from Object import Object
from Constants import bullets_anim
from Rock import Rock

offset_rock = {
    1: 0.015,
    2: 0.001,
    3: -0.01
}
offset_boss = {
    1: 250/1200 - 0.02,
    2: 250/1200 - 0.035,
    3: 250/1200 - 0.05
}


class Bullet(Object):
    def __init__(self, player, game_play):
        if player.bullet_num == 1:
            super(Bullet, self).__init__(player.x - 0.0105, player.y + 0.045, 25 / 1200, 0.05875,
                                         bullets_anim[0], game_play)
        else:
            if player.bullet_num == 2:
                super(Bullet, self).__init__(player.x - 0.0035, player.y + 0.045, 44 / 1200, 0.05875,
                                             bullets_anim[1], game_play)
            else:
                if player.bullet_num == 3:
                    super(Bullet, self).__init__(player.x + 0.0033, player.y + 0.045, 61 / 1200, 0.05875,
                                                 bullets_anim[2], game_play)
        self.dy = 0.0075
        self.count = player.bullet_num

    def update(self, game_play):
        super().update(game_play)

        if self.y > 1.055:
            self.active = False

        for e in game_play.entities:
            if e == self:
                continue
            if isinstance(e, Rock):
                if self.collides_with(e, offset_rock[self.count], 0):
                    e.active = False
                    self.active = False
                    bonus_chance = random.randint(0, 10)
                    if bonus_chance < 3:
                        Bonus(e, bonus_chance, game_play)
                    Explosion(e, game_play)
            if isinstance(e, Boss):
                if not e.intro:
                    if self.collides_with(e, offset_boss[self.count], 0.15):
                        self.active = False
                        Explosion(self, game_play)
                        if not e.special_attack:
                            e.current_health -= self.count * 2
                            e.health_bar_img.set_rect(0, 0, 1200 * e.current_health / e.max_health, 70)
                            e.health_bar_img.set_size(e.width * e.current_health / e.max_health, 20 / 800)
                            e.health_text.text = str(e.current_health)
                            if e.current_health <= 0:
                                e.active = False
                                e.health_frame_img.free(game_play)
                                e.health_bar_img.free(game_play)
                                game_play.remove_widget(e.health_text)
                                game_play.boss_appearing = False
                                Explosion(e, game_play)
