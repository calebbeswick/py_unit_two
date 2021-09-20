import turtle
import math

print("This program will tell you the acute angle using the slopes of two lines")
xcoord1 = int(input("Please enter the first x coordinate"))
ycoord1 = int(input("Please enter the first y coordinate"))
xcoord2 = int(input("Please enter the second x coordinate"))
ycoord2 = int(input("Please enter the second y coordinate"))

slope1 = (0 - ycoord1) / (0 - xcoord1)
slope2 = (ycoord1 - ycoord2) / (ycoord2 - xcoord2)


part_1_abs = abs(slope2 - slope1)
part_2 = 1 + (slope1 * slope2)
part_3 = part_1_abs / part_2

angle_radian = math.atan(part_3)

angle_degree = (angle_radian * 180) / math.pi

print(slope1)
print(slope2)
print(angle_degree)





turtle.goto(xcoord1, ycoord1)
turtle.goto(xcoord2, ycoord2)
turtle.exitonclick()