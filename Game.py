import pygame
from pygame.locals import *
ACTION_RIGHT = 1
ACTION_LEFT = -1


size = 800, 800

width, height = size
GREEN = (150, 255, 150)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 24)  # You can customize the font and size

screen = pygame.display.set_mode(size)
running = True
action = ACTION_RIGHT

agent_x = width/2
agent_y = height
agent_height = 20
agent_width = 80
agent = pygame.Rect((agent_x, agent_y, agent_height, agent_width))
pressed_left = False
pressed_down = False
pressed_right = False
pressed_up = False
while(running):
    
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, agent)
    
    for event in pygame.event.get():
        # print(event)
        
        if event.type == QUIT:
            running = False
               
        elif event.type == pygame.KEYDOWN:          # check for key presses          
            if event.key == pygame.K_LEFT:        # left arrow turns left
                pressed_left = True
            elif event.key == pygame.K_RIGHT:     # right arrow turns right
                pressed_right = True
            elif event.key == pygame.K_UP:        # up arrow goes up
                pressed_up = True
            elif event.key == pygame.K_DOWN:     # down arrow goes down
                pressed_down = True
        elif event.type == pygame.KEYUP:            # check for key releases
            if event.key == pygame.K_LEFT:        # left arrow turns left
                pressed_left = False
            elif event.key == pygame.K_RIGHT:     # right arrow turns right
                pressed_right = False
            elif event.key == pygame.K_UP:        # up arrow goes up
                pressed_up = False
            elif event.key == pygame.K_DOWN:     # down arrow goes down
                pressed_down = False

    # In your game loop, check for key states:
    if pressed_left:
        print("LEFTT")
        action = ACTION_LEFT
        agent_x = agent_x - 1 
        agent.update((agent_x, agent_y, agent_height, agent_width))
        # print(event)
    if pressed_right:
        print("RIGHTTT")
        action = ACTION_RIGHT
        agent_x = agent_x + 1
        agent.update((agent_x, agent_y, agent_height, agent_width))
        # print(event)
    if pressed_up:
        print("UP")
        action = ACTION_LEFT
        agent_y = agent_y - 1 
        agent.update((agent_x, agent_y, agent_height, agent_width))
        # print(event)
    if pressed_down:
        print("DOWN")
        action = ACTION_LEFT
        agent_y = agent_y + 1 
        agent.update((agent_x, agent_y, agent_height, agent_width))
            
        
        

    action_text = f"Current Action: {'Right' if action == ACTION_RIGHT else 'Left'}"
    text_surface = font.render(action_text, True, RED)
    text_rect = text_surface.get_rect(topleft = (0,0))
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()
        
# Quit the game
pygame.quit()     