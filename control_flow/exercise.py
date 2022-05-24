# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

def divisors(num):
    list = []

    for i in range(1, num - 1):
        if num % i == 0:
            list.append(i)
    list.append(i)
    return list


# print(divisors(12))

# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function


def two_int_func(int_1, int_2):
    if int_1 % int_2 == 0 or int_2 % int_1 == 0:
        return True
    else:
        return False


# print(two_int_func(5, 10))

# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
# "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


from string import ascii_lowercase


def letter_convert(*text):
    string = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}
    text = text

    numbers = [string[i] for i in text if i in string]

    return ' '.join(numbers)


# print(letter_convert("a", "b", "c", "d", "e", "f", "g",
#                      "h", "i", "j", "k", "l", "m", "n", "o",
#                      "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "))


# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14


def name_convert(text):
    string = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=0)}
    text = text

    numbers = [string[i] for i in text if i in string]

    return ' '.join(numbers)


# print(name_convert('bob'))


# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)


def id_convert(text):
    pass


# Q3a: Write a function which takes
# an integer as an input, and returns true if the number is prime, false otherwise.


def prime_number_checker(num):

    for i in range(2, num):
        if (num % i) == 0:
            return "number is not prime"
    return "number is prime"


# print(prime_number_checker(4))

# Q3b: Now add some functionality to the function
# which does not error if the user inputs something other than a digit

# def prime_number_checker_(num.isdigit()):
#
#     for i in range(2, num):
#         if (num % i) == 0:
#             return "number is not prime"
#     return "number is prime"

