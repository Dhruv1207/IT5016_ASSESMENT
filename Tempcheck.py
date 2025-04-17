temperature = float(input("Enter the temperature in Celsius: "))

# Check the temperature range and print the appropriate message
if temperature < 0:
    print("It's freezing!")
elif 0 <= temperature <= 15:
    print("It's cold!")
elif 16 <= temperature <= 30:
    print("It's warm!")
else:
    print("It's hot!")