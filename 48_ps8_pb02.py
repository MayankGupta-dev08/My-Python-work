# Program to convert Celsius to Fahrenhite and Kelvin temperature.

def temp_C2F(tempC):
    tempF = (9*tempC)/5 + 32
    return tempF

def temp_C2K(tempC):
    tempK = tempC + 273
    return tempK

t = float(input("Enter the temperature in Celsius: "))
print("\nTemperature in Fahrenhite: ", temp_C2F(t))
print("Temperature in Kelvin: ", temp_C2K(t))