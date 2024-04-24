import turtle
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
spot = turtle.Turtle()
spot.shape("circle")
spot.speed(0)

# Set the size and color of the spots
spot_size = 10
spot_spacing = spot_size * 4
spot_color = ["red", "blue", "green", "yellow", "orange", "purple"]

# Function to draw a spot at a specific position
def draw_spot(x, y):
    color = random.choice(spot_color)
    spot.penup()
    spot.goto(x, y)
    spot.pendown()
    spot.color(color)
    spot.begin_fill()
    spot.circle(spot_size)
    spot.end_fill()

# Draw multiple spots in a 20 x 20 grid
grid_size = 20
grid_spacing = spot_spacing + spot_size
start_x = -grid_size * grid_spacing / 2
start_y = -grid_size * grid_spacing / 2

for i in range(grid_size):
    for j in range(grid_size):
        x = start_x + i * grid_spacing
        y = start_y + j * grid_spacing
        draw_spot(x, y)

# Hide the turtle
spot.hideturtle()

# Exit on click
turtle.done()
