first_name = "Ahmed"
last_name = "Elawwad"


def password_generator(first_name, last_name):
    temp_password = first_name[len(first_name) - 2:] + last_name[len(last_name) - 2:]
    return temp_password


temp_password = password_generator(first_name, last_name)

print(temp_password)