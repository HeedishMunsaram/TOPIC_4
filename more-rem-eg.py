city_list = ["Seattle", "New York", "Washington", "Houston", "Miami", "San Diego", "Charlotte", "Atlanta", "Boston", "Baltimore"]
print(city_list)

city_to_remove = input("What city should be removed from the list? ")

if city_to_remove in city_list:
    city_list.remove(city_to_remove)
    print(city_list)
else:
    print("That city is not in the list.")