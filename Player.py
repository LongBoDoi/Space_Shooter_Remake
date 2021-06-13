import Boss
from Bonus import Bonus
from Bullet import Bullet
from Explosion import Explosion
from Object import Object
from Constants import space_ship_alive_anim, space_ship_respawn_anim, life_bar_img
from Rock import Rock


class Player(Object):
    def __init__(self, game_play):
        super(Player, self).__init__(0.5, 0.5, 1 / 24, 0.075, space_ship_alive_anim.__copy__(), game_play)
        self.bullet_num = 1
        self.is_shooting = False
        self.shooting_delay = 2.0
        self.fast_move = False
        self.fast_move_time = 0.0
        self.overheat_lvl = 0
        self.overheat = False
        self.overheat_time = 0.0

        self.lives = 3
        self.alive = True
        self.vulnerable = True
        self.respawning = False
        self.dead_time = 0.0
        self.respawn_time = 0.0

    def set_animation(self, new_animation, game_play):
        self.animation.free(game_play)

        self.animation = new_animation.__copy__()
        self.animation.real_x = self.x
        self.animation.real_y = self.y
        self.render(game_play)

    def die(self, game_play):
        self.animation.free(game_play)
        self.alive = False
        self.lives -= 1
        life_bar_img.set_rect(0, (3 - self.lives) * 64, 222, 64)
        if self.lives == 0:
            self.active = False
        self.bullet_num = 1
        self.fast_move = False
        Explosion(self, game_play)

    def update(self, game_play):
        # Check movement
        if self.alive:
            if self.dx != 0:
                self.set_x(self.x + (self.dx * 1.5 if self.fast_move else self.dx))
            if self.dy != 0:
                self.set_y(self.y + (self.dy * 1.5 if self.fast_move else self.dy))

        # Check border
        if self.x < 0.04:
            self.set_x(0.04)
        if self.x > 1:
            self.set_x(1)
        if self.y < 0.07:
            self.set_y(0.07)
        if self.y > 1:
            self.set_y(1)
        self.animation.update()

        # Check collisions
        for e in game_play.entities:
            # collide with rock
            if self.vulnerable:
                if isinstance(e, Rock):
                    if self.collides_with(e, -0.001, -0.013):
                        self.die(game_play)
                        e.active = False
                if isinstance(e, Boss.Boss):
                    if self.collides_with(e, 0.165, 0.145):
                        self.die(game_play)
            # collide with bonus packs
            if self.alive:
                if isinstance(e, Bonus):
                    if self.collides_with(e, 0, 0):
                        e.active = False
                        # bomb_pack
                        if e.type_num == 0:
                            for entity in game_play.entities:
                                if isinstance(entity, Rock):
                                    entity.active = False
                                    Explosion(entity, game_play)
                        # ammo pack
                        if e.type_num == 1:
                            self.bullet_num += 1
                            if self.bullet_num > 3:
                                self.bullet_num = 3
                        # speed pack
                        if e.type_num == 2:
                            self.fast_move = True
                            self.fast_move_time = 0.0

        # Check shooting
        if self.is_shooting and not self.overheat and self.alive:
            self.shooting_delay += 0.25
            if self.shooting_delay > 2.0:
                self.shooting_delay = 0.0
                Bullet(self, game_play)
            self.overheat_lvl += 3
            if self.overheat_lvl > 1500:
                self.overheat_lvl = 1500
                self.overheat = True
        else:
            self.shooting_delay = 2.0
            if not self.overheat:
                self.overheat_lvl -= 2
                if self.overheat_lvl < 0:
                    self.overheat_lvl = 0

        # Check overheat
        if self.overheat:
            self.overheat_time += 0.2
            if self.overheat_time > 70.0:
                self.overheat_time = 0.0
                self.overheat = False

        # Check fast move time
        if self.fast_move:
            self.fast_move_time += 0.2
            if self.fast_move_time > 150.0:
                self.fast_move_time = 0
                self.fast_move = False

        # Check dead
        if not self.alive:
            self.vulnerable = False
            self.dead_time += 0.2
            if self.dead_time > 50.0:
                self.dead_time = 0
                self.set_animation(space_ship_respawn_anim, game_play)
                self.alive = True
                self.respawning = True

        # Check respawn
        if self.respawning:
            self.respawn_time += 0.2
            if self.respawn_time > 50.0:
                self.respawn_time = 0
                self.respawning = False
                self.vulnerable = True
                self.set_animation(space_ship_alive_anim, game_play)

        if not self.active:
            self.animation.free(game_play)
            game_play.entities.remove(self)
