# first_name = "Ahmed"
# last_name = "Elawwad"
#
#
# def password_generator(first_name, last_name):
#     temp_password = first_name[len(first_name) - 2:] + last_name[len(last_name) - 2:]
#     return temp_password
#
#
# temp_password = password_generator(first_name, last_name)
#
# print(temp_password)

############

# Use negative indices to find the second to last character in company_motto. Save this to the variable second_to_last.
# Checkpoint 2 Passed
# Use negative indices to create a slice of the last 4 characters in company_motto. Save this to the variable final_word

# company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
#
# second_to_last = company_motto[-2]
#
# final_word = company_motto[-4:]
# print(final_word)


# replace name in string, hence string is immutable
#
# first_name = "Bob"
# last_name = "Daily"
#
# # first_name[0] = "R"
#
# fixed_first_name = "R" + first_name[1:]
#
# print(fixed_first_name)

########################

#
# def contains(big_string, little_string):
#   return little_string in big_string

#
# Write a function called common_letters that takes two arguments,
# string_one and string_two and then returns a list with all of the letters they have in common.

# def common_letters(string_one, string_two):
#     common = []
#     for letter in string_one:
#         if (letter in string_two) and not (letter in common):
#             common.append(letter)
#     return common


######################################
# Now for the temporary password, they want the function to take the input user name
# and shift all of the letters by one to the right, so the last letter of the username ends up
# as the first letter and so forth. For example, if the username is AbeSimp, then the temporary password
# generated should be pAbeSim.
#
# Start by defining the function password_generator so that it takes one input,
# username and in it define an empty string named password.
#
# Checkpoint 3 Passed 3. Inside password_generator create a for loop that iterates through the indices username by
# going from 0 to len(username).
#
# To shift the letters right, at each letter the for loop should add the previous letter to the string password.

#
# def password_generator(user_name):
#     password = ""
#     for i in range(0, len(user_name)):
#         password += user_name[i-1]
#     return password


# made up backward solution

# def password_generator(user_name):
#     password = ""
#     for i in range(0, len(user_name)):
#         len_i = len(user_name)
#         password += user_name[i-7]
#     return password
#
# print(password_generator("Ahmed Elawwad"))
