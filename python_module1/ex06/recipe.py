import sys
import string

if __name__ != "__main__":
    sys.exit()

print("Welcome to the Python Cookbook !\n")

theSandwich = {"ingredients": "ham bread cheese tomatoes", "meal": "lunch", "prep_time": 10}
theCake = {"ingredients": "flour sugar eggs", "meal": "dessert", "prep_time": 60}
theSalad = {"ingredients": "avocado arugula tomatoes spinach", "meal": "lunch", "prep_time": 15}
cookbook = {"The Sandwich's": theSandwich, "The Cake's": theCake, "The Salad's": theSalad}

def print_recipe():
    global cookbook
    print()
    for cle in cookbook:
        print(cle)
    print()

def print_details_recipe(name_recipe):
    global cookbook
    for cle,valeur in cookbook.items():
        if cle == name_recipe:
            print("\ndetails of the recipe : " + str(valeur))
            print()
            return 
    print("\nThis recipe don't exist\n")

def delete_recipe(name_recipe):
    global cookbook
    for cle in cookbook:
        if cle == name_recipe:
            cookbook.pop(cle)
            print(f"{name_recipe} a bien etait supprimee")
            return 
    print("\nThis recipe don't exist\n")

def add_recipe():
    global cookbook
    new_recipe = {"ingredients": "" , "meal": "", "prep_time": 0}
    name = input("Enter a name : ")
    new_recipe["ingredients"] = input("Enter ingredients : ")
    new_recipe["meal"] = input("Enter a  meal type : ")
    new_recipe["prep_time"] = input("Enter a preparation time : ")
    add_cook = {name:new_recipe}
    cookbook.update(add_cook)

while 1:
    print("""List of available option:
    1: Add a recipe
    2: Delete a recipe
    3: Print a recipe
    4: Print the cookbook
    5: Quit\n""")

    option = input("Please select an option: \n>> ")

    if option == "1":
        add_recipe()
    elif option == "2": 
        name_recipe = input("Please enter a recipe name to delete it:\n>> ")
        delete_recipe(name_recipe)     
    elif option == "3":  
        name_recipe = input("Please enter a recipe name to get its details:\n>> ")           
        print_details_recipe(name_recipe)
    elif option == "4": 
        print_recipe()
    elif option == "5": 
        print("\nCookbook closed. Goodbye !")  
        quit()
    else:
        print("\nSorry, this option does not exist.\n")   

