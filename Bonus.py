from Object import Object
from Constants import bonus_anim


class Bonus(Object):
    def __init__(self, rock, type_num, game_play):
        super().__init__(rock.x, rock.y, 50 / 1200, 50 / 800, bonus_anim[type_num], game_play)
        self.type_num = type_num
        self.dy = -(4 / 800)

    def update(self, game_play):
        super().update(game_play)
        if self.y < 0.005:
            self.active = False
