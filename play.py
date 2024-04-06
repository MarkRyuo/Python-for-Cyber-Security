# list 
# fruits = ["Banana", "Apple", "Pineapple"]

# List of Methods 
# fruits.insert(3, "Barako")
# fruits.append("Barako")
# print(fruits)
# print(help(fruits))

# Set 
# fruits = {"Banana", "Apple", "Pineapple"}

# Tuple 
# fruits = ("Banana", "Apple", "Pineapple")



# Todo Car Rental

car_Brand = ["Honda", "Toyota", "Bugatti"]
print(f"List of cars to rent: {car_Brand}")

# I'm a admin i need to add some car 

add_car = input("Add Car: ")

if add_car : 
  car_Brand.append(add_car)
  print(f"New List of cars: {car_Brand}") 
else :
  print("Null") 