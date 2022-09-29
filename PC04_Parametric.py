'''
Turtle starter code
ATLS 1300/5650
Author: Dr. Z

Author: Chris Griffin
DATE 9/26/2022

This code creates a multi-colored pentagonal spiral, surrounded by alternating black and multi-colored 
parametric equation created circles extending outwards from center. There is a cream colored background image,
and the alternating from red to blue on the circles is set by a condtional. 
'''

import turtle, math, random # import the library of commands that you'd like to use
turtle.colormode(255) # so you can use standar RGB values, 0-255

#Create a panel to draw on. 
win =turtle.Screen()
w = 900 # width of panel
h = 900 # height of panel
win.setup(width=w, height=h) #700 x 700 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!


#====================================================== Your code ======================================================
turtle.Turtle
turtle.hideturtle()
turtle.bgpic(picname="Cream Color.gif")     ###Background Picture (just a picture of cream colored background, nothing fancy)
turtle.color("red")
turtle.speed(0)    #gotta go fast
turtle.width(4)

#Circle of circles
turtle.up()
turtle.goto(-15,-170)
turtle.down()
for i in range(40):                ###circle of circles for loop
    turtle.color("black")
    turtle.forward(30)
    turtle.circle(100)
    turtle.left(30)
    turtle.right(20)

#Interior Pentagon
turtle.up()
turtle.goto(0,0)
turtle.down()
for i in range(114):              ###for loop, creates center pentagonal spiral (143)
    turtle.forward(i*2)
    if(turtle.xcor()>0):          ###Conditional changing the color from red to blue based on x cor
        turtle.color("blue")
    else:
        turtle.color("red")
    turtle.right(80)
turtle.hideturtle()
turtle.width(3)

turtle.tracer(0)   #okay I'm not making you sit through the rest
#First 1st Circle
amp=250
turtle.up()
turtle.color("black")
turtle.begin_fill()
for i in range (200):                ###for loop, creates black circle
    r=math.radians(i)                ###parametric equation
    x=amp*math.cos(i)
    y=amp*math.sin(i)
    turtle.goto(x,y)
    turtle.down()

#Second 2nd Circle
amp=300
turtle.up()
turtle.color("red")
turtle.begin_fill()
for i in range (200):                 ###for loop, creates red/blue circle
    r=math.radians(i)                 ###parametric equation
    x=amp*math.cos(i)
    y=amp*math.sin(i)
    if(turtle.xcor()>0):
        turtle.color("blue")          ###Conditional changing the color from red to blue based on x cor
    else:
        turtle.color("red")
    turtle.goto(x,y)
    turtle.down()

#Third 3rd Circle
amp=360
turtle.up()
turtle.color("black")
turtle.begin_fill()
for i in range (200):                 ###for loop, creates black circle
    r=math.radians(i)                 ###parametric equation
    x=amp*math.cos(i)
    y=amp*math.sin(i)
    turtle.goto(x,y)
    turtle.down()

#Exterior (4th) Circle
amp=425
turtle.up()
turtle.color("red")
turtle.begin_fill()
for i in range (200):                  ###for loop, creates red/blue circle
    r=math.radians(i)
    x=amp*math.cos(i)                  ###parametric equation
    y=amp*math.sin(i)
    if(turtle.xcor()>0):
        turtle.color("red")            ###Conditional changing the color from red to blue based on x cor
    else:
        turtle.color("blue")
    turtle.goto(x,y)
    turtle.down()

#======= Clean up, required to run properly ======
turtle.done() # nothing should come after this line of code!
