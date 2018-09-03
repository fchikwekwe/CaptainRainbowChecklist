import sys
from os import system, name
from termcolor import colored

checklist = list()

def create(item):
    checklist.append(item)

def read(index):
        return checklist[index]

def update(index, item):
    checklist[index] = item

def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    checklist[index] = "√ " + checklist[index]
    return checklist[index]

# def unmark_completed(index):
#     checklist[index].replace("√", "")

def user_input(prompt):
    user_input = input(prompt)
    return user_input
    # return input(prompt)

def clear():
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')

def select(function_code):
    if function_code.lower() == "c":
        input_item = user_input(colored("Type item to add to list : ", "yellow", attrs=["bold"]))
        create(input_item)
        print(colored("Changes sucessful! The list is now : ", "yellow", attrs=["bold"]))
        list_all_items()
    elif function_code.lower() == "r":
        item_index = user_input(colored("What index number would you like to see? : ", "green", attrs=["bold"]))
        read(int(item_index))
        print(checklist[int(item_index)])
    elif function_code.lower() == "u":
        item_index = user_input(colored("Please type the index number you would like to change : ", "blue", attrs=["bold"]))
        input_item = user_input(colored("Please type the new item you would like at that index : ", "blue", attrs=["bold"]))
        update(int(item_index), str(input_item))
        print(colored("Changes sucessful! The list is now : ", "blue", attrs=["bold"]))
        list_all_items()
    elif function_code.lower() == "d":
        item_index = user_input(colored("Please type the index number you would like to delete : ", "magenta", attrs=["bold"]))
        destroy(int(item_index))
        print(colored("Changes sucessful! The list is now : ", "magenta", attrs=["bold"]))
        list_all_items()
    elif function_code.lower() == "m":
        item_index = user_input(colored("Please type the index number you would like to mark as complete : ", "cyan", attrs=["bold"]))
        mark_completed(int(item_index))
        print(colored("Changes sucessful! The list is now : ", "cyan", attrs=["bold"]))
        list_all_items()
    elif function_code.lower() == "p":
        print(colored("The list is currently: ", "red", attrs=["bold"]))
        list_all_items()
        print(colored(" Make a selection to continue.", "red", attrs=["bold"]))
    elif function_code.lower() == "q":
        return False
    else:
        print("***That did not quite work. Please stick to the letters on the list. Avoid any spaces or special characters. Upper or lowercase is fine. Please select a valid option below.***")
    return True

def test():
    create("Red cloak")
    create("Orange handkerchief")
    create("Yellow hat")
    create("Green scarf")
    create("Blue suede shoes")
    create("Purple sox")

    # print(read(0))
    # print(read(1))

    update(5, "Purple socks")
    #
    # destroy(1)
    #
    # print(read(0))
    #

    mark_completed(0)
    mark_completed(1)
    unmark_completed(0)
    list_all_items()
    # select("C")
    # list_all_items()
    # select("R")
    # list_all_items()
    #
    # user_value = user_input("Please enter a value:")
    # print(user_value)
    # clear()

test()

running = True
while running:
    try:
        selection = user_input(colored(
            "*** Welcome to Captain Rainbow's Checklist!*** ", "red", attrs=["bold"]) + colored("Press C to add to list, ", "yellow", attrs=["bold"]) + colored("R to read from list, ", "green", attrs=["bold"]) + colored("U to update item on list, ", "blue", attrs=["bold"]) + colored("M to mark item as complete, ", "cyan", attrs=["bold"]) + colored("D to delete from list, ", "magenta", attrs=["bold"]) + colored("P to display entire list, ", "red", attrs=["bold"]) + colored("and Q to quit program, ", "yellow", attrs=["bold"]) + ": ")
        clear()
        running = select(selection)
    except IndexError:
        print(colored("Please try again. Select an index on the list. The list currently goes from 0 to {}.".format(len(checklist) - 1), "red"))
