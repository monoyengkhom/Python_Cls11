import math

u = float(input("Enter the initial velocity: "))
a = int(input("Enter the acceleration: "))
s = int(input("Enter the distance covered: "))
vsq = (math.power(u,2)) + 2*a*s
v = math.sqrt(vsq)

print("The final velocity: ")