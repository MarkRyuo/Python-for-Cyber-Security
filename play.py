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

# removeCar = input("Do you want to remove a car in the list (y/n): ")

# if removeCar == "y" or removeCar == "Y" :
#   carRemove = input(f"What car in the list: {car_Brand} : \n")
#   if carRemove in car_Brand :
#     car_Brand.remove(carRemove)
#     print(f"New Car list: {car_Brand}")
#     # End
# else :
#   print(f"Your answer is {removeCar} let's Continue!")
  
  
# Do you want to clear the list or delete 1 of the car in the list 

RemoveOrClear = input("Do you want to remove a car or clear the list (clear/remove) : ")

if RemoveOrClear == "clear" or RemoveOrClear == "Clear" :
  car_Brand.clear() 
  print(f"You list is Cleared: {car_Brand}")
elif RemoveOrClear == "remove" or RemoveOrClear == "Remove" :
  removeCar = input(f"What car you want to remove: {car_Brand} \n")
  if removeCar in car_Brand : 
    car_Brand.remove(removeCar)
    print(f"Updated list of car: {car_Brand}")     
  else:
    print(f"Your Choice is not in the choices")
else:
  print(f"Your Choice is not in the choices")
  