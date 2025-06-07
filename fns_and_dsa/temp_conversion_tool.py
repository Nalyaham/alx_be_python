FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    Result = CELSIUS_TO_FAHRENHEIT_FACTOR * (fahrenheit - 32)
    print(fahrenheit, "°F is ", Result)

def convert_to_fahrenheit(celsius):
    Result = (FAHRENHEIT_TO_CELSIUS_FACTOR * celsius) + 32
    print(celsius, "°C is ", Result)

def main():
    temp = int(input("Enter the temperature to convert: "))
    tempDegree = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    match tempDegree:
        case "F":
            convert_to_celsius(temp)

        case "C":
            convert_to_fahrenheit(temp)

if __name__ == "__main__":
    main()
