from Animation import Animation
from Texture import Texture

background_img = Texture('images/background.jpg', -1, 0, 0, 0)
life_bar_img = Texture('images/life.png', 0, 0, 222, 64)

space_ship_alive = Texture('images/spaceship.png', 39, 0, 39, 39)
space_ship_respawn = Texture('images/spaceship.png', 78, 0, 78, 39)
bullets_image = Texture('images/blue_bullet.png', -1, 0, 0, 0)
explosion_texture = Texture('images/explosions/new_explosion_1.png', -1, 0, 0, 0)
ship_explosion_texture = Texture('images/explosions/new_ship_explosion.png', -1, 0, 0, 0)
rock_texture = Texture('images/Rocks.png', -1, 0, 0, 0)
bomb_bonus_texture = Texture('images/Bomb.png', -1, 0, 0, 0)
ammo_bonus_texture = Texture('images/bullet_icon.png', -1, 0, 0, 0)
speed_bonus_texture = Texture('images/speed_bonus.png', -1, 0, 0, 0)
overheat_frame_texture = Texture('images/Overheat_frame.png', -1, 0, 0, 0)
overheat_bar_texture = Texture('images/Overheat_bar.png', -1, 0, 0, 0)
boss_texture = Texture('images/Boss.png', -1, 0, 0, 0)
health_frame_texture = Texture('images/Boss_health_frame.png', -1, 0, 0, 0)
health_bar_texture = Texture('images/Boss_health_bar.png', -1, 0, 0, 0)
d_pad_frame_texture = Texture('images/d_pad_frame.png', -1, 0, 0, 0)
d_pad_texture = Texture('images/d_pad.png', -1, 0, 0, 0)

# Animation
space_ship_alive_anim = Animation(space_ship_alive, 39, 0, 39, 39, 1, 1, 0)
space_ship_respawn_anim = Animation(space_ship_respawn, 0, 0, 39, 39, 1, 2, 0.1)
rock_anim = Animation(rock_texture, 0, 0, 48, 48, 1, 16, 0.6)
bullets_anim = [Animation(bullets_image, 0, 128, 25, 47, 1, 1, 0),
                Animation(bullets_image, 0, 64, 44, 47, 1, 1, 0),
                Animation(bullets_image, 0, 0, 61, 47, 1, 1, 0)]
explosion_anim = [Animation(explosion_texture, 0, 0, 256, 256, 6, 8, 0.65),
                  Animation(ship_explosion_texture, 0, 0, 192, 192, 8, 8, 0.65)]
bonus_anim = [Animation(bomb_bonus_texture, 0, 0, 200, 200, 1, 1, 0),
              Animation(ammo_bonus_texture, 0, 0, 1000, 1000, 1, 1, 0),
              Animation(speed_bonus_texture, 0, 0, 1000, 1000, 1, 1, 0)]
boss_anim = Animation(boss_texture, 0, 0, 802, 496, 1, 1, 0)
