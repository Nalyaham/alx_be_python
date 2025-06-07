FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_fahrenheit(celsius): 
    print(celsius, "°F is ", (CELSIUS_TO_FAHRENHEIT_FACTOR * fahrenheit) + 32)

def convert_to_celsius(fahrenheit):
    print(fahrenheit, "°C is ", FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32))

def main():
    
    try:
        temp = int(input("Enter the temperature to convert: "))
        tempDegree = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

        match tempDegree:
            case "F":
                convert_to_celsius(temp)

            case "C":
                convert_to_fahrenheit(temp)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
