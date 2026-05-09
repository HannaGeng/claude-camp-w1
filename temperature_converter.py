# # Temperature Converter
choice = input("Convert (C)elsius or (F)ahrenheit? ")

if choice.upper() == "C":
    celsius = int(input("Enter Celsius: "))
    fahrenheit = round(celsius * 9 / 5 + 32)
    print("Fahrenheit:", fahrenheit)

elif choice.upper() == "F":
    fahrenheit = int(input("Enter Fahrenheit: "))
    celsius = round((fahrenheit - 32) * 5 / 9)
    print("Celsius:", celsius)

else:
    print("Invalid choice")
