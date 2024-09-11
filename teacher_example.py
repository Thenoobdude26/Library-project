from datetime import datetime

def goBackMenu():
    goBack = input("Go back to main menu(Y/N):")
    return goBack.upper()

def mainMenu():
    print("PIZZA RIA FOOD AVAILABILITY")
    print("---------------------------")
    print("1.Add New Food")
    print("2.Deactivate Food")
    print("3.Activate Food")
    print("4.Edit Food Name")
    print("5.Delete Food")
    print("6.View Food Menu")
    print("7.Exit System")
    choice = int(input("Enter option:"))

    # Menu Selection Actions
    if choice == 1:
        addFood()
    elif choice == 2:
        deactivateFood()
    elif choice == 3:
        activateFood()
    elif choice == 4:
        editFood()
    elif choice == 5:
        delFood()
    elif choice == 6:
        viewFoods()
    else:
        print("System Exited!")
        exit()

    # Go back to the main menu after each operation
    if goBackMenu() == 'Y':
        mainMenu()
    else:
        exit()

def resetMyList():
    mylist = []  # Initialize an empty list
    with open("foods.txt", "r") as file:
        for line in file:
            items = line.split(";")
            myDictionary = {'item': items[0], 'status': items[1], 'createdAt': items[2]}
            mylist.append(myDictionary)
    return mylist

def addFood():
    print("ADD FOOD")
    print("------------")
    item = input("Add Food:")
    currDateTime = datetime.now().strftime("%d-%B-%Y %H:%M:%S")
    with open("foods.txt", 'a+') as file:
        file.write(f"{item};NOT AVAILABLE;{currDateTime};\n")

def deactivateFood():
    print("DEACTIVATE FOOD")
    print("------------")
    mylist = resetMyList()  # Reset the list before using it

    # Menu items
    no = 1
    for i in mylist:
        print(f"{no}) item:{i['item']} status:{i['status']} date and time: {i['createdAt']}")
        no += 1
    inputItems = input("Enter which food you want to deactivate:")

    # Update data in list
    for data in mylist:
        if data['item'] == inputItems:
            data['status'] = "NOT AVAILABLE"
            break

    # Write back the updated list data into file
    with open("foods.txt", "w") as file:
        for data in mylist:
            file.write(f"{data['item']};{data['status']};{data['createdAt']};\n")

def activateFood():
    print("ACTIVATE FOOD")
    print("------------")
    mylist = resetMyList()  # Reset the list before using it

    # Menu items
    no = 1
    for i in mylist:
        print(f"{no}) item:{i['item']} status:{i['status']} createdAt: {i['createdAt']}")
        no += 1
    inputItems = input("Enter which food you want to activate:")

    # Update data in list
    for data in mylist:
        if data['item'] == inputItems:
            data['status'] = "AVAILABLE"
            break

    # Write back the updated list data into file
    with open("foods.txt", "w") as file:
        for data in mylist:
            file.write(f"{data['item']};{data['status']};{data['createdAt']};\n")

def editFood():
    print("EDIT FOOD")
    print("------------")
    mylist = resetMyList()  # Reset the list before using it

    # Menu items
    no = 1
    for i in mylist:
        print(f"{no}) item:{i['item']} status:{i['status']} createdAt: {i['createdAt']}")
        no += 1
    inputItems = input("Enter which food you want to edit information:")
    newInputItems = input(f"Enter the new food name:")

    # Update the data in the list
    for data in mylist:
        if data['item'] == inputItems:
            data['item'] = newInputItems
            break

    # Write back the updated list data into file
    with open("foods.txt", "w") as file:
        for data in mylist:
            file.write(f"{data['item']};{data['status']};{data['createdAt']};\n")

def delFood():
    print("DELETE FOOD")
    print("------------")
    mylist = resetMyList()  # Reset the list before using it

    # Menu items
    no = 1
    for i in mylist:
        print(f"{no}) item:{i['item']} status:{i['status']} createdAt: {i['createdAt']}")
        no += 1

    inputItems = input(f"Which food you want to DELETE from the menu:")
    for index, data in enumerate(mylist):
        if data['item'] == inputItems:
            mylist.pop(index)
            break  # Exit the loop once the item is found and deleted

    # Write back the updated list data into file
    with open("foods.txt", "w") as file:
        for data in mylist:
            file.write(f"{data['item']};{data['status']};{data['createdAt']};\n")

def viewFoods():
    print("PIZZA RIA FOOD MENU")
    print("--------------------")
    with open("foods.txt") as file:
        for line in file:
            items = line.split(";")
            # Print each item on a new line (you can customize the format as needed)
            for item in items:
                print(item, end=" ")  # Make it 1 line
            print(" ")  # Newline

if __name__ == "__main__":
    mainMenu()