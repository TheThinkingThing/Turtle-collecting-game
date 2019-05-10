#Turtle Graphics Game
import turtle
import math
import random

#screen
wn = turtle.Screen()
wn.bgcolor("Gray")
wn.bgpic("gam3-wp.gif")
wn.tracer(2)

#register shapes


#Draw Border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(4)
for side in range (4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()


#create player turtle
player = turtle.Turtle()
player.color("Blue")
player.shape("triangle")
player.penup()
player.speed(0)

#create player score
score = 0

#Create goals
maxGoals = 6
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("White")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-290, 290), random.randint(-290, 290))

#set speed variable
speed = 1

#Define functions

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 1

def decreasespeed():
    global speed
    speed -= 1

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False

#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")#listens for input then calls a function
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")

while True:
    player.forward(speed)

    #Boundary Checking x coord
    if player.xcor() > 292 or player.xcor() < -292:
        player.right(180)

    #Boundary Checking y coord
    if player.ycor() > 292 or player.ycor() < -292:
        player.right(180)

    #move the goal
    for count in range(maxGoals):
        goals[count].forward(2)


        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(180)

        #Boundary Checking y coord
        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)

        #Collision checking
        if isCollision(player, goals[count]):
            goals[count].setposition(random.randint(-290, 290), random.randint(-290, 290))
            goals[count].right(random.randint(0,360))
            score += 1
            #Draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring = "Score: %s" %score
            mypen.write(scorestring, False, align ="left", font=("Back to 1982", 14, "bold"))



delay = input("Press Enter to Finish.: ")
