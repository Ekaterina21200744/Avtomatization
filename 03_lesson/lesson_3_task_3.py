from address import Adress
from mailing import Mailing

from_adress = Adress("125849", "Москва","Большая садовая", "302-бис", "50")
to_adress = Adress("125965", "Москва", "Мансуровский переулок", "10", "1")
track = '5012635178'
cost = 2500



mailing = Mailing(from_adress, to_adress, track, cost)

print(f"Отправление", track, "из", from_adress.index, ",", from_adress.city, ",", from_adress.street, ",", from_adress.building, "-", from_adress.apartment, "в", to_adress.index, ",", to_adress.city, ",", to_adress.street, ",", to_adress.building, "-", to_adress.apartment, "."  "Стоимость", cost, "рублей" )