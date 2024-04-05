from bannames import list_ban_names
import coffeelist 

# Todo Create a Secure Coffee Shop 
print(list_ban_names)

name = input("Input your name: ")

while not name :
  name = input("Input your name: ")

if name == "Mark" :
  print("Your Ban, Ngunit kung ikaw ay papasa sa Character Question, Makakapasok ka")
else :
  print(f"Welcome to Arc Coffee shop {name}")
  
