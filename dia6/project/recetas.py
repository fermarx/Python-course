from distutils.command.clean import clean
from pathlib import Path
from os import rmdir, system
import os
import string

base = Path.home()
username = str(base).split("\\")[-1]
path = Path(base, "OneDrive", "Documentos", "curso_python", "dia6", "project", "Recetas")

def init():
    n_recipes = 0

    for n in Path(path).glob("**/*.txt"):
        n_recipes += 1

    system("cls")
    print(f"\nHello {username}.\nThe recipes are stored in {path}\nYou have {n_recipes} recipes.\n")


def menu():
    inp = "Choose an option:\n"

    options = ["Read recipe", "Create recipe", "Create category", "Delete recipe", "Delete category", "End program"]

    for n in range(0, len(options)):
        inp += f"[{n+1}] - {options[n]}\n"
    inp += ">>> "

    option = input(inp)
    if option.isnumeric() == False:
        print("Enter a number.")
        return 0
    
    option = int(option)
    if option < 1 or option > len(options):
        return 0

    return option


def choose_category():
    inp = "Choose a category:\n"

    categ = next(os.walk('Recetas'))[1]

    for n in range(0, len(categ)):
        inp += f"[{n+1}] - {categ[n]}\n"
    inp += ">>> "

    option = input(inp)
    if option.isnumeric() == False:
        print("Enter a number.")
        return ""
    
    option = int(option)
    if option < 1 or option > len(categ):
        return ""

    system("cls")
    return categ[option-1]


def choose_recipe(path):
    inp = "Choose a recipe:\n"

    recipes = next(os.walk(path))[2]

    for n in range(0, len(recipes)):
        n_path = Path(path, recipes[n])
        inp += f"[{n+1}] - {n_path.stem}\n"
    inp += ">>> "

    option = input(inp)
    if option.isnumeric() == False:
        print("Enter a number.")
        return ""
    
    option = int(option)
    if option < 1 or option > len(recipes):
        return ""

    system("cls")
    return recipes[option-1]


def read_recipe():
    category = ""
    recipe = ""

    while category == "":
        category = choose_category()
        if category == "":
            system("cls")
            print("Choose a valid option.") 
    
    while recipe == "":
        recipe = choose_recipe(Path(path, category))
        if recipe == "":
            system("cls")
            print("Choose a valid option.") 
    
    pf = open(Path(path, category, recipe))
    print(pf.read())
    input("\n\nPress enter to continue with other recipes.")
    pf.close()
    system("cls")


def create_recipe():
    category = ""
    
    while category == "":
        category = choose_category()
        if category == "":
            system("cls")
            print("Choose a valid option.") 
    
    name = input("Name of your recipe: ")
    pf = open(Path(path, category, name), "w")
    inp = input("Create your recipe:\n")
    pf.write(inp)
    pf.close()
    system("cls")


def create_category():

    name = input("Name of your new directory: ")
    n_path = Path(path, name)
    os.makedirs(n_path)
    print(f"Directory {name} created.")


def delete_recipe():

    category = ""
    recipe = ""

    while category == "":
        category = choose_category()
        if category == "":
            system("cls")
            print("Choose a valid option.") 
                
    while recipe == "":
        recipe = choose_recipe(Path(path, category))
        if recipe == "":
            system("cls")
            print("Choose a valid option.") 
    
    name = Path(path, category, recipe).stem

    sure = input(f"Are you sure you want to delete {name.upper()}?\nPress Y for Yes or N for no. ")
    print(sure)
    if sure.lower() == "y":
        os.remove(Path(path, category, recipe))
        print("Recipe deleted.")  
    elif sure.lower() == "n":
        print("Recipe not deleted.")
    else: 
        print("Command not understood")


def delete_category():
    category = ""

    while category == "":
        category = choose_category()
        if category == "":
            system("cls")
            print("Choose a valid option.") 

    sure = input(f"Are you sure you want to delete {category.upper()}?\nPress Y for Yes or N for no.")
    if sure.lower() == "y":
        n_path = Path(path, category)
        rmdir(n_path)
        print("Directory deleted.")
    elif sure.lower() == "n":
        print("Directory not deleted.")
    else: 
        print("Command not understood")


def main():
    option = 0

    init()
    
    while option != -1:
        option = menu()
        if option == 0:
            system("cls")
            print("Choose a valid option.") 
        
        system("cls")
        if option == 1:
            read_recipe()

        elif option == 2:
            create_recipe()

        elif option == 3:
            create_category()
            
        elif option == 4:
            delete_recipe()
            
        elif option == 5:
            delete_category()
            
        elif option == 6:
            print(f"Thanks for using us! See you soon {username}.")
            break
        else: 
            print("Choose a valid option.")

            
if __name__ == "__main__":
    main()