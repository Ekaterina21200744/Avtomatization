s = int(input ("Введите номер месяца:"))

def month_to_season(s):
    if 1 <= s <= 2 or s ==12:
         return ("Зима")
    elif 3 <= s <= 5:
        return ("Весна")
    elif 6 <= s <= 8:
        return ("Лето")
    elif 9 <= s <= 11:
        return ("Осень")
    else: print ("Неверный месяц")
result = month_to_season(s)
print (result)
    
month_to_season(s)


    
s = int(input ("Введите номер месяца:"))

def month_to_season(s):
    if s in range(1,2) or s ==12:
         return ("Зима")
    elif s in range(3,6):
        return ("Весна")
    elif s in range(6,9):
        return ("Лето")
    elif s in range(9,12):
        return ("Осень")
    else: print ("Неверный месяц")
result = month_to_season(s)
print (result)

month_to_season(s)


