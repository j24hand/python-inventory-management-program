# Jake Hand
# Program 10:Inventory
# COP 2500
# November 23,2024


def menu():
    # 5 prints - main menu + 4 options
    print("Main Menu")
    print("1. Increase Inventory")
    print("2. Decrease Inventory")
    print("3. View Inventory")
    print("4. Quit")
    choice = int(input("What would you like to do?\n"))
    return choice

def increase(inventory):
    # Prompt the user for the name of the game
    inc_game_name = input("What game are you purchasing?\n")
    # Prompt the user for how many we are adding
    inc_game_num = int(input("How many are you purchasing?\n"))
   
    # If the game is in the dictionary
    if inc_game_name in inventory:
        # We will add the current amount with the amount we are adding.
        inventory[inc_game_name] += inc_game_num
    else:
        # Add the game to the dictionary with the amount we are adding
        inventory[inc_game_name] = inc_game_num

def decrease(inventory):
    # Prompt the user for the name of the game
    dec_game_name = input("What game are you selling?\n")
    # Prompt the user for how many we are removing
    dec_game_num = int(input("How many are you selling?\n"))
   
    # If the game is NOT in the dictionary
    if dec_game_name not in inventory:
        print("We do not have that game.")
    else:
        # Check to see if we have that many games, if we do:
        if inventory[dec_game_name] >= dec_game_num:
            # Subtract that many games from the dictionary
            inventory[dec_game_name] -= dec_game_num
            print("Successfully removed the games.")
            # Check to see if the new value of the game is zero
            if inventory[dec_game_name] == 0:
                # Delete the game from the dictionary
                del inventory[dec_game_name]
        else:
            # Otherwise:
            print("We don't have that many games.")
            X = dec_game_num
            Y = dec_game_name
            Z = dec_game_num
            print("You do not have", X ,"copies of",Y, "in stock. You sold",Z,"of them.")

def view_inventory(inventory):
    # Create an on sale list, and low stock list both will be empty
    on_sale = []
    low_stock = []
   
    # Print the header message
    print("Current Inventory:")
   
    # Loop over key in the dictionary
    for game, quantity in inventory.items():
        # Print out the key and value
        print(f"{game}: {quantity}")
        # If the value is less than maybe equal to 100
        if quantity <= 100:
            # Add it to the low stock list
            low_stock.append(game)
        # If the value is greater than maybe equal to 1000
        elif quantity >= 1000:
            # Add it to the on sale list
            on_sale.append(game)
   
    # Print out the header for the low stock
    print("\nLow Stock Warning(s):")
    # Loop over the low stock list
    for game in low_stock:
        # Print out each value
        print(game)
       
    # Print the header for the on sale
    print("\nSale Recommendations:")
    # Loop over the on sale list
    for game in on_sale:
        # Print out each value
        print(game)


def main():
    # Create a dictionary that stores all the games and how many we have.
    inventory = {}
   
    # Call menu and save the result
    option = menu()
    while option != 4:
        if option == 1:
            increase(inventory)
        elif option == 2:
            decrease(inventory)
        elif option == 3:
            view_inventory(inventory)
       
        # Call the menu and save the result
        option = menu()

main()
