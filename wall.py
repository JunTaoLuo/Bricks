from gameEntity import *

class Wall(GameEntity):
  Colour = "white"

  def __init__(self, x, y, width, height):
    super().__init__(x, y, width, height, Wall.Colour)

