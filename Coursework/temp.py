def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

try:
    temp = float(input("Enter the temperature value: "))
    unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        print(f"{temp}°C is {celsius_to_fahrenheit(temp):.2f}°F")
    elif unit == 'F':
        print(f"{temp}°F is {fahrenheit_to_celsius(temp):.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")
except ValueError:
    print("Invalid temperature. Please enter a number.")