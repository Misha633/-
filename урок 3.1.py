import pygame
import random

class Rect:
   def __init__(self, x, y, dx, width, height, s): 
      self.x = x
      self.y = y
      self.dx = dx
      self.width = width
      self.height = height
      self.s = s
      
   def die(self):
       self.x = -100
       self.y = -100
       self.s = False
    
      
def kill_rocket():
    global rx, ry, rs   
    rx = -100
    ry = -100
    rs = False     
      
screen = pygame.display.set_mode((500, 500))
x = 225
y = 450
dx = 1
hp = 3


rx = -100
ry = -100
rs = False

pygame.init()

font = pygame.font.Font(None, 60)






# random.randint(a, b) - случайное целое число в диопазоне от a до b
num_rects = random.randint(3, 5)
                #0 + 1 500 - ширина квадрата (rect) - 1       
rects = [Rect(random.randint(1, 449), 50, random.randint(5,10), 50, 50, True) for i in  range(num_rects)]
bullets = [Rect(-100, -100, 7, 25, 25, False) for i in  range(num_rects)]

while True:
    screen.fill((0, 0, 0))
    hp_text = font.render(str(hp), True, (255, 255, 255))
    screen.blit(hp_text, (450, 10))
    for event in pygame.event.get():
         pass
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and x < 450:
        x += 5
    if keys[pygame.K_a] and x > 0 :
        x -= 5
    if keys[pygame.K_SPACE] and rs == False:
        rx = x + 50 // 4
        ry = y
        rs = True
        
    if ry <= 0:
        kill_rocket()
    
    
    if rs:
        pygame.draw.rect(screen, (0, 255, 0), (rx, ry, 25, 25 ))
        ry -= 12
        
    if hp <=0:
        break
    # обработка врагов в этом цикле  
    for i in range(len(rects)):
        if rects[i].x > x and rects[i].x < x + 50 and bullets[i].s == False:
            bullets[i].x = rects[i].x + rects[i].width // 4
            bullets[i].y =  rects[i].y
            bullets[i].s = True
         
        if bullets[i].y >=500:
            bullets[i].die()
            
        if (x < bullets[i].x < x + 50 or x < bullets[i].x + bullets[i].width < x + 50) and \
            bullets[i].y + bullets[i].height >= y:
            bullets[i].die()
            hp -= 1
            
            
        
        if bullets[i].s:
            bullets[i].y += bullets[i].dx
            pygame.draw.rect(screen, (0, 255, 255), (bullets[i].x, bullets[i].y, bullets[i].width, bullets[i].height))
        if rects[i].x >= 450 or rects[i].x <= 0:
            rects[i].dx = -rects[i].dx
        if (rx >= rects[i].x and rx <= rects[i].width or rx + 25 <= rects[i].x + rects [i].width and rx + 25 >= rects[i].x) and ry <= rects[i].y + rects[i].height:
            kill_rocket()
            rects[i].die()
        if rects[i].s:
           rects[i].x += rects[i].dx
           
           pygame.draw.rect(screen, (200, 10, 50), (rects[i].x, rects[i].y, rects[i].width, rects[i].height))
        
    pygame.draw.rect(screen, (50, 50, 200), (x, y, 50, 50))
    pygame.display.update()
    pygame.time.delay(8)

text = font.render("Game Over!", True, (255, 255, 255))
screen.blit(text, (125, 200))
pygame.display.update()
    

    


