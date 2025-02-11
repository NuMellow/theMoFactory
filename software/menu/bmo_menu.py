
import pygame  
import sys  

from .menu_enums import MAIN_MENU_ITEMS, GAMES_MENU_ITEMS  
from .menu import (
  update_is_enabled_for_menu_group,
  set_menu_positions,
  is_menu_group_active,
)
  
# initializing the constructor  
pygame.init()  
  
# screen resolution
SCREEN_HEIGHT = 480
SCREEN_WIDTH = 800 
  
# opens up a window  
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#set colors
color_light = (170,170,170) # light shade of the button  
color_dark = (100,100,100) # dark shade of the button
bg_color = (30, 57, 52)  # bmo background color
  
# stores the width and height of the  
# screen into a variable  
width = screen.get_width()
height = screen.get_height()  

def render_main_menu(mouse, item):
  #render main menu items
  for item in MAIN_MENU_ITEMS.values():
    if item.is_enabled:
      item_box = item.get_bounding_box()
      if (
        (item_box[0] <= mouse[0] <= (item_box[0] + item_box[2])
        and item_box[1] <= mouse[1] <= (item_box[1] + item_box[3]))
        or 
        (item_pos >= 0 and item.name == list(MAIN_MENU_ITEMS.values())[item_pos].name)
      ):
        #If the mouse is hovering over a menu item,
        #or a menu item is selected using arrows, highlight it
        pygame.draw.rect(screen, color_light, item_box)
      else:
        #else don't highlight it
        pygame.draw.rect(screen, color_dark, item_box)
      
      if mouse_clicked:
        if (
          item_box[0] <= mouse_x <= (item_box[0] + item_box[2])
          and item_box[1] <= mouse[1] <= (item_box[1] + item_box[3])
        ):
          if item.name == "Camera":
            item.on_click(MAIN_MENU_ITEMS["GAMES"])
          elif item.name == "Games":
            item.on_click(
              MAIN_MENU_ITEMS.values(), 
              GAMES_MENU_ITEMS.values()
            )
          else:
            item.on_click()
          mouse_clicked = False
          mouse_x = -1
          mouse_y = -1
      screen.blit(
        item.render_font(),
        item.location
      )

def main():
  update_is_enabled_for_menu_group(MAIN_MENU_ITEMS.values(), True)
  set_menu_positions(MAIN_MENU_ITEMS.values())
  set_menu_positions(GAMES_MENU_ITEMS.values())
  mouse_clicked = False
  mouse_x = -1
  mouse_y = -1
  item_pos = 0
  item_clicked = False

  while True:
    # stores the (x,y) coordinates into  
    # the variable as a tuple  
    mouse = pygame.mouse.get_pos() 
        
    for ev in pygame.event.get():
      if ev.type == pygame.QUIT:  
        pygame.quit()  
            
      #checks if a mouse is clicked  
      if ev.type == pygame.MOUSEBUTTONDOWN:
        mouse_clicked = True
        mouse_x = mouse[0]
        mouse_y = mouse[1]
      # cycle through menu items using the arrow buttons
      elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_DOWN:
        item_pos += 1
      elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_UP:
        item_pos -= 1 
      elif ev.type == pygame.KEYDOWN and (ev.key == pygame.K_SPACE or ev.key == pygame.K_RETURN):
        item_clicked = True
                  
    # fills the screen with a color  
    screen.fill(bg_color) 
    
    #render main menu items
    # render_main_menu(mouse)
    for item in MAIN_MENU_ITEMS.values():
      if item.is_enabled:
        item_box = item.get_bounding_box()
        cursor_pos = item_pos % len(MAIN_MENU_ITEMS) 
        if (
          (item_box[0] <= mouse[0] <= (item_box[0] + item_box[2])
          and item_box[1] <= mouse[1] <= (item_box[1] + item_box[3]))
          or 
          (item.name == list(MAIN_MENU_ITEMS.values())[cursor_pos].name)
        ):
          #If the mouse is hovering over a menu item,
          #or a menu item is selected using arrows, highlight it
          pygame.draw.rect(screen, color_light, item_box)
        else:
          #else don't highlight it
          pygame.draw.rect(screen, color_dark, item_box)
        
        if mouse_clicked:
          if (
            item_box[0] <= mouse_x <= (item_box[0] + item_box[2])
            and item_box[1] <= mouse[1] <= (item_box[1] + item_box[3])
          ):
            if item.name == "Camera":
              item.on_click(MAIN_MENU_ITEMS["GAMES"])
            elif item.name == "Games":
              item.on_click(
                MAIN_MENU_ITEMS.values(), 
                GAMES_MENU_ITEMS.values()
              )
            else:
              item.on_click()
            mouse_clicked = False
            mouse_x = -1
            mouse_y = -1
        screen.blit(
          item.render_font(),
          item.location
        )

    #render game menu items    
    for item in GAMES_MENU_ITEMS.values():
      if item.is_enabled:
        item_box = item.get_bounding_box()
        cursor_pos = item_pos % len(GAMES_MENU_ITEMS)
        if (
          (item_box[0] <= mouse[0] <= (item_box[0] + item_box[2])
          and item_box[1] <= mouse[1] <= (item_box[1] + item_box[3]))
          or (item.name == list(GAMES_MENU_ITEMS.values())[cursor_pos].name)
        ):
          pygame.draw.rect(screen, color_light, item_box)
        else:
          pygame.draw.rect(screen, color_dark, item_box)
        
        if mouse_clicked:
          if (
            item_box[0] <= mouse_x <= (item_box[0] + item_box[2])
            and item_box[1] <= mouse[1] <= (item_box[1] + item_box[3])
          ):
            if item.name == "Back":
              item.on_click(
                GAMES_MENU_ITEMS.values(), 
                MAIN_MENU_ITEMS.values()
              )
            else:
              item.on_click()
            mouse_clicked = False
            mouse_x = -1
            mouse_y = -1
        screen.blit(
          item.render_font(),
          item.location
        )
    
    if item_clicked:
      #check active
      if is_menu_group_active(MAIN_MENU_ITEMS.values()):
        item = list(MAIN_MENU_ITEMS.values())[cursor_pos]
        if item.name == "Camera":
          item.on_click(MAIN_MENU_ITEMS["GAMES"])
        elif item.name == "Games":
          item.on_click(
            MAIN_MENU_ITEMS.values(), 
            GAMES_MENU_ITEMS.values()
          )
        else:
          item.on_click()
      elif is_menu_group_active(GAMES_MENU_ITEMS.values()):
        item = list(GAMES_MENU_ITEMS.values())[cursor_pos]
        if item.name == "Back":
          item.on_click(
            GAMES_MENU_ITEMS.values(), 
            MAIN_MENU_ITEMS.values()
          )
        else:
          item.on_click()
      item_clicked = False
      item_pos = 0

    mouse_clicked = False
    mouse_x = -1
    mouse_y = -1
      
    # updates the frames of the game  
    pygame.display.update()  

if __name__ == "__main__":
  main()