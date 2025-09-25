class Adress:
    def __init__(self, index, city, street, building, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.building = building
        self. apartment = apartment

    def __str__(self):
        return f"{self.index} {self.city} улица {self.street} дом {self.building} квартира{self.apartment}"

    
        