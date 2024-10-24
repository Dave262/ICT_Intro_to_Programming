# Write a program that creates a list of pets: cat, dog, rabbit, snake, and then displays the list.


# Write a program that reverses the order of the list of pets (from question 1) and then displays the list.


def list_creator(reverse: bool = False) -> None: 
    my_list: list[str] = ["cat", 1, "rabbit", "snake"] 
    print (my_list.reverse)
    if not reverse:
        for pet in my_list:
            print(pet)
    else:
        for pet in my_list[::-1]: # [::-1] reverses the order
            print(pet)
           

list_creator(True)
 




# Given the following list of pets = [“dog”, “cat”, “goldfish”] use a for loop to display each pet.


def other_list() -> None:
    pet_list: list[str] = ["dog", "cat", "goldfish"]
    for pet in pet_list:
        print(pet)


other_list()