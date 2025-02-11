import pygame
import os
# from games import *
from menu import bmo_menu

# Initializes pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 480))

# Title and icon
pygame.display.set_caption("BMO")
#icon = pygame.image.load('image.png')
#pygame.display.set_icon(icon)

# BMO face
img_name = os.path.join('img', 'bmo_smile.png')
gif_name = os.path.join('img', 'breakdance.gif')
bmo_face = pygame.image.load(img_name)
bmo_x = 0
bmo_y = 0

# backgrounds
bmo_bg_color = (199,249,214)

def bmo():
	screen.blit(bmo_face, (bmo_x, bmo_y))

def openMenu():
	# menu_bg = (0,0,0)
	bmo_menu.main()

#Game loop
running = True
while running:
	
	screen.fill(bmo_bg_color)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
			openMenu() #Open Menu

			
	bmo()
	pygame.display.update()