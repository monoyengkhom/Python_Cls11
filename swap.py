num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("The number before swapping: ", num1," ",num2)

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("The number after swapping: ",num1," ",num2)