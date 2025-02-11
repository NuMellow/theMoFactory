from .main_menu import (
	GamesMenu,
	CameraMenu,
	QuitMenu,
)
from .games_menu import *

GAMES = GamesMenu()
CAMERA = CameraMenu()
QUIT = QuitMenu()

MAIN_MENU_ITEMS = {
	"GAMES": GAMES,
	"CAMERA": CAMERA,
	"QUIT": QUIT,
}


PRO_FOOTBALL = ProFootballMenu()
CONVERSATION_PARADE = ConversationParadeMenu()
GAMES_BACK = BackMenu()

GAMES_MENU_ITEMS = {
	"PRO FOOTBALL": PRO_FOOTBALL,
	"CONVO PARADE": CONVERSATION_PARADE,
	"BACK": GAMES_BACK,
}
