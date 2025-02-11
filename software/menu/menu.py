import pygame

#initialize the constructor
pygame.init()

class Menu():
	
	def __init__(self):
		self.name = ""
		self.location= (0, 0)
		self.font = pygame.font.SysFont('Corbel', 35)
		self.is_selected = False
		self.text_color = (25, 243, 139)
		self.is_enabled = False
		self.pygame = pygame
		
	def on_click(self):
		pass
		
	def render_font(self):
		rendered_font = self.font.render(
			self.name,
			True,
			self.text_color
		)
		return rendered_font
		
	def render_highlight_box(self):
		pass
		
	def update_is_selected(self, value: bool):
		self.is_selected = value
	
	def update_is_enabled(self, value: bool):
		self.is_enabled = value	
		
	def get_bounding_box(self):
		padding = 8
		width, height = self.font.size(self.name)
		start_x, start_y = self.location
		
		bounding_box = [
			start_x - padding,
			start_y - padding,
			width + ( 2 * padding),
			height + ( 2 * padding)
		]
		return bounding_box

def update_is_enabled_for_menu_group(menu_items: list[Menu], value: bool):
	for item in menu_items:
		item.update_is_enabled(value)

def is_menu_group_active(menu_items: list[Menu]) -> bool:
	is_active = False
	for item in menu_items:
		if item.is_enabled:
			is_active = True
			break
	return is_active

def set_menu_positions(menu_items:list[Menu]):
	xpos = 40
	ypos = 40
	
	for item in menu_items:
		item.location = (xpos, ypos)
		ypos += 60
		if ypos >= 360:
			xpos += 300
			ypos = 40 
