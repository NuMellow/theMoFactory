import pygame

#initialize the constructor
pygame.init()

class MenuItem():
	
	def __init__(self):
		self.name: str = ""
		self.location: tuple[int, int] = (0, 0)
		self.font: pygame.font.Font = pygame.font.SysFont('Corbel', 35)
		self.is_selected: bool = False
		self.text_color: tuple[int, int, int] = (25, 243, 139)
		self.is_sub_menu: bool = False
		self.pygame: pygame = pygame
		
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
	
	def is_mouse_in_bounding_box(self, mouse_pos: tuple[int, int]):
		bounding_box = self.get_bounding_box()
		left_bound = bounding_box[0]
		right_bound = bounding_box[0] + bounding_box[2]
		top_bound = bounding_box[1]
		bottom_bound = bounding_box[1] + bounding_box[3]

		return (
			(left_bound <= mouse_pos[0] <= right_bound)
			and (top_bound <= mouse_pos[1] <= bottom_bound)
		)
