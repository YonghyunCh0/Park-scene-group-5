import turtle as trtl

# screen setup
wn = trtl.Screen()
wn.setup(width = 750, height= 600)
wn.bgcolor("skyblue")

# basic layout of park
layout = trtl.Turtle()
layout.penup()
layout.goto(-375-300)
layout.pendown()
layout.left(90)
layout.forward(350)
layout.right(90)
layout.forward(750)
layout.right(90)
layout.forward(350)

wn.mainloop()
