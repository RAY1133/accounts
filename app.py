import random
user_name=input("what is your name")
NO_OF=5
assets = ["Cash and cash equivalents", "Accounts Receivable", "Inventory", "Investments", "PPE (Property, Plant, and Equipment)", "Vehicles", "Furniture", "Patents (intangible asset)"]
liabilities = ["Accounts Payable", "Loans", "Mortgages", "Credit Card Balances", "Lease Obligations"]
game_on=True
while game_on:
    # Select 5 random assets and liabilities
    selected_assets = random.sample(assets, NO_OF)
    selected_liabilities = random.sample(liabilities,NO_OF)

    # Create a dictionary with the selected assets and liabilities as keys
    my_dict = {}
    for item in selected_assets + selected_liabilities:
        # Generate a random number from 10,000 to 10,00,000 that is divisible by 10
        value = random.randint(1000, 100000) * 10
        my_dict[item] = value
    # print(my_dict)
    # Calculate the total value of the assets and liabilities
    total_assets = sum(my_dict[item] for item in selected_assets)
    total_liabilities = sum(my_dict[item] for item in selected_liabilities)
    # print(total_assets,total_liabilities)
    # print("the above values are before ")
    # If the total assets do not equal the total liabilities, adjust the values to make them equal
    if total_assets != total_liabilities and total_liabilities>total_assets:
        diff = total_liabilities - total_assets
        my_dict[selected_assets[len(selected_assets)-1]] += diff
    elif total_assets != total_liabilities and total_liabilities<total_assets:
        diff = total_assets - total_liabilities
        my_dict[selected_liabilities[len(selected_liabilities)-1]] += diff


    total_assets = sum(my_dict[item] for item in selected_assets)
    total_liabilities = sum(my_dict[item] for item in selected_liabilities)
    print(total_assets,total_liabilities)
    print(selected_assets)
    print(selected_liabilities)


    # Create the balance sheet variable and add the assets and liabilities to it
    balance_sheet = {"Assets": selected_assets, "Liabilities": selected_liabilities}

    # Shuffle the items in the balance sheet

    random.shuffle(balance_sheet["Assets"])
    random.shuffle(balance_sheet["Liabilities"])


    # Print the balance sheet
    print("Balance Sheet:")

    # Print the header row
    print("{:<40s} {:>20s}".format("Item", "Value"))

    # Print a line to separate the header from the data
    print("-" * 60)

    # Loop through the assets and liabilities and print each one

    for item in balance_sheet["Assets"]:
        print("{:<40s} {:>20,d}".format(item, my_dict[item]))

    # Print a line to separate the assets from the liabilities
    # print("=" * 60)

    for item in balance_sheet["Liabilities"]:
        print("{:<40s} {:>20,d}".format(item, my_dict[item]))


    user_answer=int(input("Enter the final tallied balance sheet amount you got"))
    students_who_got_the_answer_right=[]
    if user_answer==total_assets:
        print("Congrats you solved the sum correctly")
        students_who_got_the_answer_right.append(user_name)
        game_on=False

    else:
        game_on=True
