# # def add_plus_one(num1, num2):
# #     return num1 + num2 + 1
# #
# #
# # # lambda also known as anonymous function
# #
# # addition = lambda num1, num2: num1 + num2 + 1
# #
# # print(addition(5,8))
# #
# #
# # # map functions
#
# savings = [234, 555, 647.25, 839]
#
#
# # Bonus to be a list of each of the saving with 10% added on
#
# def apply_bonus(savings):
#     return savings * 1.1
#
#
# bonus_map = map(apply_bonus, savings)
#
# bonus_map_list = list(map(apply_bonus, savings))
# print(bonus_map)
#
# for b in bonus_map:
#     print(b)
#
#
# apply_bonus_lambda = map(lambda x: x * 1.1, savings)
#
# apply_bonus_lambda_list = list(map(lambda x: x * 1.1, savings))
#
# # print(apply_bonus_lambda_list)
#
# total = sum(apply_bonus_lambda)
# print(total)
#
#
# squared_lambda = map(lambda  x:x **2, apply_bonus_lambda)
#
# print(list(squared_lambda))
#
#


# use lambda to create a list of each number squared  plus 3


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s_lambda = map(lambda x: (x ** 2) + 3, numbers)
# print(list(s_lambda))

# filter wants a function that return a boolean
evens = filter(lambda x: x % 2 == 0, s_lambda)
# print(list(evens))


jobs = ["Data Analyst", "C# Developer", "Data Engineer", "DevOps Engineer", "Data Architect"]

# using map and filter produce a list of database roles

# data_jobs = []
# for i in jobs:
#     if i[0:4] == "Data":
#         data_jobs.append(i[4::])
# print(data_jobs)

# data_lambda = filter(lambda x: x[0:4] == "Data", jobs)
# data_jobs = map(lambda x: x[5::], data_lambda)
#
# print(list(data_jobs))

#
data_filter = filter(lambda x: "Data" in x, jobs)
data_map = map(lambda x: x[5::], data_filter)

print(list(data_map))
