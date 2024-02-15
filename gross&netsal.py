name = input("Enter the name of the employee: ")
basic = float(input("Enter the Basic pay: "))

da = basic * (30/100)
hra = basic * (18/100)
pf = basic * (12.5/100)
gross = basic + da + hra 
net = gross - pf

print("The Net Salary earned = ", net)
