from tkinter import Tk, Frame, Canvas
from ball import Ball
from wall import Wall
from block import Block
from paddle import Paddle

guiHeight = 700
guiWidth = 500

# React to key press by updating the paddle's step which will be used to resolve the new paddle position
def movePaddle(e, paddle, canvas, direction):
  pos = canvas.coords(paddle.canvasEntity)

  if direction == "left" and pos[0] > 0:
    paddle.step -= 1
  elif direction == "right" and pos[2] < guiWidth:
    paddle.step += 1


# Convert tuple to rgb
def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


def main():
  # Set up game entities
  paddle = Paddle((guiWidth - Paddle.Width)/2, guiHeight - Paddle.Height - 10)
  ball = Ball(200, 600)
  topWall = Wall(0, 0, guiWidth, 0)
  leftWall = Wall(0, 0, 0, guiHeight)
  rightWall = Wall(guiWidth, 0, guiWidth, guiHeight)

  gameEntities = [paddle, ball, topWall, leftWall, rightWall]

  for i in range(0, 500, 50):
    for j in range(100, 200, 25):
      gameEntities.append(Block(i, j, _from_rgb((200, int(i*2/5), j + 50))))

  # Set up GUI
  gui = Tk()
  gui.geometry(f"{guiWidth}x{guiHeight}")
  gui.title("Breakout")

  # Bring to front
  gui.lift()
  gui.attributes("-topmost", True)
  gui.attributes("-topmost", True)
  gui.after_idle(gui.attributes,'-topmost',False)

  frame = Frame(gui, width=guiWidth, height=guiHeight)

  canvas = Canvas(frame, width=guiWidth, height=guiHeight, bg='black')
  for gameEntity in gameEntities:
    gameEntity.addToCanvas(canvas)
  canvas.pack()

  # Set up key binding
  frame.bind("<Left>", lambda event: movePaddle(event, paddle, canvas, "left"))
  frame.bind("<Right>", lambda event: movePaddle(event, paddle, canvas, "right"))
  frame.pack()
  frame.focus_set()

  # While the ball is in play
  while canvas.coords(ball.canvasEntity)[1] < canvas.coords(paddle.canvasEntity)[1] - paddle.height + 1:
    for gameEntity in gameEntities:
      if isinstance(gameEntity, Ball):
        # Ball can't collide with itself
        continue
      if ball.collide(gameEntity, canvas):
        if isinstance(gameEntity, Block):
          # Ball collided with block so destroy it
          canvas.delete(gameEntity.canvasEntity)
          gameEntities.remove(gameEntity)
          ball.increaseSpeed()
        if isinstance(gameEntity, Paddle):
          # Ball collided with paddle, need to update its velocity vector
          gameEntity.updateBallVelocity(ball, canvas)

    # Update paddle position
    if (paddle.step != 0):
      canvas.move(paddle.canvasEntity, 10*paddle.step, 0)
      paddle.step = 0

    # Update ball position
    canvas.move(ball.canvasEntity, ball.getVelocityX(), ball.getVelocityY())
    canvas.update()

  exit()


if __name__ == "__main__":
  main()
