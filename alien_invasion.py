
#author: xiaoxiong
#first_finish: 2020/5/14,21:07
#version: 1.0.1
#author_website: https://www.xiaoxiong713.com
#-------------------------------------------------------------


#倒入模块
import pygame

#通过类实例化 ，取得设置属性
from settings import Settings

from ship import Ship

from alien import Alien

import game_function as gf

from pygame.sprite import Group

from game_stats import GameStats
from scoreboard import Scoreboard

from button import Button

def run_game():
	#初始化，并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("我爱Python, 更爱Linux，奋斗，努力！！！")

	#创建一艘飞船
	ship = Ship(ai_settings,screen)

	#创建一个用于存储子弹的 编组
	bullets = Group()

	#创建外星人组
	aliens = Group()

	#创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)

	#创建一个 用于统计信息的实例
	stats = GameStats(ai_settings)

	#创建play按钮
	play_button = Button(ai_settings, screen, "Play")


	#创建积分牌
	sb = Scoreboard(ai_settings, screen, stats)

	#开始游戏的主要循环
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
		






