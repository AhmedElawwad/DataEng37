
def accepting_order():
    with open("drinks_menu.txt") as menu:

        menu_file = menu.read().lower()
    menu_list = menu_file.split("\n")
    print("The menu is :" + str(menu_list))

    with open("order.txt", "a") as order:
        # "a" write thing in append mode
        # or create a new file if doesn't exist

        order.write("\n")
        order_taking = input("Write your order here or type 'n' to leave the bar! \n")

        if order_taking in menu_list:
            order.write(order_taking)
            accepting_order()
        elif order_taking == 'n'.lower():
            print("Thanks for stopping by!! Goodbye")
            return False

        else:
            print("Not on the menu")
            accepting_order()


# def accepting_order():
#     with open("drinks_menu.txt") as menu:
#
#         menu_file = menu.read().lower()
#     menu_list = menu_file.split("\n")
#     print("The menu is :" + str(menu_list))
#
#     with open("order.txt", "a") as order:
#         # "a" write thing in append mode
#         # or create a new file if doesn't exist
#
#         order.write("\n")
#         order_taking = input("Write your order here or type 'n' to leave the bar! \n")
#
#         try:
#             if order_taking in menu_list:
#                 order.write(order_taking)
#                 accepting_order()
#             elif order_taking == 'n'.lower():
#                 print("Thanks for stopping by!! Goodbye")
#                 return False
#             else:
#                 raise print("Not on the menu")
#
#         except TypeError as errmsg:
#             print("I just made it to throw an error!!")
#             print(errmsg)


accepting_order()
