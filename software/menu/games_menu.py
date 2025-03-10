import sys

sys.path.append("../software")
from . import menu_enums
from .menu import Menu
from .menu_item import MenuItem
from games.pro_football import pro_footbal_1861
from games.conversation_parade import conversation_parade


class GamesMenu(Menu):
	
	def __init__(self):
		super().__init__()
		self.menu_items: list[MenuItem] = [
			ProFootballMenu(),
			ConversationParadeMenu(),
			BackMenu()
		]
		self.name = menu_enums.GAMES_MENU

class ProFootballMenu(MenuItem):
	
	def __init__(self):
		super().__init__()
		self.name = menu_enums.PRO_FOOTBALL_MENU_ITEM
		
	def on_click(self) -> None:
		print("Opening football")
		pro_footbal_1861.main()
		
class ConversationParadeMenu(MenuItem):
	
	def __init__(self):
		super().__init__()
		self.name = menu_enums.CONVERSATION_PARADE_MENU_ITEM
		
	def on_click(self) -> None:
		conversation_parade.main()
		
class BackMenu(MenuItem):
	def __init__(self):
		super().__init__()
		self.name = menu_enums.BACK_MENU_ITEM
		self.is_sub_menu = True

	def on_click(self) -> str:
		return menu_enums.MAIN_MENU
