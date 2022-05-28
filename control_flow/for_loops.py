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


dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        print("They have the dog I want!")
        break
