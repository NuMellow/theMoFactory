
import pygame  
import sys  

from . import menu_enums
from .menu_dir import MenuDir

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

def main():
  menu_dir = MenuDir()
  menu_dir.set_active_menu(menu_enums.MAIN_MENU)
  menu_dir.set_menu_item_positions()
  mouse_clicked = False
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
      # cycle through menu items using the arrow buttons
      elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_DOWN:
        item_pos += 1
      elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_UP:
        item_pos -= 1 
      elif ev.type == pygame.KEYDOWN and (ev.key == pygame.K_SPACE or ev.key == pygame.K_RETURN):
        item_clicked = True
                  
    # fills the screen with a color  
    screen.fill(bg_color) 
    
    #render menu items
    for menu in menu_dir.get_menus():
      if menu.is_active:
        for menu_item in menu.menu_items:
          item_bounding_box = menu_item.get_bounding_box()
          cursor_pos = item_pos % len(menu.menu_items)
          if (menu_item.is_mouse_in_bounding_box(mouse)
             or menu_item.name == menu.menu_items[cursor_pos].name
          ):
            #If the mouse is hovering over a menu item,
            #or a menu item is selected using arrows, draw and highlight it
            pygame.draw.rect(screen, color_light, item_bounding_box)
          else:
            #else just draw it
            pygame.draw.rect(screen, color_dark, item_bounding_box)

          if (mouse_clicked and menu_item.is_mouse_in_bounding_box(mouse)
              or item_clicked
          ):
            selected_menu_item = menu_item if mouse_clicked else menu.menu_items[cursor_pos]
            if selected_menu_item.is_sub_menu:
              menu_to_show = selected_menu_item.on_click()
              menu_dir.set_active_menu(menu_to_show)
            else:
              selected_menu_item.on_click()

            mouse_clicked = False
            item_clicked = False

          screen.blit(
            menu_item.render_font(),
            menu_item.location
          )

    mouse_clicked = False
    item_clicked = False
      
    # updates the frames of the game  
    pygame.display.update()  

if __name__ == "__main__":
  main()