# store mangager


# Instructions

# * Create a dictionary that has a few items already stored.

# * Prompt the user is they would like to add a new item, remove an existing one, or to display all the items currently in stock.

# * If the user would like to add a new item, ask what they would like to add and how many. Add the results to your dictionary.

# * If the user wants to remove and item, first check if that item is available then remove that item from the dictionary.

# * If the user want to display the result print out an easy to read list of all the items and amount to the console.


store_items = {
    "footballs": 20,
    "basketballs": 2,
    "shorts": 80,
    "bats": 2
}
manage_system = "y"

# Run the code so long as the user wants to manage the systm
while manage_system == "y":

    # Take users input
    action_item = input(
        "What would like to do today? (A)dd new item, (R)emove an item, or (S)how all items ")

    if action_item == "A":

        # Input item to add
        item_added = input("What would you like to add? ")
        amount_added = input("How many would you like to add? ")

        # Add item to dictionary
        store_items[item_added] = amount_added

        # Print confirmation
        print(item_added + " " + amount_added + " added!")

    elif action_item == "R":

        # Input item to be removed
        item_removed = input("Which item would you like to be removed? ")

        # Check if item exists
        if item_removed in store_items:

            # Remove item
            del store_items[item_removed]

            # Print confirmation
            print(item_removed + " has been removed! ")

        # Print error if item is does not exist
        else:
            print("That item does not exist")

    elif action_item == "S":

        print("Store inventory")
        print("----------")

        # Iterate through all keys and values
        for key, value in store_items.items():

            # Print all items
            print(key + ": " + str(value))
        print("----------")

    else:
        print("Sorry the action is not available")

    # Check if the user wants to continue working within the system
    manage_system = input("Would you like to continue working? (y)es or (n)o ")
