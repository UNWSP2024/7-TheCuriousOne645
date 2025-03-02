def rainfall():
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    rainfall_data = []
    
    for month in months:
        rainfall = float(input(f"Enter the total rainfall for {month}: "))
        rainfall_data.append(rainfall)
    
    total_rainfall = sum(rainfall_data)
    average_rainfall = total_rainfall / 12
    max_rainfall = max(rainfall_data)
    min_rainfall = min(rainfall_data)
    max_month = months[rainfall_data.index(max_rainfall)]
    min_month = months[rainfall_data.index(min_rainfall)]
    
    print(f"\nTotal rainfall for the year: {total_rainfall} inches")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
    print(f"Month with the highest rainfall: {max_month} ({max_rainfall} inches)")
    print(f"Month with the lowest rainfall: {min_month} ({min_rainfall} inches)")

rainfall()
