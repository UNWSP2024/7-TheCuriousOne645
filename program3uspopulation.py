def us_population():
    data = []
    while True:
        year = int(input("Enter the year: "))
        state = input("Enter the state: ")
        population = int(input("Enter the population: "))
        data.append([year, state, population])
        
        cont = input("Do you want to add more data? (yes/no): ")
        if cont.lower() != "yes":
            break
    
    search_year = int(input("Enter the year to calculate total population: "))
    total_population = sum([item[2] for item in data if item[0] == search_year])
    
    print(f"Total population for the year {search_year}: {total_population}")

us_population()
