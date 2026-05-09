# BMI Calculator

def get_positive_integer(prompt):
    while True:
        user_input = input(prompt)

        if user_input.isdigit():
            value = int(user_input)
            if value > 0:
                return value

        print("Please enter a positive integer.")


def get_gender():
    while True:
        print("Please select your gender:")
        print("1. Male")
        print("2. Female")
        print("3. Other")

        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            return "Male"
        elif choice == "2":
            return "Female"
        elif choice == "3":
            return "Other"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def get_height():
    while True:
        try:
            height = float(input("Please enter your height in centimetres: "))

            if height < 0:
                print("Height cannot be negative. Please enter again.")
                continue

            if height < 50 or height > 240:
                confirm = input("This height seems unusual. Is it correct? Enter Y or N: ").upper()
                if confirm == "Y":
                    return height
                else:
                    continue

            return height

        except ValueError:
            print("Please enter a valid number for height.")


def get_weight():
    while True:
        weight = get_positive_integer("Please enter your weight in kilograms: ")

        if weight > 250:
            confirm = input("This weight seems unusual. Is it correct? Enter Y or N: ").upper()
            if confirm == "Y":
                return weight
            else:
                continue

        return weight


def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi


def get_health_advice(bmi):
    if bmi < 18.5:
        return "Your BMI is in the underweight range. Please consider speaking with a health professional."
    elif bmi < 25:
        return "Your BMI is in the healthy weight range. Please keep maintaining a balanced lifestyle."
    elif bmi < 30:
        return "Your BMI is in the overweight range. You may consider improving diet and physical activity."
    else:
        return "Your BMI is in the obese range. Please consider seeking professional health advice."


def main():
    print("BMI Calculator")

    name = input("Please enter your name: ")
    print(f"Hello, {name}")

    age = get_positive_integer("Please enter your age: ")
    gender = get_gender()
    height_cm = get_height()
    weight_kg = get_weight()

    bmi = calculate_bmi(height_cm, weight_kg)
    advice = get_health_advice(bmi)

    height_m = height_cm / 100

    print("\n--- BMI Result ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print(f"Height: {height_cm:.1f} cm")
    print(f"Weight: {weight_kg} kg")
    print(f"BMI: {bmi:.2f}")

    print("\nCalculation:")
    print(f"BMI = weight / height²")
    print(f"BMI = {weight_kg} / ({height_m:.2f} x {height_m:.2f})")
    print(f"BMI = {bmi:.2f}")

    print("\nHealth Advice:")
    print(advice)


main()
