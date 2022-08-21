class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name {self.restaurant_name} and the cuisine is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The  Restaurant {self.restaurant_name} is open")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, n):
        self.number_served += n

restaurant1=Restaurant("Manchester" , "french")
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

print("*" * 10)

restaurant2=Restaurant("Hesham" , "French")
restaurant3=Restaurant("Hashem" , "Burger")
restaurant4=Restaurant("Hesham Hashem" , "Shawarma")

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant4.describe_restaurant()

print("*" * 10)

restaurant5=Restaurant("Reema" , "Pizza")

print(restaurant5.number_served)
restaurant5.number_served=5
print(restaurant5.number_served)

restaurant5.set_number_served(6)
print(restaurant5.number_served)

restaurant5.increment_number_served(20)
print(restaurant5.number_served)