import turtle
import time
import random

# Initialize the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("circle")
head.color("red")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "Right"

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("green")  # Set color to green
food.speed(0)
food.penup()
food.goto(100, 100)  # Initial position (you can set it to a random position)

# Body segments
segments = []

# Functions
def move():
    if head.direction == "Up":
        head.sety(head.ycor() + 20)
    elif head.direction == "Down":
        head.sety(head.ycor() - 20)
    elif head.direction == "Right":
        head.setx(head.xcor() + 20)
    elif head.direction == "Left":
        head.setx(head.xcor() - 20)

    # Check for boundary collisions
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        game_over()

def game_over():
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "Right"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

# Keyboard bindings
def go_up():
    if head.direction != "Down":
        head.direction = "Up"

def go_down():
    if head.direction != "Up":
        head.direction = "Down"

def go_right():
    if head.direction != "Left":
        head.direction = "Right"

def go_left():
    if head.direction != "Right":
        head.direction = "Left"

# Keyboard bindings
wn.listen()
wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_right, "d")
wn.onkey(go_left, "a")

# Game loop
while True:
    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collisions with body segments
    for segment in segments:
        if head.distance(segment) < 20:
            game_over()

    # Check for collision with food
    if head.distance(food) < 20:
        # Move the food to a random position
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.shape("circle")
        new_segment.speed(0)
        new_segment.penup()
        new_segment.goto(head.xcor(), head.ycor())
        segments.append(new_segment)

        # Adjust the color shade of existing segments
        for i, segment in enumerate(segments):
            color_shade = 0.1 * (i + 1)  # Increase shade by a small factor
            color_value = max(0.3, 1 - color_shade)  # Minimum value for visibility
            segment.color((color_value, 0, 0))


    # Update the screen
    wn.update()

    # Time delay
    time.sleep(0.1)

# Ensure the window stays open
turtle.mainloop()
