number = int(input("Enter a number to see its multiplication table: "))
for iteration in range(1, 6):
    output = iteration * number
    print(number, " * ", iteration, " = ", output)
