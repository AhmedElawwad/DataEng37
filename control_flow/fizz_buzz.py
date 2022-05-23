def fizz_buzz():
    for each_number in range(1, 101):
        string = ""
        if each_number % 3 == 0:
            string +=  "Fizz"
        if each_number % 5 == 0:
            string +=  "Buzz"
        if each_number % 5 != 0 and each_number % 3 != 0:
            string = string + str(each_number)
        print(string)

fizz_buzz()

