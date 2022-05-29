# alphabet = ["A", "B", "C", "D", "E"]
#
# for letter in alphabet:
#     print(letter.lower())

# #
# nest = [[1,2,3], [4,5], [6,7,8]]
#
# for i in nest:
#     print(i)
#     for j in nest:
#         print(j)
#

# dict = {'first_value':'belongs_to_first', 'second_value':'belongs_to_second_value'}
#
# for values in dict['first_value']:
#     print(values)


# dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
# dog_breed_I_want = "dalmatian"
#
# for dog_breed in dog_breeds_available_for_adoption:
#     print(dog_breed)
#     if dog_breed == dog_breed_I_want:
#         print("They have the dog I want!")
#         break
#

#
# Your computer is the doorman at a bar in a country where the drinking age is 21.
# Loop through the ages list. If an entry is less than 21, skip it and move to the next entry. Otherwise, print() the
# age.


# ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
#
# for age in ages:
#     if age < 21:
#         continue
#     print(age)




#############

# We have provided the list sales_data that shows the numbers of different
# flavors of ice cream sold at three different locations: Scoopcademy, Gilberts Creamery, and Manny’s Scoop Shop.
# We want to sum up the total number of scoops sold. Start by defining a variable scoops_sold and set it to zero.

# sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
#
# scoops_sold = 0
#
# for location in sales_data:
#     print(location)
#     for each_location in location:
#         scoops_sold += each_location
# print(scoops_sold)

##############

# We have been provided a list of grades in a physics class. Using a list comprehension,
# create a new list called scaled_grades that scales the class grades based on the highest score.
# Since the highest score was a 90 we simply want to add 10 points to all the grades in the list.
#

# grades = [90, 88, 62, 76, 74, 89, 48, 57]
#
# scaled_grades = [ i + 10 for i in grades]
# print(scaled_grades)


#################################

# We have defined a list heights of visitors to a theme park.
# In order to ride the Topsy Turvy Tumbletron roller coaster, you need to be above 161 centimeters.
#
# Using a list comprehension, create a new list called can_ride_coaster
# that has every element from heights that is greater than 161.

# heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
#
# can_ride_coaster = [height for height in heights if height > 161]
#
# print(can_ride_coaster)

