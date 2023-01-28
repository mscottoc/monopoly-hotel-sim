# 1. Name:
#      M. Scott O'Connor
# 2. Project Name:
#      Lab 04: Monopoly
# 3. Project Description:
#      This program will determine if you are able to place a hotel on Pennsylvania Avenue
#      in a game of monopoly.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of making this program was was the planning before hand. Once I got
#      decision tree on paper the program was simple to code.
# 5. How long did it take for you to complete the project?
#      1hr
# 6. Youtube demo
#      https://youtu.be/Qyfn_7WKG68
while True:
    own_all = input("Do you own all green properties? (y/n)\n> ")
    if own_all == 'y' or own_all == 'Y' or own_all == "yes":
        own_all = True
        break
    elif own_all == 'n' or own_all == 'N' or own_all == "no":
        own_all = False
        break
    else:
        print("\tNot a valid input")

if not own_all:
    print("Must own all green properties")
else:
    pc = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel)\n> "))

    nc = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel)\n> "))

    pa = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel)\n> "))

    b_houses = int(input("How many houses are in the bank?\n> "))

    b_hotels = int(input("How many hotels are in the bank?\n> "))

    cash = int(input("How much money do you have to spend?\n> $"))

    if pa == 5:
        print("There is already a house on Pennsylvania Avenue. You cannot have more.\n")
    elif nc == 5:
        print("Swap North Carolina's hotel with Pennsylvania's 4 houses.\n")
    elif pc == 5:
        print("Swap Pacific's hotel with Pennsylvania's 4 houses.\n")
    else:
        houses_needed = 12 - (pa + nc + pc)
        price = houses_needed * 200 + 200

        if cash < price:
            print("You do not have sufficient funds to purchase a hotel at this time.\n")
        elif b_houses < houses_needed:
            print("There are not enough houses available for purchase at this time.\n")
        elif b_hotels < 1:
            print("There are not enough hotels available for purchase at this time.\n")
        else:
            print("This will cost $" + str(price) + '.')
            print("\tPurchase 1 hotel and", houses_needed, "house(s).")
            print("\tPut 1 hotel on Pennsylvania and return any houses to the bank.")
            if nc < 4:
                print("\tPut", 4 - nc, "house(s) on North Carolina.")
            if pc < 4:
                print("\tPut", 4 - pc, "house(s) on Pacific.")
