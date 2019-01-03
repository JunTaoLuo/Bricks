from gameEntity import *

class Block(GameEntity):
  Width = 50
  Height = 25

  def __init__(self, x, y, colour):
    super().__init__(x, y, Block.Width, Block.Height, colour)

