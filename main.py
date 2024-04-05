from bannames import list_ban_names
from coffeelist import Coffee_List
import coffeelist # object may dot(.) notation kapag kinukuha 

# Todo Create a Secure Coffee Shop 
print(list_ban_names)

name = input("Input your name: ")

while not name :
  name = input("Input your name: ")

if name in list_ban_names :
  print("Your Ban, Ngunit kung ikaw ay papasa sa Character Identity Check you can come in!")
  identity_Check1 = input("Are you a good citizen (y/n): ") # if y/Y go to next identity check if n automatically exit
  if identity_Check1 == "y" or identity_Check1 == "Y" :
    identity_Check2 = int(input("How many good way you have: "))
    if identity_Check2 <= 3 :
      print("You're Totally a Ban!")
      exit()
    else :
      print(f"{name} your pass in identity check! Welcome to Arc Coffee Shop")  
  else :
      print("You're Totally a Ban!")    
else :
  print(f"Welcome to Arc Coffee shop {name}")
  
# We need to welcome the costumer and list the coffee we have

print(f"Here the list of coffee: {Coffee_List}")


order = input("What is your order?: ")

americano = "" 

if order in americano["Coffee_name"] :
  print(f"Your order is {americano["Coffee_name"]}")
