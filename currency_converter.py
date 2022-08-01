print("This is a currency converter")

while True:
    menu = int(input("What conversion would you like to do?" +
                     "\n1. Naira to Dollars" +
                     "\n2. Dollars to Naira" +
                     "\nPlease select an option: "))
    naira_per_dollar = 720
    if (menu == 1):
        naira = float(input("Please enter amount in Naira: "))
        no_of_dollars = round(naira / naira_per_dollar, 2)
        print(str(naira) + " Naira is equivalent to " + str(no_of_dollars) + " Dollars")
        options = input("\nDo you want to do another conversion (yes/no)?: ")
        if (options == "yes"):
            continue
        else:
            break

    elif (menu == 2):
        dollars = float(input("Please enter amount in dollars: "))
        no_of_naira = round(dollars * naira_per_dollar, 2)
        print(str(dollars) + " Dollars is equivalent to " + str(no_of_naira) + " Naira")
        options = input("\nDo you want to do another conversion (yes/no)?: ")
        if (options == "yes"):
            continue
        else:
            break
    else:
        print("Please enter a valid option\n")
        continue
                
