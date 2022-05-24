# def fizz_buzz():
#     for each_number in range(1, 101):
#         string = ""
#         if each_number % 3 == 0:
#             string +=  "Fizz"
#         if each_number % 5 == 0:
#             string +=  "Buzz"
#         if each_number % 5 != 0 and each_number % 3 != 0:
#             string = string + str(each_number)
#         print(string)
#
# fizz_buzz()
#


# def fizz_buzz_while() :
#     number = int(input("Please type a number"))
#     while number < 101:
#         if number % 5 == 0 and number % 3 == 0:
#             print("FizzBuzz")
#             fizz_buzz_while()
#         elif number % 3 == 0:
#             print("Fizz")
#             fizz_buzz_while()
#         elif number % 5 == 0:
#             print("Buzz")
#             fizz_buzz_while()
#         else:
#             print(number)
#
#         number += 1
#
#
# fizz_buzz_while()


def fizz_buzz_while():
    number = int(input("Please type a number"))
    while number < 101:
        if number % 5 == 0 and number % 3 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

        number += 1

        play_again = input("If you would like to play again, please type 'y' or 'n' to stop").lower()
        if play_again == 'n':
            print("Thank you, goodbye")
            break
        elif play_again == 'y':
            return fizz_buzz_while()


fizz_buzz_while()
