from . import menu_enums
from .menu import Menu
from .menu_item import MenuItem

class MainMenu(Menu):
	def __init__(self):
		super().__init__()
		self.menu_items: list[MenuItem] = [
			GamesMenuItem(),
			CameraMenuItem(),
			QuitMenuItem(),
		]
		self.name = menu_enums.MAIN_MENU

class GamesMenuItem(MenuItem):
	
	def __init__(self):
		super().__init__()
		self.name = menu_enums.GAMES_MENU_ITEM
		self.is_sub_menu = True
		
	def on_click(self):
		print("Open games")
		return menu_enums.GAMES_MENU

class CameraMenuItem(MenuItem):
	def __init__(self):
		super().__init__()
		self.name = "Camera"
		
	def on_click(self,):
		print(self.name)
		
class QuitMenuItem(MenuItem):
	def __init__(self):
		super().__init__()
		self.name = "Quit"

	def on_click(self):
		print(self.name)
		self.pygame.quit()
