#
# try:
#     file = open("order.txt")
# except FileNotFoundError as errmsg:
#     print("It is an error but I printed it ")
#     print(errmsg)

# raise

# print(file, type(file))

# orders = file.readlines()


# orders = list(map(lambda x: x.strip('\n'), orders))

# file.close()

# with open("order.txt") as file:
#
#     raw_order = file.read()
#     # orders = list(map(lambda x: x.strip('\n'), raw_order))
#
# print(raw_order)
# file.close()


# with open("order.txt") as file:
#
#     raw_order = file.read().split('\n')
#
# print(raw_order)


# with open("order.txt", "w") as file:
#     # overwrites anything in the file
#     # or create a new file if doesn't exist
#     file.write("This will write a string")


# with open("order.txt", "a") as file:
#     # "a" write thing in apend mode
#     # or create a new file if doesn't exist
#     file.write("New line to write\n")

#
# colours = ["Red\n", "yellow\n", "green\n"]
#
# with open("order.txt", "a") as file:
#     # "a" write thing in apend mode
#     # or create a new file if doesn't exist
#     file.write("New line to write\n")
#     file.writelines(colours)  # "It writes an iterable"


# Create a drinks' menu text file
# create drinks orders text file
# write a function that will take in a drink order
# if that order exists in the menu, write it to the orders
# Otherwise, raise an error



