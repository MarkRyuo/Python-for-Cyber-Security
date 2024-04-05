from bannames import list_ban_names
import coffeelist 

# Todo Create a Secure Coffee Shop 
print(list_ban_names)

name = input("Input your name: ")

while not name :
  name = input("Input your name: ")

if name == "Mark":
  print("Your Ban, Ngunit kung ikaw ay papasa sa Character Identity Check you can come in!")
  identity_Check1 = input("Are you a good citezen (y/n): ")
  if identity_Check1 == "y" or identity_Check1 == "Y" :
    identity_Check2 = input("How many good way you have: ")
    if identity_Check2 <= 3 :
      print
    elif identity_Check2 >= 4: 
      print

elif name == "Ryuo" :
  print("Your Ban, Ngunit kung ikaw ay papasa sa Character Identity Check you can come in!")
  
else :
  print(f"Welcome to Arc Coffee shop {name}")
  
