from gameEntity import *
from ball import *
from tkinter import Canvas

class Paddle(GameEntity):
  Width = 100
  Height = 10
  Colour = "white"


  def __init__(self, x, y):
    super().__init__(x, y, Paddle.Width, Paddle.Height, Paddle.Colour)
    self.step = 0


  def updateBallVelocity(self, ball, canvas):
    ballCoord = canvas.coords(ball.canvasEntity)
    paddleCoord = canvas.coords(self.canvasEntity)
    ball.Angle = math.pi* (1 + min(max((((ballCoord[0] + ballCoord[2])/2 - paddleCoord[0])/self.Width), 0.2), 0.8))

