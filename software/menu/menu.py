from .menu_item import MenuItem

class Menu():

    LEFT_MARGIN = 40
    COL_2_LEFT_MARGIN = 300
    TOP_MARGIN = 40
    PADDING = 60

    def __init__(self):
        self.name = ""
        self.menu_items: list[MenuItem] = []
        self.is_active: bool = False

    def set_active(self, active: bool) -> None:
        self.is_active = active

    def set_menu_item_positions(self) -> None:
        xpos = self.LEFT_MARGIN
        ypos = self.TOP_MARGIN

        for item in self.menu_items:
            item.location = (xpos, ypos)
            ypos += self.PADDING
            if ypos >= 360:
                xpos += self.COL_2_LEFT_MARGIN
                ypos = self.TOP_MARGIN

