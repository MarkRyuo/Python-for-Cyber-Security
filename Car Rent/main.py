# Create a question for login 

# do you want to login? YES --> Continue if No --> Exit 

question = input("Do you want to login? (yes/no)") 

while not question :
    question = input("Do you want to login? (yes/no)") 
    if question == "yes" :
        question.lower()
        # Display the answer 
        print(f"{question}")
    elif question == "no"  