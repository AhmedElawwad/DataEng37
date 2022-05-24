#
#
#
# def product(*args):
#
#     result =1
#     for i in args:
#         result *= i
#     return result
#
# print(product())
#
# def product(*args):
#
#     if len(args) == 0:
#         return None
#
#     result =1
#     for i in args:
#         result *= i
#     return result
#
# print(product(1,1))


# def kwargs_demo(**kawrgs):
#     print(kawrgs, type(kawrgs))
#
# print(kwargs_demo())
#
# # kwargs return as dictionary


#
# def calculate_total_cost(**meal_price):
#     #
#     # cost = 0
#     # for i in meal_price.values():
#     #     cost += i
#     # return cost
#     return sum(meal_price.values())
#
# print(calculate_total_cost(pizza= 8.5, burger=9, hot_dog = 9.20))


# def greeting(name: str):  # : str represents the type hint in python
#     print("Hello", name)
#
# greeting(2568)
#
#
#
# def division(denom: int, num: int):
#     return denom / num
#
# a = division(12,6)
# print(a)


# Good function

"""
- name them clearly, lower letter with underscore
- clear argument name we can also use type hints
- Function should return something
- keep them small
- use comments with doc string as using help() will return the doc string
-consider type hints like :str or :int

"""

