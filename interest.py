# Use this file to calculate the amount of compound interest. Follow the instructions on the
# Variables and Expressions sheet carefully.

p = 10000
r = 0.08
t = int(input("Enter years "))
n = 12

answer = p * (1 + r / n) ** (n * t)

print("The amount of compound interest is", answer)