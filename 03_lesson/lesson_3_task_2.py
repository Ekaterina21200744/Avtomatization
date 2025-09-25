from smartphone import Smartphone

catalog = [
    Smartphone ("Iphone", "17ProMax", "+79880000101"),
    Smartphone ("Samsung", "GalaxyS50", "+79880000102"),
    Smartphone ("Honor", "X9C", "+79880000103"),
    Smartphone ("Simens", "A50", "+79880000104"),
    Smartphone ("Nokia", "75", "+79880000105")
  
]

for Smartphone in catalog:
    print(f"{Smartphone.brand} - {Smartphone.model}. {Smartphone.number_phone}")

