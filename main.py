from bannames import list_ban_names

# Todo Create a Secure Coffee Shop 

name = input("Input your name: ")

while not name :
  name = input("Input your name: ")

if name == "Mark" :
  print("Your Ban!")
else :
  print(f"Welcome Here {name}")