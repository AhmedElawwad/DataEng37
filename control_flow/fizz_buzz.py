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




def fizz_buzz_while():

    number = int(input("Please type a number"))
    while number <101:
        if number % 5 == 0 and number % 3 == 0:
            print("FizzBuzz")
            fizz_buzz_while()
        elif number % 3 == 0:
            print("Fizz")
            fizz_buzz_while()
        elif number % 5 == 0:
            print("Buzz")
            fizz_buzz_while()
        else:
            print (number)


        number += 1

fizz_buzz_while()