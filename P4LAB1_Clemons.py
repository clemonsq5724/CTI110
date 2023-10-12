"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle
import random

t = turtle.Turtle()
t.pensize(3)

# Set our variables

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

PEN_COLOR = random.choice(COLORS)
SIDES = 3
LENGTH = 100
FILL = True
REPEAT = 10
for time in range(REPEAT):
  X = random.randrange(-200, 200)
  Y = random.randrange(-200, 200)
  t.penup()
  t.goto(X, Y)
  t.pendown()
  
  FILL_COLOR = random.choice(COLORS)
    
  # optional: let user pick
  SIDES = random.randrange(3, 12)
  LENGTH = random.randrange(10, 50)
  ANGLE = 360 / SIDES
    
    
  if FILL == True:
      
    t.begin_fill()
    t.fillcolor(FILL_COLOR)
    
    
    
    
  # draw a simple shape
  t.pencolor(PEN_COLOR)
  for side in range(SIDES):
    t.forward(LENGTH)
    t.right(ANGLE)
    
    
  if FILL == True:
     t.end_fill()
  
# keep window open(at end)
win = turtle.Screen()
win.exitonclick()

