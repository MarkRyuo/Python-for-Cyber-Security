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
  
# remove a car in the list and print the new list 

removeCar = input("Do you want to remove a car in the list (y/n): ")

if removeCar == "y" or removeCar == "Y" :
  carRemove = input(f"What car in the list: {car_Brand} : \n")
  if carRemove in car_Brand :
    car_Brand.remove(carRemove)
    print(f"New Car list: {car_Brand}")
    # End
else :
  print(f"Your answer is {carRemove} let's Continue!")