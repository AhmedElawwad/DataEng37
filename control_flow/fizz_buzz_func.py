def fizz_buzz(first_range, second_range):
    for each in range(first_range, second_range):
        if each % 3 == 0 and each % 5 == 0:
            print("FizzBuzz")
        elif each % 3 == 0:
            print("Fizz")
        elif each % 5 == 0:
            print("Buzz")
        else:
            print(each)

fizz_buzz(1, 101)