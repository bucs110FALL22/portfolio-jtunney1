import pygame
import random
import math

pygame.init()

#create screen
screen_width=500
screen_height=500
screen = pygame.display.set_mode([screen_width, screen_height])

#make main loop and player guess for winning selection here
square_length = 100
square_pos_y = 200
red_square_pos_x = 400
blue_square_pos_y = 0

playerSelection = 0

red_button = pygame.draw.rect(screen, 'blue',(blue_square_pos_y,square_pos_y,square_length,square_length))
blue_button = pygame.draw.rect(screen, 'red',(red_square_pos_x,square_pos_y,square_length,square_length))
blue_select = pygame.Rect(blue_square_pos_y, square_pos_y, square_length,square_length)
red_select = pygame.Rect(red_square_pos_x, square_pos_y, square_length,square_length)

#asking player for input
msg = 'Click the box for which player you think will win!'
font = pygame.font.Font(None, 18)
font_object = font.render(msg, True, "white")
screen.blit(font_object, (10, 10))

pygame.display.flip()

selection = False

while not selection:
  for event in pygame.event.get():
     if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click_pos = event.pos
            if red_select.collidepoint(mouse_click_pos):
                playerSelection = 1
                selection = True
            elif blue_select.collidepoint(mouse_click_pos):
                playerSelection = 2
                selection = True

  
pygame.display.flip()
pygame.time.wait(1000)

#create dart board
pygame.draw.rect(screen, 'light blue',(0,0,500,500))
pygame.draw.circle(screen, 'red',(250,250),250)

player_red_score = 0
player_blue_score = 0 

#simulate game
for i in range(10):
  #Player 1 
  #create random landing spot of dart
  random_x = random.randrange(0,screen_width)
  random_y = random.randrange(0, screen_height)

  distance_from_center = math.hypot((screen_width/2)-random_x, (screen_height/2)- 
  random_y) #the distance formula

#determine if inside circle or not
  if distance_from_center <= screen_width/2:
    #draw dot at langing spot
    pygame.draw.circle(screen, 'black',(random_x,random_y),10)
    player_red_score = player_red_score + 1
  else:
    #draw dot at langing spot
    pygame.draw.circle(screen, 'orange',(random_x,random_y),10)

  #player 2
      #create random landing spot of dart
  random_x = random.randrange(0,screen_width)
  random_y = random.randrange(0, screen_height)

  distance_from_center = math.hypot((screen_width/2)-random_x, (screen_height/2)- 
  random_y) #the distance formula

#determine if inside circle or not
  if distance_from_center <= screen_width/2:
    #draw dot at langing spot
    pygame.draw.circle(screen, 'blue',(random_x,random_y),10)
    player_blue_score = player_blue_score + 1
  else:
    #draw dot at langing spot
    pygame.draw.circle(screen, 'purple',(random_x,random_y),10)

    
#print the winner
if player_red_score > player_blue_score:
  print('Player Red won the game with a score of: ', player_red_score)
  print('Player Blue only had a score of: ', player_blue_score)
  if playerSelection == 1:
    print('You guessed correctly')
  else:
    print('You guessed incorrectly')
    
elif player_blue_score > player_red_score:
  print('Player Blue won the game with a score of: ', player_blue_score)
  print('Player Red only had a score of: ', player_red_score)
  if playerSelection == 2:
    print('You guessed correctly')
  else:
    print('You guessed incorrectly')
else:
  print('The game was a tie with both players scoring: ', player_red_score)


pygame.display.flip()
pygame.time.wait(5000)