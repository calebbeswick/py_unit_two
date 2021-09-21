import turtle
import math

print("This program will tell you the acute angle using the slopes of two lines")
xcoord1 = int(input("Please enter the first x coordinate"))
ycoord1 = int(input("Please enter the first y coordinate"))
xcoord2 = int(input("Please enter the second x coordinate"))
ycoord2 = int(input("Please enter the second y coordinate"))

slope1 = (0 - ycoord1) / (0 - xcoord1)
slope2 = (ycoord1 - ycoord2) / (xcoord1 - xcoord2)


upper_half = slope2 - slope1
lower_half = 1 + (slope1 * slope2)
tan = upper_half / lower_half
total_abs = abs(tan)
turtle.hideturtle()
angle_radian = math.atan(total_abs)
angle_degrees = math.degrees(angle_radian)

print("The angle is", angle_degrees, "Degrees")

turtle.goto(xcoord1, ycoord1)
turtle.write(angle_degrees, font=("Arial", 16, "normal"))
turtle.goto(xcoord2, ycoord2)
turtle.done
turtle.exitonclick()