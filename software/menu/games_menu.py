import sys

sys.path.append("../software")
from .menu import Menu, update_is_enabled_for_menu_group
from games.pro_football import pro_footbal_1861
from games.conversation_parade import conversation_parade

class ProFootballMenu(Menu):
	
	def __init__(self):
		super().__init__()
		self.name = "Pro Football 1861"
		
	def on_click(self):
		print("Opening football")
		pro_footbal_1861.main()
		
class ConversationParadeMenu(Menu):
	
	def __init__(self):
		super().__init__()
		self.name = "Conversation Parade"
		
	def on_click(self):
		conversation_parade.main()
		
class BackMenu(Menu):
	def __init__(self):
		super().__init__()
		self.name = "Back"

	def on_click(
		self,
		menu_to_hide: list[Menu],
		menu_to_show: list[Menu],
	):
		update_is_enabled_for_menu_group(menu_to_hide, False)
		update_is_enabled_for_menu_group(menu_to_show, True)
