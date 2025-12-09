import turtle as trtl
trtl.colormode(255)
trtl.resizemode("user")

# screen setup
wn = trtl.Screen()
wn.setup(width = 750, height= 550)
wn.bgcolor("skyblue")
trtl.speed(0)

# basic layout of park
layout = trtl.Turtle()
layout.turtlesize(0.1)
layout.penup()
layout.goto(-375,-300)
layout.begin_fill()
layout.color(50,180,20)
layout.fillcolor(50,180, 20)
layout.pendown()
layout.left(90)
layout.forward(350)
layout.right(90)
layout.forward(750)
layout.right(90)
layout.forward(350)
layout.penup()
layout.end_fill()
layout.goto(-375,0)
layout.pensize(50)
layout.color(36,36,36)
layout.pendown()
layout.right(90)
layout.circle(500, -70)


# tree function
def tree_one(x,y):
    tree = trtl.Turtle()
    tree.penup()
    tree.goto(x,y)
    tree.pendown()
    tree.setheading(90)
    tree.begin_fill()
    tree.color(92,64,51)
    tree.fillcolor(92,64,51)
    tree.forward(70)
    tree.right(90)
    tree.forward(20)
    tree.right(90)
    tree.forward(70)
    tree.end_fill()
    tree.penup()
    tree.goto(x, y+50)
    tree.setheading(116)
    tree.begin_fill()
    tree.pendown()
    tree.forward(20)
    tree.left(90)
    tree.forward(5)
    tree.left(90)
    tree.forward(30)
    tree.penup()
    tree.end_fill()
    tree.fillcolor(6, 64, 43)
    tree.goto(x-20, y+60)
    tree.pendown()
    tree.color(6,64,43)
    for i in range(5):
        tree.begin_fill()
        tree.setheading(0)
        tree.circle(10)
        tree.penup()
        tree.goto(tree.xcor()+15, y+60)
        tree.pendown()
        tree.end_fill()
    tree.penup()
    tree.goto(x-10, y + 72)
    tree.pendown()
    for i in range(4):
        tree.begin_fill()
        tree.setheading(0)
        tree.circle(10)
        tree.penup()
        tree.goto(tree.xcor()+12, y+72)
        tree.pendown()
        tree.end_fill()
    tree.penup()
    tree.goto(x, y+85)
    tree.pendown()
    for i in range(2):
        tree.begin_fill()
        tree.setheading(0)
        tree.circle(10)
        tree.penup()
        tree.goto(tree.xcor()+15, y+85)
        tree.pendown()
        tree.end_fill()


#tree function number 2

def tree_two(x,y):
    tree = trtl.Turtle()
    tree.setheading(90)
    tree.pensize(10)
    tree.pencolor(84,44,2)
    tree.penup()
    tree.goto(x,y)
    tree.pendown()
    for i in range(5):
        temp_heading = 90-tree.heading()
        tree.forward(50/(i+1))
        tree.pensize(3)
        tree.left(50-(i*3)+temp_heading)
        tree.forward(40/((i+1)/(i+0.5)))
        tree.color(15,122,5)
        tree.begin_fill()
        tree.right(50)
        tree.circle(15)
        tree.left(50)
        tree.end_fill()
        tree.penup()
        tree.color(84,44,2)
        tree.right(180)
        tree.forward(40/((i+1)/(i+0.5)))
        tree.left(180-(50-(i*3))+temp_heading)
        tree.pendown()
        tree.right(50-(i*3)-temp_heading)
        tree.forward(40/((i+1)/(i+0.5)))
        tree.color(15,122,5)
        tree.begin_fill()
        tree.right(180)
        tree.circle(15)
        tree.right(180)
        tree.end_fill()
        tree.color(84,44,2)
        tree.penup()
        tree.left(180)
        tree.forward(40/((i+1)/(i+0.5)))
        tree.right(180-(50-(i*3))-temp_heading)
        tree.right(10)
        tree.pendown()
        tree.pensize(10)
    tree.color(84,44,2)
    tree.left(170)
    tree.pensize(3)
    tree.forward(15)
    tree.color(15,122,5)
    tree.begin_fill()
    tree.circle(12)
    tree.end_fill()
    tree.penup()
    tree.goto(x-20, y + 100)
    tree.pendown()
    tree.begin_fill()
    tree.circle(13)
    tree.end_fill()
    tree.penup()
    tree.goto(x, y+110)
    tree.pendown()
    tree.begin_fill()
    tree.circle(12)
    tree.end_fill()
    tree.penup()
    tree.goto(x+10, y+90)
    tree.pendown()
    tree.begin_fill()
    tree.circle(16)
    tree.end_fill()

# tree function number 3
def tree_three(x,y):
    tree = trtl.Turtle()
    tree.penup()
    tree.goto(x,y)
    tree.pendown()
    tree.setheading(90)
    tree.color(48,31,0)
    for i in range(10):
        tree.pensize(5-0.5*i)
        tree.forward(10+1.5*i)
    tree.penup()
    tree.color(8,48,0)
    tree.setheading(90)
    tree.goto(x, y+40)
    tree.pensize(3)
    for i in range(24):
        tree.pensize(5)
        tree.forward(5)
        tree.left(110)
        tree.pendown()
        tree.pensize(3)
        tree.forward((45-i)/3)
        tree.right(180)
        tree.forward((45-i)/3)
        tree.setheading(90)
        tree.right(110)
        tree.forward((45-i)/3)
        tree.left(180)
        tree.forward((45-i)/3)
        tree.setheading(90)
        
# car that moves by
def car():
    body1 = trtl.Turtle()
    body2 = trtl.Turtle()
    body3 = trtl.Turtle()
    body4 = trtl.Turtle()
    body5 = trtl.Turtle()
    body6 = trtl.Turtle()
    body1.shape("square")
    body2.shape("square")
    body3.shape("square")
    body4.shape("triangle")
    body5.shape("triangle")
    body6.shape("square")
    body4.setheading(90)
    body5.setheading(90)
    body1.turtlesize(2)
    body2.turtlesize(2)
    body3.turtlesize(2)
    body4.turtlesize(1.75)
    body5.turtlesize(1.75)
    body6.turtlesize(1.75)
    body1.color(204,27,14)
    body2.color(204,27,14)
    body3.color(204,27,14)
    body4.color(204,27,14)
    body5.color(204,27,14)
    body6.color(204,27,14)
    body1.penup()
    body2.penup()
    body3.penup()
    body4.penup()
    body5.penup()
    body1.goto(-40,0)
    body2.goto(0,0)
    body3.goto(40,0)
    body4.goto(10,30)
    body5.goto(-25,30)
    body6.goto(-7.5,33)
    wheel1 = trtl.Turtle()
    wheel2 = trtl.Turtle()
    wheel1.penup()
    wheel2.penup()
    wheel1.shape("circle")
    wheel2.shape("circle")
    wheel1.goto(30,-20)
    wheel2.goto(-30, -20)
    wheel1.turtlesize(2)
    wheel2.turtlesize(2)
    rim1 = trtl.Turtle()
    rim2 = trtl.Turtle()
    rim1.color(54,54,54)
    rim2.color(54,54,54)
    rim1.shape("circle")
    rim2.shape("circle")
    rim1.penup()
    rim2.penup()
    rim1.goto(30,-20)
    rim2.goto(-30,-20)
    window = trtl.Turtle()
    window.shape("square")
    window.color(14,204,195)
    window.penup()
    window.goto(-15,30)

#christmas tree
def xmas_tree():
    tree = trtl.Turtle()
    tree.penup()
    tree.goto(200, -150)
    tree.pendown()
    tree.color(67,19,1)
    tree.begin_fill()
    tree.setheading(90)
    tree.forward(150)
    tree.right(90)
    tree.forward(50)
    tree.right(90)
    tree.forward(150)
    tree.end_fill()

    # leaves
    r = 70

    
    for i in range(4):
        tree.penup()
        tree.goto(225+r, -110 + i*30)
        tree.pendown()
        tree.setheading(90)
        tree.color(7,48,0)
        tree.begin_fill()
        tree.circle(r, 180, 2)
        tree.end_fill()
        r = r - 7
    
    tree.setheading(60)
    tree.penup()
    tree.goto(220, 36)
    tree.color(191, 176, 10)
    tree.begin_fill()
    for i in range(5):
        tree.forward(10)
        tree.right(120)
        tree.forward(10)
        tree.right(72-120)
        
    tree.end_fill()

benchsize = 0.2
bench_colors = ["#944d2f", "#bf8a73", "#deb581", "#4b4c4d"]
bench = trtl.Turtle()

def draw_leg():
  bench.fillcolor(bench_colors[0])
  bench.begin_fill()
  bench.forward(30*benchsize)
  bench.left(90)
  bench.circle(16*benchsize,180)
  bench.end_fill()
  bench.penup()
  bench.left(90)
  bench.forward(30*benchsize)
  bench.left(90)
  bench.circle(16*benchsize,112.5)
  bench.pendown()
  bench.fillcolor(bench_colors[1])
  bench.begin_fill()
  bench.right(112.5)
  bench.forward(40*benchsize)
  bench.right(90)
  bench.forward(16*benchsize)
  bench.right(90)
  bench.forward(40*benchsize)
  bench.penup()
  bench.right(115)
  bench.circle(17*benchsize,50)
  bench.end_fill()



def draw_seat():
  bench.right(115)
  bench.forward(42*benchsize)
  bench.right(90)
  bench.pendown()
  bench.forward(36*benchsize)
  bench.left(180)
  bench.fillcolor(bench_colors[2])
  bench.begin_fill()
  bench.forward(245*benchsize)
  bench.right(120)
  bench.forward(14*benchsize)
  bench.right(60)
  bench.forward(235*benchsize)
  bench.right(60)
  bench.forward(14*benchsize)
  bench.end_fill()


def lower_rest():
  bench.right(180)
  bench.forward(14*benchsize)
  bench.right(30)
  bench.penup()
  bench.forward(20*benchsize)
  bench.pendown()
  bench.begin_fill()
  bench.left(90)
  bench.forward(235*benchsize)
  bench.right(100)
  bench.forward(12*benchsize)
  bench.right(80)
  bench.forward(230*benchsize)
  bench.right(80)
  bench.forward(12*benchsize)
  bench.end_fill()
  

def upper_rest():
  bench.right(180)
  bench.penup()
  bench.forward(27*benchsize)
  bench.pendown()
  bench.left(80)
  bench.begin_fill()
  bench.forward(225*benchsize)
  bench.right(100)
  bench.forward(12*benchsize)
  bench.right(80)
  bench.forward(220*benchsize)
  bench.right(80)
  bench.forward(12*benchsize)
  bench.end_fill()

def left_supports():
  bench.penup()
  bench.forward(47*benchsize)
  bench.pendown()
  bench.right(100)
  bench.forward(35*benchsize)
  bench.fillcolor(bench_colors[0])
  bench.begin_fill()
  bench.right(80)
  bench.forward(20*benchsize)
  bench.left(80)
  bench.forward(12*benchsize)
  bench.left(100)
  bench.forward(20*benchsize)
  bench.end_fill()
  bench.penup()
  bench.left(180)
  bench.forward(22*benchsize)
  bench.right(100)
  bench.forward(6*benchsize)
  bench.pendown()
  bench.fillcolor(bench_colors[3])
  bench.begin_fill()
  bench.circle(3*benchsize)
  bench.end_fill()
  
  bench.penup()
  bench.backward(5*benchsize)
  bench.left(100)
  bench.forward(10*benchsize)
  bench.pendown()
  bench.fillcolor(bench_colors[0])
  bench.begin_fill()
  bench.forward(15*benchsize)
  bench.right(100)
  bench.forward(12*benchsize)
  bench.right(80)
  bench.forward(15*benchsize)
  bench.end_fill()
  bench.right(100)
  bench.forward(12*benchsize)
  bench.right(80)
  bench.penup()
  bench.forward(18*benchsize)
  bench.right(100)
  bench.forward(6*benchsize)
  bench.pendown()
  bench.fillcolor(bench_colors[1])
  bench.begin_fill()
  bench.circle(3*benchsize)
  bench.end_fill()

def right_supports():
  bench.pendown()
  bench.fillcolor(bench_colors[0])
  bench.begin_fill()
  bench.right(100)
  bench.forward(20*benchsize)
  bench.left(100)
  bench.forward(10*benchsize)
  bench.left(80)
  bench.forward(20*benchsize)
  bench.end_fill()
  bench.penup()
  bench.left(180)
  bench.forward(22*benchsize)
  bench.right(80)
  bench.forward(5*benchsize)
  bench.pendown()
  bench.fillcolor(bench_colors[1])
  bench.begin_fill()
  bench.circle(3*benchsize)
  bench.end_fill()
  
  bench.penup()
  bench.backward(5*benchsize)
  bench.left(80)
  bench.forward(10*benchsize)
  bench.pendown()
  bench.fillcolor(bench_colors[0])
  bench.begin_fill()
  bench.forward(15*benchsize)
  bench.right(80)
  bench.forward(10*benchsize)
  bench.right(100)
  bench.forward(15*benchsize)
  bench.end_fill()
  bench.right(80)
  bench.forward(10*benchsize)
  bench.right(100)
  bench.forward(18*benchsize)
  bench.right(80)
  bench.forward(5*benchsize)
  bench.fillcolor(bench_colors[3])
  bench.begin_fill()
  bench.circle(3*benchsize)
  bench.end_fill()

def draw_bench():
  #first leg
  draw_leg()
  
  #getting to second leg
  bench.circle(17*benchsize,65)
  bench.left(90)
  bench.forward(30*benchsize)
  bench.penup()
  bench.forward(150*benchsize)
  bench.pendown()
  
  #second leg
  draw_leg()
  
  #seat section
  draw_seat()
  
  #back rest bottom
  lower_rest()
  
  #back rest top
  upper_rest()
  
  #back rest supports
  #left side supports
  left_supports()
  
  #going to right side
  bench.penup()
  bench.forward(5*benchsize)
  bench.right(80)
  bench.forward(49*benchsize)
  bench.right(100)
  bench.forward(165*benchsize)
  
  #right side supports
  right_supports()
  
  #going to left edge
  bench.penup()
  bench.forward(5*benchsize)
  bench.right(100)
  bench.forward(52*benchsize)
  bench.left(100)
  bench.forward(200*benchsize)
  bench.pendown()
  
  #arm rest left
  bench.left(85)
  bench.fillcolor(bench_colors[1])
  bench.begin_fill()
  bench.forward(25*benchsize)
  bench.left(90)
  bench.forward(10*benchsize)
  bench.left(85)
  bench.forward(25*benchsize)
  bench.end_fill()
  bench.penup()
  bench.right(80)
  bench.forward(225*benchsize)
  bench.pendown()
  
  #arm rest right
  bench.right(85)
  bench.begin_fill()
  bench.forward(25*benchsize)
  bench.right(90)
  bench.forward(10*benchsize)
  bench.right(85)
  bench.forward(25*benchsize)
  bench.end_fill()





walkersize = 0.5
walker_colors = ["gray", "green", "brown"]
walker = trtl.Turtle()


def draw_legs():
  #dog walker's left leg
  walker.setheading(260)
  walker.fillcolor(walker_colors[0])
  walker.forward(19*walkersize)
  walker.begin_fill()
  walker.forward(16*walkersize)
  walker.right(10)
  walker.forward(25*walkersize)
  walker.circle(10*walkersize,180)
  walker.forward(25*walkersize)
  walker.left(10)
  walker.forward(15*walkersize)
  
  #dog walker's right leg
  walker.right(145)
  walker.forward(26*walkersize)
  walker.right(10)
  walker.forward(16*walkersize)
  walker.circle(10*walkersize,180)
  walker.forward(16*walkersize)
  walker.left(10)
  walker.forward(26*walkersize)
  walker.right(25)
  walker.end_fill()

def head():
  walker.fillcolor(walker_colors[1])
  walker.begin_fill()
  walker.forward(40*walkersize)
  for i in range(10):
    walker.forward(2*walkersize)
    walker.left(5)
  walker.right(110)
  walker.circle(20*walkersize,300)
  walker.right(120)
  for i in range(10):
    walker.forward(2*walkersize)
    walker.left(6)
  walker.forward(44*walkersize)
  walker.penup()
  walker.left(90)
  walker.forward(38*walkersize)
  walker.left(90)
  walker.end_fill()
  
  
def arms():
  #walker's right arm
  walker.begin_fill()
  walker.forward(45*walkersize)
  walker.left(90)
  walker.forward(25*walkersize)
  walker.pendown()
  walker.left(50)
  walker.forward(20*walkersize)
  walker.left(15)
  walker.forward(30*walkersize)
  walker.circle(9*walkersize,180)
  walker.forward(30*walkersize)
  walker.right(15)
  walker.forward(20*walkersize)

  #walker's left arm
  walker.right(90)
  walker.penup()
  walker.forward(10*walkersize)
  walker.pendown()
  walker.left(15)
  walker.forward(20*walkersize)
  walker.circle(9*walkersize,180)
  walker.forward(30*walkersize)
  walker.end_fill()

def leash():
  walker.right(180)
  walker.penup()
  walker.forward(30*walkersize)
  for i in range(14):
    walker.forward(1*walkersize)
    walker.right(6)
  walker.left(90)
  walker.pendown()
  walker.forward(95*walkersize)

def dog_walker():
  #draw walker's legs
  draw_legs()

  #walker's head
  head()
  
  #walker's arms
  arms()
  
  #draw dog leash
  leash()


def tail():
  walker.fillcolor(walker_colors[2])
  walker.begin_fill()
  walker.right(165)
  walker.forward(60*walkersize)
  walker.circle(10*walkersize,60)
  walker.right(130)
  walker.forward(20*walkersize)
  walker.circle(3*walkersize,175)
  walker.forward(30*walkersize)

def front_leg():
  walker.left(90)
  walker.penup()
  walker.forward(10*walkersize)
  walker.right(180)
  walker.pendown()
  walker.forward(20*walkersize)
  walker.circle(6*walkersize,180)
  walker.forward(20*walkersize)
  walker.right(180)
  walker.forward(10*walkersize)

def back_leg():
  walker.left(90)
  walker.forward(5*walkersize)
  walker.right(90)
  walker.forward(10*walkersize)
  walker.circle(6*walkersize,180)
  walker.forward(10*walkersize)
  walker.left(90)
  walker.forward(12*walkersize)
  walker.right(180)
  walker.penup()
  walker.forward(12*walkersize)
  walker.pendown()
  
def dog_head():
  walker.circle(20*walkersize,60)
  walker.right(60)
  walker.forward(15*walkersize)
  walker.circle(5*walkersize,170)
  walker.forward(5*walkersize)
  walker.right(50)
  walker.circle(15*walkersize,70)
  walker.right(65)
  walker.forward(10*walkersize)
  walker.circle(2*walkersize,120)
  walker.forward(10*walkersize)
  walker.right(80)
  walker.circle(15*walkersize,40)
  walker.forward(5*walkersize)
  walker.end_fill()

def dog():
  
  #tail
  tail()
  
  #legs/underside
  walker.right(30)
  walker.circle(10*walkersize,110)
  
  front_leg()
  
  back_leg()
  
  walker.forward(20*walkersize)
  
  front_leg()
  
  back_leg()
  
  #head
  dog_head()

#draw trees
tree_one(-300,40)
tree_one(150, -250)
tree_two(100, 20)
tree_three(300, -200)


# Kyuhyun - Dip & pull up bars, moving baseketball 
# Make turtle object 
t = trtl.Turtle()

# Scale variable & pensize 
t.pensize(7.5)
t.penup()

# Bar 
def bar(scale, x, y): 
  t.goto(x,y)
  t.pendown()
  t.setheading(90)
  t.forward(100*scale)
  t.penup()
  t.setheading(270)
  t.forward(10*scale)
  t.setheading(0)
  t.pensize(5)
  t.pendown()
  t.forward(75*scale)
  t.penup()
  t.pensize(7.5)
  t.setheading(90)
  t.forward(10*scale)
  t.setheading(270)
  t.pendown()
  t.forward(100*scale)
  t.setheading(0)
  t.penup() 


# Calling functions 
# (0,0) Is the location of pull up bar - CHANGE THIS WHEN PUTTING TOGETHER 
bar(1,0,0)
bar(0.75,100,0)

# Dip bars 
def dip_bar(scale, x, y):
  t.goto(x,y)
  t.pensize(5)
  t.setheading(90)
  t.pendown()
  t.forward(50*scale)
  t.circle(-25*scale,75)
  t.forward(75*scale)
  t.circle(-25*scale,105)
  t.forward(50*scale)
  t.penup()
  t.setheading(0) 

dip_bar(1,0,0)
dip_bar(1,50,0)
t.hideturtle()

# Set color mode and import random number generator 
trtl.colormode(255)
import random 

# Moving basketball 
def basketball(angle,distance,x,y):
  # Make turtle object 
  b = trtl.Turtle()
  b.shape("circle")
  b.turtlesize(2)
  
  # 1/10 chance to get blue ball 
  if random.randint(1,10) > 9: 
    b.color(3, 252, 227)
  else:
    b.color(252, 98, 3) 
  
  #Basketball animation 
  b.penup()
  b.goto(x,y)
  b.setheading(angle)
  lengths = [1,4,9,16]
  for length in lengths:
    b.forward(length)
  for i in range(distance):
    b.forward(1)

basketball(0,200,0,0) 


#draw benches
bench.penup()
bench.goto(-50,-70)
bench.setheading(0)
bench.right(30)
bench.pendown()
draw_bench()
bench.penup()
bench.goto(15,-110)
bench.setheading(0)
bench.right(45)
bench.pendown()
draw_bench()
bench.penup()
bench.goto(65,-150)
bench.setheading(0)
bench.right(65)
bench.pendown()
draw_bench()
bench.hideturtle()

#draw dog walker
walker.penup()
walker.goto(-300, 10)
walker.right(12)
walker.pendown()
dog_walker()

#draw dog
dog()

walker.hideturtle()
#draw car
car()


wn = trtl.Screen() 
wn.mainloop() 
