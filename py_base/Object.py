# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sit(self):
#         print(f"{self.name} is now sitting")
#     def roll_over(self):
#         print(f"{self.name} rolled over")


# bal = Dog("bal", 2)
# bal.sit()
# bal.roll_over()

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    
    def describe_restaurant(self):
        print(f"There are {self.restaurant_name} have {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"restaurant is openning")

my_restaurant = Restaurant("BIL", "chinese_style")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()




from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)



