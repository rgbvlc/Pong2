#name=Pong2
#author=rgbvlc bartek.b133@wp.pl
#info=simple game in pygame, livewires
#           remake the classic pong game!
#status=unfinished
#final version= ~ summer 2018
#todo= acceleration  the ball, AI, profile system

from livewires import games
import random, pygame, datetime


games.init(screen_width=770, screen_height=525, fps=50)
games.mouse.is_visible=False
pygame.display.set_caption("Pong2")  

class Move(games.Sprite):
    maybe =(True, False)
    touch=0
    def balldirect(self):
        direct = random.choice(Move.maybe)
        self.direct = direct  
 
    def collide(self):
        for ball in self.overlapping_sprites:
            ball.dx = -ball.dx
            Move.touch+=1
            print(Ball.speed,"\t", Ball.dx, Ball.dy)
                       
    def update(self):
        self.collide()
        if self.top < 0:
            self.top = 0
        if self.bottom > games.screen.height:
            self.bottom=games.screen.height
   

class Paddle(Move):
    SPEED=3.2
    paddle = games.load_image("images/paddle.bmp", transparent=False)
    def __init__(self,x,y):
        super(Paddle, self).__init__(image=Paddle.paddle,
                                     y=y,
                                     x=x)
        
    def update(self):
        super(Paddle,self).update()
        if games.keyboard.is_pressed(games.K_w):
            self.y -= Paddle.SPEED
        if games.keyboard.is_pressed(games.K_s):
            self.y += Paddle.SPEED


class Paddle2(Paddle):
    def __init__(self,x,y):
        super(Paddle2,self).__init__(x=x,
                                     y=y)
    def update(self):
        super(Paddle,self).update()
        if games.keyboard.is_pressed(games.K_UP):
            self.y -= Paddle.SPEED
        if games.keyboard.is_pressed(games.K_DOWN):
            self.y += Paddle.SPEED

class Ball(games.Sprite):
    ball_image = games.load_image("images/ball.bmp", transparent=False)
    speed=3.5
    def __init__(self):
        super(Ball, self).__init__(image=Ball.ball_image,
                                   x=games.screen.width/2,
                                   y=games.screen.height/2,
                                   dy=self.speed
                                   )
        
        self.score1 = games.Text(value=0,
                                 size=88,
                                 top=20,
                                 right=192.5,
                                 color=(255,255,255),
                                 is_collideable=False)
        games.screen.add(self.score1)
        self.score2 = games.Text(value=0,
                                 size=88,
                                 top=20,
                                 left=577,
                                 color=(255,255,255),
                                 is_collideable=False)
        games.screen.add(self.score2)
    
        Paddle.balldirect(self)
        
        if self.direct == True:
            self.dx=self.speed
        else:
            self.dx=-self.speed

    def accelerate(self):
        if Move.touch>=5:
            Ball.speed=5
            
    def out(self):
        if self.right>games.screen.width:
            self.set_x(games.screen.width/2)
            self.set_y(games.screen.height/2)
            self.score1.value += 1
        if self.left<0:
            self.set_x(games.screen.width/2)
            self.set_y(games.screen.height/2)
            self.score2.value += 1

    def save_score(self):
        date = datetime.datetime.today()
        score_file=open("score.txt","a")
        lines=[str(date), " |",str(self.score1.value),
               "-",str(self.score2.value),"|\n"]
        score_file.writelines(lines)
        score_file.close()
        games.screen.quit()
        
            
    def end_game(self):
        self.game_over = games.Message(x=games.screen.width/2,
                                       y=games.screen.width/4,
                                       size=150,
                                       color=(192,192,192),
                                       lifetime=2*games.screen.fps,
                                       after_death=self.save_score,
                                       value="||GameOver||",
                                       is_collideable=False)
        games.screen.add(self.game_over)
            
            
    def update(self):
        if self.bottom>games.screen.height or self.top<0:
            self.dy = -self.dy
        self.out()
        if self.score1.value==8 or self.score2.value==8:
            self.end_game()

        self.accelerate()
 

class Logo(games.Sprite):
    games.music.load("sounds/intro.wav")
    logoIMG=games.load_image("images/logos.png", transparent=False)
    def __init__(self):
        super(Logo, self).__init__(image=Logo.logoIMG,
                                   x=games.screen.width/2,
                                   y=games.screen.height/2)
        games.music.play(-1)
    def update(self):
        if games.keyboard.is_pressed(games.K_RETURN):
            main()


def main():
    games.screen.clear()
    games.music.stop()
    bg=games.load_image("images/background.png", transparent=False)
    games.screen.background=bg
    
    the_paddle=Paddle(x=25,y=games.screen.height/2)
    games.screen.add(the_paddle)
    the_paddle2=Paddle2(x=745, y=games.screen.height/2)
    games.screen.add(the_paddle2)
    the_ball = Ball()
    games.screen.add(the_ball)
    

def game():
    the_logo=Logo()
    games.screen.add(the_logo)
    games.screen.mainloop()
    




