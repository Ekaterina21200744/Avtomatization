def if_year_lear (year):
    
    return True if year % 4 ==0 else False

year = int(input ("Введите год:"))   
result = if_year_lear(year)
print(f"Год {year}: {result}")





