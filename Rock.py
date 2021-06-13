import random

from Object import Object
from Constants import rock_anim


# left: 0.04, right: 1, up: 1, down: 0.06
# OUT: left: 0.01, right: 1.035, down: 0.005, up: 1.05
class Rock(Object):
    def __init__(self, game_play):
        x = random.randint(4, 100) / 100.0
        super().__init__(x, 1.035, 0.04, 0.06, rock_anim, game_play)
        self.dx = random.randint(-3, 3) / 1200.0
        self.dy = random.randint(-6, -3) / 800.0

    def update(self, game_play):
        super().update(game_play)
        if self.x < 0.01:
            self.set_x(1.035)
        if self.x > 1.035:
            self.set_x(0.01)
        if self.y < 0.005:
            self.active = False

        self.animation.update()
