from pygame import *  
from time import time as timer 
  
window = display.set_mode((700, 500))  
display.set_caption('Shooter')  
background = transform.scale(image.load('vfvf228.jpg'), (700, 500)) 
clock = time.Clock()  


class GameSprite(sprite.Sprite):  
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):  
        sprite.Sprite.__init__(self)  
        self.image = transform.scale(image.load(player_image), (width, height))  
        self.speed = player_speed  
        self.rect = self.image.get_rect()  
        self.rect.x = player_x  
        self.rect.y = player_y  
  
    def reset(self):  
        window.blit(self.image, (self.rect.x, self.rect.y)) 
 
class Player(GameSprite):  
    def update(self):  
        keys = key.get_pressed()  
        if keys[K_UP] and self.rect.y > 5:  
            self.rect.y -= self.speed  
        if keys[K_DOWN] and self.rect.y < 435:  
            self.rect.y+= self.speed  
    def update2(self): 
        keys = key.get_pressed()  
        if keys[K_w] and self.rect.y > 5:  
            self.rect.y -= self.speed  
        if keys[K_s] and self.rect.y < 435:  
            self.rect.y+= self.speed 
         
 
     
 
ball = GameSprite('asteroid.png',330,230,35,35,4) 
player1 = Player('123.png',50,175,50,75,5) 
player2 = Player('123.png',600,175,50,75,5) 
run = True 
finish = False 
while run: 
    for e in event.get():  
        if e.type == QUIT:  
            run = False 
    if not finish: 
        window.blit(background, (0, 0)) 
        ball.reset() 
        ball.update() 
        player1.reset() 
        player1.update2() 
        player2.reset() 
        player2.update() 
 
    display.update() 
    clock.tick(60)
