from tkinter import Canvas

class GameEntity():
  def __init__(self, x, y, width, height, colour, shape="rect"):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.colour = colour
    self.shape = shape


  def addToCanvas(self, canvas):
    if self.shape == "oval":
      self.canvasEntity = canvas.create_oval(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.colour, outline="")
    else:
      self.canvasEntity = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.colour, outline="")