from manim import *
class BouncingScene(Scene):
    CONFIG={
        'radius':1
    }
    def construct(self):
        ball=self.get_ball(self.CONFIG['radius'])
        box=self.get_box()
        for mob in [ball,box]:
            self.play(Create(mob))
        ball.add_updater(self.update_ball)
        self.wait(5)
    def get_ball(self,radius):
        ball=Circle(radius=radius,color=GREEN)
        ball.velocity=np.array([0,0,0])
        return ball
    def get_box(self,width=13,height=6):
        box=Rectangle(width=width,height=height)
        return box
    def update_ball(self,ball,dt):
        ball.acceleration=np.array([0,-4,0])
        ball.velocity=ball.velocity+ball.acceleration*dt
        ball.shift(ball.velocity)
        if ball.get_center()[1]-self.CONFIG['radius']/2>3 or ball.get_center()[1]+self.CONFIG['radius']<-3:
            ball.velocity[1]=-ball.velocity[1]