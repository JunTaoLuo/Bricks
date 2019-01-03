from tkinter import Canvas
from gameEntity import *
import math

class Ball(GameEntity):
  Width = 10
  Height = 10
  Colour = "red"
  SpeedIncreaseRate = 0.2

  def __init__(self, x, y):
    super().__init__(x, y, Ball.Width, Ball.Height, Ball.Colour, "oval")
    self.Speed = 3
    self.Angle = math.pi/4


  # Properties? Also, this should be a vector instead of two numbers
  def getVelocityX(self):
    return math.cos(self.Angle) * self.Speed


  def getVelocityY(self):
    return math.sin(self.Angle) * self.Speed


  def increaseSpeed(self):
    self.Speed += Ball.SpeedIncreaseRate


  # This is actually buggy, but the proper algorithm requires proper
  # 2D vector manipulation that I don't want to write
  def collide(self, gameEntity, canvas):
    ballCoord = canvas.coords(self.canvasEntity)
    ballCenter = (ballCoord[0] + Ball.Width/2, ballCoord[1] + Ball.Height/2)
    entityCoord = canvas.coords(gameEntity.canvasEntity)
    velocityX = self.getVelocityX()
    velocityY = self.getVelocityY()

    # Check if ball's center falls within the horizontal or vertical extent of the game entity
    overlapX = entityCoord[0] < ballCenter[0] < entityCoord[2]
    overlapY = entityCoord[1] < ballCenter[1] < entityCoord[3]

    if overlapY:
      # Check if the ball is to the left or right of the entity
      leftOfEntity = ballCenter[0] < entityCoord[0]
      rightOfEntity = ballCenter[0] > entityCoord[2]

      # Check if the next position of the ball crosses the left or right edge of the entity
      collideRight = ballCoord[2] + velocityX > entityCoord[0]
      collideLeft = ballCoord[0] + velocityX < entityCoord[2]

      # Reflect the angle of the ball with the Y axis
      if (velocityX > 0 and leftOfEntity and collideRight
        or velocityX < 0 and rightOfEntity and collideLeft):
        self.Angle = math.pi - self.Angle
        return True

    if overlapX:
      # Check if the ball is above or below the entity
      aboveEntity = ballCenter[1] < entityCoord[1]
      belowEntity = ballCenter[1] > entityCoord[3]

      # Check if the next position of the ball crosses the top or bottom edge of the entity
      collideDown = ballCoord[3] + velocityY > entityCoord[1]
      collideUp = ballCoord[1] + velocityY < entityCoord[3]

      # Reflect the angle of the ball with the X axis
      if (velocityY > 0 and aboveEntity and collideDown
        or velocityY < 0 and belowEntity and collideUp):
        self.Angle *= -1
        return True

