# 1. Create a tuple named zoo that contains 10 of your favorite animals.
zoo = ("tiger", "lion", "bear", "panda", "monkey", "snake", "walrus", "flamingo", "murkat", "boar")


# 2. Find one of your animals using the tuple.index(value) syntax on the tuple.
# print(zoo.index("murkat"))


# 3. Determine if an animal is in your tuple by using value in tuple syntax.
animal_to_find = "snake"
if animal_to_find in zoo:
    # print(f"The {animal_to_find} was found!")
    # Print that the animal was found


# 4. You can reverse engineer (unpack) a tuple into another tuple with the following syntax.
# children = ("Sally", "Hansel", "Gretel", "Svetlana")
# (first_child, second_child, third_child, fourth_child) = children
# print(first_child) # Output is "Sally""tiger", "lion", "bear", "panda", "monkey", "snake", "walrus", "flamingo", "murkat", "boar"
# print(second_child) # Output is "Hansel"
# print(third_child) # Output is "Gretel"
# print(fourth_child) # Output is "Svetlana"


#  Create a variable for the animals in your zoo tuple, and print them to the console.
    my_animals = ("tiger", "lion", "bear", "panda", "monkey", "snake", "walrus", "flamingo", "murkat", "boar")
    (first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eight_animal, ninth_animal, tenth_animal) = my_animals
    # print(first_animal)
    # print(second_animal)
    # print(third_animal)
    # print(fourth_animal)
    # print(fifth_animal)
    # print(sixth_animal)
    # print(seventh_animal)
    # print(eight_animal)
    # print(ninth_animal)
    # print(tenth_animal)


# 5. Convert your tuple into a list.
zoo_list = list(zoo)
# print(zoo_list)


# 6. Use extend() to add three more animals to your zoo.
zoo_list.extend(["bat", "crocodile", "wolf"])
# print("zoo list", zoo_list)


# 7. Convert the list back into a tuple.
zoo_tuple = tuple(zoo_list)
print("zoo tuple", zoo_tuple)