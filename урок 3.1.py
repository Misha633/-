import pygame
import random

class Rect:
   def __init__(self, height, width): 
      self.x = random.randint(1, 449)
      self.y = 50
      self.dx = random.randint(5, 10)
      self.width = width
      self.height = height
      
screen = pygame.display.set_mode((500, 500))
x = 225
y = 225
dx = 1
# random.randint(a, b) - случайное целое число в диопазоне от a до b
num_rects = random.randint(3, 5)
                #0 + 1 500 - ширина квадрата (rect) - 1       
rects = [Rect(50, 50) for i in  range(num_rects)]

while True:
    
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
         pass
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and x < 450:
        x += 5
    if keys[pygame.K_a] and x > 0 :
        x -= 5
    if keys[pygame.K_s] and y < 450:
        y += 5
    if keys[pygame.K_w] and y > 0:
        y -= 5
      
      
      
    for i in range(len(rects)):  
        if rects[i].x >= 450 or rects[i].x <= 0:
            rects[i].dx = -rects[i].dx
        rects[i].x += rects[i].dx
        pygame.draw.rect(screen, (200, 10, 50), (rects[i].x, rects[i].y, rects[i].width, rects[i].height))
        
    pygame.draw.rect(screen, (50, 50, 200), (x, y, 50, 50))
    pygame.display.update()
    pygame.time.delay(8)
    

    


