city_list = ["Seattle", "New York", "Washington", "Houston", "Miami", "San Diego", "Charlotte", "Atlanta", "Boston", "Baltimore"]

option = int(input("1-Add a city, 2-Remove a city, 3-Insert a city, Please enter 1, 2, or 3: "))

if option == 1:
    print("This option allows you to add a city to the end of the list.")
    print(city_list)
    city = input("What city would you like to add to the list? ")
    city_list.append(city)
    print(city_list)

elif option == 2:
    print("This option allows you to remove a city from the list.")
    print(city_list)

    city_to_remove = input("What city should be removed from the list? ")

    if city_to_remove in city_list:
        city_list.remove(city_to_remove)
        print(city_list)
    else:
        print("That city is not in the list.")

elif option == 3:
    print("This option allows you to insert a city in a specific position on the list.")
    city = input("What city would you like to add to the list? ")
    position = int(input("Where on the list would you like to add it? "))

    if position < len(city_list):
        city_list.insert(position, city)
        print(city_list)
    else:
        print("Invalid Position")