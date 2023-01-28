WIDTH    = 1280
HEIGHT   = 720
FPS      = 60
TILESIZE = 64

bar_height = 20
health_bar_width = 200
energy_bar_width = 140
item_box_size = 80
ui_font = './graphics/font/joystix.ttf'
ui_font_size = 18

water_colour = '#71ddee'
ui_bg_colour = '#222222'
ui_border_colour = '#111111'
text_color= '#EEEEEE'

health_colour = 'red'
energy_colour = 'blue'
ui_border_active_colour = 'gold'

weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphics': './graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'graphics': './graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphics': './graphics/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphics': './graphics/weapons/rapier/full.png'},
    'sai': {'cooldown': 80, 'damage': 10, 'graphics': './graphics/weapons/rapier/full.png'},
}

magic_data = {
    'flame': {'strength': 5, 'cost': 20, 'graphics': './graphics/particles/flame/fire.png'},
    'heal': {'strength': 20, 'cost': 10, 'graphics': './graphics/particles/heal/heal.png'} 
}

monster_data = {
	'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'../audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'../audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}
