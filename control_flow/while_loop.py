# age = input("What is your age?\n")
#
# keep_asking = True
#
# age_int = None
#
# while keep_asking:
#     age = input("What is your age?\n")
#     if age.isdigit():
#         age_int = int(age)
#         keep_asking = False
#
#     else:
#         print("Please enter a valid number in digits.")
#
# print(f"Your age is {age_int}")


# While Loop Walkthrough

# count = 0
# print("Starting While Loop")
# while count <= 3:
#     # Loop Body
#     # Print if the condition is still true
#     print("Loop Iteration - count <= 3 is still true")
#     # Print the current value of count
#     print("Count is currently " + str(count))
#     # Increment count
#     count += 1
#     print(" ----- ")
# print("While Loop ended")
#

# count down

# countdown = 10
#
# while countdown >= 0:
#     print(countdown)
#     countdown -= 1
# print("We have liftoff!")

# ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
#
# length = len(ingredients)
# index = 0
#
# while index < length:
#     print(ingredients[index])
#     index += 1


python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0

while index < length:
    print("I am learning about", python_topics[index])
    index += 1
