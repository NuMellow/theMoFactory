import pygame

# Initializes pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("BMO")
#icon = pygame.image.load('image.png')
#pygame.display.set_icon(icon)

# BMO face
#bmo_face = pygame.image.load('bmo.gif')
bmo_x = 400
bmo_y = 300

def bmo():
	screen.blit(bmo_face, (bmo_x, bmo_y)

#Game loop
running = True
while running:
	
	screen.fill((199,249,214))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	bmo()
	pygame.display.update()