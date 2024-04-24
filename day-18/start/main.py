import turtle as t
import random

tim = t.Turtle()
# tim.shape("turtle")
# tim.color("red")

# Draw a dashed line
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10) 
#     tim.pendown()



# Draw multiple shapes (simple)
# for _ in range(3):
#     tim.color("red")
#     tim.forward(100)
#     tim.right(120)

# for _ in range(4):
#     tim.color("blue")
#     tim.forward(100)
#     tim.right(90)

# for _ in range(5):
#     tim.color("green")
#     tim.forward(100)
#     tim.right(72)

# for _ in range(6):
#     tim.color("orange")
#     tim.forward(100)
#     tim.right(60)

# for _ in range(7):
#     tim.color("purple")
#     tim.forward(100)
#     tim.right(51.42)

# for _ in range(8):
#     tim.color("yellow")
#     tim.forward(100)
#     tim.right(45)



# Draw multiple shapes (using a loop)
# colors = ["red", "blue", "green", "orange", "purple", "yellow", "black", "pink", "brown", "cyan"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)



# Random walk
# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)    
#     random_color = (r, g, b)
#     return random_color

# turning_angles = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")

# for _ in range(500):
#     tim.color(random_color())
#     tim.forward(45)
#     tim.setheading(random.choice(turning_angles))



# Spirograph
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)    
    random_color = (r, g, b)
    return random_color

t.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        t.color(random_color())
        t.circle(150)
        t.setheading(t.heading() + size_of_gap)

draw_spirograph(2)

screen = t.Screen()
screen.exitonclick()


