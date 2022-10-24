import pygame

pygame.init()
display = pygame.display.set_mode()

dictonary = {}
numbers = []
max_so_far_num = 0
scale = 3
upperlimit = 98
for i in range(2,upperlimit):
  count = 0
  x = i
  while x > 1:
      count = count + 1
      if x % 2 == 0:
       x = x/2
      else:
       x = x * 3 + 1
      numbers.append(x)
      if count > max_so_far_num:
       max_so_far_num = count
       max_so_far = str(count)
       max_val = str(i)
  dictonary[i] = count
print(dictonary)
list = [(k * scale, v * scale) for k, v in dictonary.items()]
pygame.draw.lines(display, 'white', False, list)
new_display = pygame.transform.flip(display, False, True)
display.blit( new_display , (0, 0) )
font = pygame.font.Font(None, 24)
text = 'Max count so far is: ' + max_so_far + ' Max value so far is: ' + max_val
msg = font.render(text, True, 'white')
display.blit(msg, (10,10))
pygame.display.flip()
pygame.time.wait(7000)


