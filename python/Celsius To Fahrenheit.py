# Python Program to convert temperature in celsius(take input from user) to fahrenheit 

# Input: temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Convert and display the result
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")
