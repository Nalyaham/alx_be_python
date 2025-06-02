number = int(input("Enter a number to see its multiplication table: "))
for iteration in range(1, 11):
    output = iteration * number
    print(number, "*", iteration, "=", output)
