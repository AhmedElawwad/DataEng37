age = input("What is your age?\n")

keep_asking = True

age_int = None

while keep_asking:
    age = input("What is your age?\n")
    if age.isdigit():
        age_int = int(age)
        keep_asking = False

    else:
        print("Please enter a valid number in digits.")

print(f"Your age is {age_int}")

