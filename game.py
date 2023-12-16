from pygame import *
init()
#класс-родитель для спрайтов 
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
    
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):   
    def update_r(self):
        keys = key.get_pressed()        
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()        
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
                 

        

win_width = 1000
win_height = 600
window = display.set_mode((win_width, win_height))
display.set_caption("PING-Pong")
window.fill((200,255,255))
#background = transform.scale(image.load("fon2.jpg"), (win_width, win_height))


clock = time.Clock()
FPS = 60
game = True
#rocket1 = Player()

ball = GameSprite('ball2.png', win_width/2, win_height/2, [4,4], 40,40)
rock1 = Player('ping_rocket1.png',10,win_height/2-100, 7, 20, 100)
rock2= Player('ping_rocket2.png',win_width-30,win_height/2, 7, 20, 100)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                game = quit()
    
    window.fill((200,255,255))
    
    ball.rect.x += ball.speed[0]
    ball.rect.y += ball.speed[1]
    if ball.rect.y < 0 or ball.rect.y > win_height-40:
        ball.speed[1] *= -1

    if sprite.collide_rect(ball, rock2) or \
        sprite.collide_rect(ball, rock1):
            ball.speed[1] *= -1
            ball.speed[0] *= -1

    ball.reset()


    rock2.update_r()
    rock1.update_l()

    rock1.reset()
    rock2.reset()

    display.update()
    clock.tick(FPS)

