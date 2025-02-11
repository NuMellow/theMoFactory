from .menu import Menu, update_is_enabled_for_menu_group
from games.pro_football import pro_footbal_1861

class GamesMenu(Menu):
	
	def __init__(self):
		super().__init__()
		self.name = "Games"
		
	def on_click(self, 
				menu_to_hide: list[Menu], 
				menu_to_show: list[Menu],
	):
		print("Open games")
		update_is_enabled_for_menu_group(menu_to_hide, False)
		update_is_enabled_for_menu_group(menu_to_show, True)

class CameraMenu(Menu):
	def __init__(self):
		super().__init__()
		self.name = "Camera"
		
	def on_click(self, menu_item: Menu):
		print(self.name)
		menu_item.is_enabled = True
		
class QuitMenu(Menu):
	def __init__(self):
		super().__init__()
		self.name = "Quit"

	def on_click(self):
		print(self.name)
		self.pygame.quit()

if __name__ == "__main__":
	my_menu = GamesMenu()
	my_menu.on_click()
