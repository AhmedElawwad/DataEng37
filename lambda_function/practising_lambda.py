# calc_lambda = lambda num1, num2: num1 + num2
#
# print(calc_lambda(2 ,2))


# saving = [234.00, 555.55, 647.25, 839.00]

# bonus = []

# for i in saving:
#     bonus.append(i * 1.1)
# print(bonus)
#        |
#        |
#        |
#        |
#        \/
# bonus_l = list(map(lambda i: i * 1.1 ,saving))
# print(bonus_l)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_lambda = list(map(lambda x: (x ** 2 + 3), numbers))

print(num_lambda)

filter_lambda = filter(lambda x: x % 2 == 0, numbers)

print(list(filter_lambda))

jobs = ["Data Analyst", "C# Developer", "Data Engineer", "DevOps Engineer", " Data Architect"]

jobs_no_data = filter(lambda x: "Data" in x, jobs)
print(list(jobs_no_data))
map_jobs_no_data = map(lambda x: x[4::], jobs)
print(list(map_jobs_no_data))