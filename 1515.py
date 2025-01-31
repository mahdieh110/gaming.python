import turtle 
import time 
import random

delay = 0.1
score = 0
high_score = 0


wn = turtle.Screen() 
wn.title('Turtle بازي با مار')
wn.bgcolor('sky blue')
wn.setup(width=800,height=500)
wn.tracer(0)

head = turtle.Turtle() 
head.shape('square')
head.color('dark blue')
head.penup()
head.goto(0,0)
head.direction = "Stop"

segments=[]

food = turtle.Turtle()  
food.shape('circle') 
food.color('red') 
food.penup() 
food.goto(0, 100)

pen = turtle.Turtle() 
pen.speed(0) 
pen.color("purple") 
pen.penup() 
pen.hideturtle() 
pen.goto(0, 250) 
pen.write("Score : 0 High Score : 0",  align="center", font=("candara", 24, "bold"))

def goup(): 
    if head.direction != "down":
        head.direction = "up"

def godown():
     if head.direction != "up":
         head.direction = "down"
def goleft():
    if head.direction != "right":
         head.direction = "left"
def goright():
    if head.direction != "left":
         head.direction = "right"

def move(): 
    if head.direction == "up": 
        y = head.ycor() 
        head.sety(y+20) 
    if head.direction == "down": 
        y = head.ycor() 
        head.sety(y-20) 
    if head.direction == "left": 
        x = head.xcor() 
        head.setx(x-20) 
    if head.direction == "right": 
        x = head.xcor() 
        head.setx(x+20)

wn.listen()
wn.onkeypress(goup, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")


while True:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara",24, "bold"))



    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("gray")
        segment.penup()
        segments.append(segment)

        
       

        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara",24, "bold"))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    time.sleep(delay)
   
   
wn.mainloop()



