class Settings():
	"""存储《外星人大战》的所有设置的类"""


	def __init__(self):
		"""初始化游戏的 静态设置"""
		#屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		
		#飞船的设置
		self.ship_speed_factor = 3
		self.ship_limit = 3

		#子弹设置
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 300



		#外星人的设置
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 100
		# 1 向右移动， -1 表示左
		self.fleet_direction = 1


		#以什么样的 速度 加快游戏的节奏
		self.speedup_scale = 1.1

		#外星人点数的提高速度
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""初始化游戏 进行而变化的设置"""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		#fleet_direction = 1 表示向右， -1 向左
		self.fleet_direction = 1

		#记分
		self.alien_points = 100

	def increase_speed(self):
		"""提高速度, 外星人的点数"""
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale


		self.alien_points = int(self.alien_points * self.score_scale)

		#每消灭一波就会 升1级
		#print(self.alien_points)



