# write a python program  to convert ued to pkr , useful for travelers & finance applications, declare a function "converter", input: value(USD$), input =rupees , input +usd, usd*285=pkr value

pkr_value = float(input('Enter value in USD: '))
USD_value = 285

converted_value = pkr_value * USD_value
print(f'The converted value in PKR is: {converted_value}')

#BMI calculation

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")


# Celsius to Fahrenheit conversion
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")