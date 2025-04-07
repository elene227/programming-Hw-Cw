import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Simple House Drawing")

# Create a turtle named "pen"
pen = turtle.Turtle()

# Draw the square base of the house
for i in range(4):
    pen.forward(100)  # Move forward 100 units
    pen.left(90)     # Turn left 90 degrees

# Draw the roof (a triangle)
pen.goto(0, 100)     
pen.goto(50, 150)    
pen.goto(100, 100)  
pen.goto(100, 0)     

# Finish the drawing
pen.goto(0, 0)       # Go back to the starting point

# Hide the turtle
pen.hideturtle()

# Wait for user to click to exit
screen.exitonclick()
