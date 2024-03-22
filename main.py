class House:
    house_data = [
        {"house_id": "DGB2354", "address": "22 Helens Rd", "num_bedrooms": 4, "asking_price": 320000, "area": 240},
        {"house_id": "DGB2355", "address": "2 Aston Crescent", "num_bedrooms": 3, "asking_price": 110000, "area": 190},
        {"house_id": "DGB2356", "address": "5 Stratton St", "num_bedrooms": 5, "asking_price": 550000, "area": 380}
    ]

    def __init__(self, house_id, address, num_bedrooms, asking_price, area):
        self.house_id = house_id
        self.address = address
        self.num_bedrooms = num_bedrooms
        self.asking_price = asking_price
        self.area = area

    def calculate_price_per_area(self):
        return self.asking_price / self.area

    def calculate_price_per_room(self):
        return self.asking_price / self.num_bedrooms

    def show_info(self):
        print(f"ID: {self.house_id}  Address: {self.address}")
        print(f"Number of bedrooms: {self.num_bedrooms}  Asking price: ${self.asking_price}")
        print(f"Price by area ${self.calculate_price_per_area()}")
        print(f"Price per room ${self.calculate_price_per_room()}")
        print("**************")

    @classmethod
    def create_houses(cls):
        houses = []
        for data in cls.house_data:
            house = House(data["house_id"], data["address"], data["num_bedrooms"], data["asking_price"], data["area"])
            houses.append(house)
        return houses

# Example usage:
houses = House.create_houses()
for house in houses:
    house.show_info()
