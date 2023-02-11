'''
Greetings, this is one of my first completed projects that I'm going to add to my resume. Therefore, I will comment on my actions in detail.
To begin with, I will connect the module that is responsible for the time and random numbers.
'''
from tkinter import *
import time
import random
# Next, I will create a field with graphics, now I will use the class Tk().
tk = Tk()
tk.title(
  'Sisyphus platform'
)  # I make the title of the window - Games using the title property of the object.
tk.resizable(0, 0)  # In this line I set the window resizing limit.
# This is where I start to choke.) I believe that programmable programming languages are a kind of canvases for the creation of artists, or sheets for writers.
tk.wm_attributes(
  '-topmost',
  1)  #Put our game window above the rest of the windows on the computer.
canvas = Canvas(
  tk, width=500, height=500,
  highlightthickness=0)  #Set coordinates for visible field elements
canvas.pack()
tk.update()

# The first part is done. I included all the relevant libraries and set up a playing field for them. Next, my little project will be divided into three classes.


# In the first class, I will describe the ball object.
class Ball:

  def __init__(self, canvas, paddle, score, color):
    self.canvas = canvas
    self.paddle = paddle
    self.score = score
    # I would like to note that now I have encountered an object id, I hope I will write a short post soon, what is an object id in a programmable language.
    self.id = canvas.create_oval(
      10, 10, 25, 25, fill=color)  #I set the coordinates of the ball
    starts = [-2, -1, 1, 2]
    random.shuffle(starts)
    # In the last two lines, I have set the possible directions for starting and I mix the directions for starting. Next, I need to choose the first of the mixed options
    self.x = starts[0]
    self.y = -2
    self.canvas_height = self.canvas.winfo_height()
    self.canvas_width = self.canvas.winfo_width()
    self.hit_bottom = False
#The last 5 lines are needed so that the ball knows its coordinates and whether it has reached the bottom.

  def hit_paddle(
    self, pos
  ):  #In the first class, I will create a new function that will calculate the touch of the platform.
    paddle_pos = self.canvas.coords(self.paddle.id)
    # Where without checking the truth?)
    if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
      if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
        self.score.hit()
        return True
    return False
# We need the last 5 lines to determine whether the coordinates of the ball coincide with the coordinates of the platform.
# Next, you need to create a function that will be responsible for displaying the ball.

  def draw(self):
    self.canvas.move(self.id, self.x,
                     self.y)  # Move the ball to the desired coordinates.
    pos = self.canvas.coords(
      self.id)  # Remembering the new coordinates of the ball.
    if pos[1] <= 0:
      self.y = 2
    if pos[3] >= self.canvas_height:
      self.hit_bottom = True
      canvas.create_text(250,
                         120,
                         text='noob',
                         font=('Courier', 30),
                         fill='black')
    if self.hit_paddle(pos) == True:
      self.y = -2
    if pos[0] <= 0:
      self.x = 2
    if pos[2] >= self.canvas_width:
      self.x = -2


# We described the approximate logic of the interaction of the movement of the ball in relation to the platform and even began to write down the interaction with the player.

# In the next class, we will describe how the platform works. Denote her behavior and break the fourth wall so that the player can control the platform.


class Paddle:

  def __init__(self, canvas, color):  # Creating an image of our platform.
    self.canvas = canvas
    self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
    start_1 = [40, 60, 90, 120, 150, 180, 200]
    random.shuffle(start_1)
    self.starting_point_x = start_1[0]
    self.canvas.move(self.id, self.starting_point_x, 300)
    # In these lines, I created a platform and randomized its position on the screen.
    self.x = 0
    self.canvas_width = self.canvas.winfo_width()
    # In this code, I use a new toolkit for me, this is the interaction of a program and a person in addition to simple commands. I will manage the Platform using the arrows.
    self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
    self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
    #and most importantly, you need to start the game).
    self.started = False
    self.canvas.bind_all('<KeyPress-Return>', self.start_game)
# Now I will denote the movement by the platform in a separate function.

  def turn_right(self, event):
    self.x = 2

  def turn_left(self, event):
    self.x = -2
# Now the interpreter stack can process the start of the game. We will make a change to an already existing variable.

  def start_game(self, event):
    self.started = True
# Now I will create a method that will move the platform and limit its movement on the field boundaries.

  def draw(self):
    self.canvas.move(self.id, self.x, 0)
    pos = self.canvas.coords(self.id)
    if pos[0] <= 0:
      self.x = 0
    elif pos[2] >= self.canvas_width:
      self.x = 0


# Readability for other code writers is most important. Here I have to say that the hardest thing for me in programming is inventing variables. For convenience, you need to come up with an score, but it is very difficult to announce it manually each time. Therefore, I will take it out into a separate variable.


class Score:

  def __init__(self, canvas, color):
    self.score = 0
    self.canvas = canvas
    self.id = canvas.create_text(450,
                                 10,
                                 text=self.score,
                                 font=('Courier', 15),
                                 fill=color)

  def hit(self):
    self.score += 1
    self.canvas.itemconfig(self.id, text=self.score)


# In this small class, we have written a counting algorithm using a simple counter.

# All mechanisms are ready. Now I'll start writing the game itself. It is only necessary to create objects of the ball, platforms and give them a logical algorithm of actions.\

score = Score(canvas, 'black')
paddle = Paddle(canvas, 'black')
ball = Ball(canvas, paddle, score, 'black')
while not ball.hit_bottom:
  if paddle.started == True:
    ball.draw()
    paddle.draw()
  tk.update_idletasks()
  tk.update()
  time.sleep(0.01)
time.sleep(3)