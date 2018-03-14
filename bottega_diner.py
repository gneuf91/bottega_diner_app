# Bottega Diner
# You get one entree and two side choices at regular cost.
# - show them the entire menu (print out)
# - waitress suggests a chef’s special, which is a random mix of 1 entree and 2 side choices
# - User selects an entree.
# - “Waitress” makes a comment based on their selection (you ordered this? That’s gross)
# - comment can either be a comparison of the two items, or random comment pulled from a comment vault.
# - Tell them the price
# - repeat the above options for side choices (suggestion and a price, don’t repeat chef suggestion)
# - total up the cost
# Have a breakfast, lunch and dinner menu.  Breakfast has different items, lunch and dinner have the same items but are different prices.
# BONUS: Allow for item customization (how items are prepared, decide addtional cost implications)
# EXTRA BONUS: 3D print out actual food and eat it.


def welcome(choice):
    if choice == "yes":
    menu()
        else:
            print("Thanks for stopping by!")

def menu():
    print("Welcome to Bottega Diner!")
    print("Here is our menu, please keep in mind that all Entrees come with two sides")
    print("Breakfast - Omelet - $10, Biscuits & Gravy - $12, and Pancakes - $8")
    print("Lunch - Sandwich - $10, Hamburger - $12, Chicken Tenders - $10")
    print("Dinner - Pasta - $12, Parmesan Chicken - $12, Roast Beef - $14")
    print("There is also the Chef's Choice of a Hamburger with fries and a milkshake.")

def eat_or_not():
    choice1 = input("Welcome! Would you like to make an order?")
    welcome(choice1)

eat_or_not()




def order(order_total):
    choice2 = input("What will you have?")
    print(choice2, "...that sounds great")
    print("Here are our sides, please choose 2")
    print("Fruit bowl, Steamed Vegetables, Fries, Onion Rings, Salad, Soup, Milkshake, Pudding")
    sid1 = input("Choose a side")
    sid2 = input("Choose another side")
    print(sid1, sid2)
    order_total()


choice2 = ""
sid1 = ""
sid2 = ""


def order_total():
    print("That sounds delicious!")
    print("Your total order is:")
    print({choice2} + {sid1} + {sid2})
    print("...and that will cost:")

order(order_total)
