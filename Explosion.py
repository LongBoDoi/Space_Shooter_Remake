import Boss
import Bullet
import Player
import Rock
from Object import Object
from Constants import explosion_anim


class Explosion(Object):
    def __init__(self, obj, game_play):
        if isinstance(obj, Rock.Rock):
            super().__init__(obj.x + 0.085, obj.y + 0.13, 256/1200, 256/800, explosion_anim[0], game_play)
        if isinstance(obj, Player.Player):
            super().__init__(obj.x + 0.085, obj.y + 0.13, 256 / 1200, 256 / 800, explosion_anim[1], game_play)
        if isinstance(obj, Bullet.Bullet):
            super().__init__(obj.x + 0.095, obj.y + 0.145, 256 / 1200, 256 / 800, explosion_anim[0], game_play)
        if isinstance(obj, Boss.Boss):
            super().__init__(obj.x + 0.1, obj.y + 0.2, 512 / 1200, 512 / 800, explosion_anim[1], game_play)

    def update(self, game_play):
        super().update(game_play)
        self.animation.update()

        if self.animation.is_end():
            self.active = False
