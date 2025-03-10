from .menu import Menu
from .main_menu import MainMenu
from .games_menu import GamesMenu

class MenuDir():
    def __init__(self):
        self.menus: list[Menu] = [
            MainMenu(),
            GamesMenu(),
        ]

    def set_active_menu(self, menu_name: str) -> None:
        for menu in self.menus:
            if menu.name == menu_name:
                menu.set_active(True)
            else:
                menu.set_active(False)

    def set_menu_item_positions(self) -> None:
        for menu in self.menus:
            menu.set_menu_item_positions()

    def get_menu(self, menu_name: str) -> Menu:
        for menu in self.menus:
            if menu.name == menu_name:
                return menu

    def get_menus(self) -> list[Menu]:
        return self.menus