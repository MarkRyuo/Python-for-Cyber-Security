import userdata 

# Create a question for login 

# do you want to login? YES --> Continue if No --> Exit 

question = input("Do you want to login? (yes/no): ") # To-do This code have a issue 

while not question :
    question = input("Do you want to login? (yes/no): ") 

question.lower()

if question == "yes" :
    # Display the answer 
    print(f"{question}")
elif question == "no" :
    print(f"{question}")
    exit()
else: 
    print(f"Your answer wrong {question}")
    exit()

# Success in Log in 

user = userdata.user
admin = userdata.admin

   
login = input("Enter your username: ")

def Admin(login) :
    if login in admin["username"] :
        # Change
        print("Hello admin:")


Admin(login)

def User(login) :
    if login in user["username"] :
        print(f"Hello User")

User(login)

    

