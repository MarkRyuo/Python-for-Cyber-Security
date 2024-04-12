# Create a question for login 

# do you want to login? YES --> Continue if No --> Exit 

question = input("Do you want to login? (yes/no): ") # To-do This code have a issue 

# while not question :
#     question = input("Do you want to login? (yes/no): ") 
#     if question == "yes" :
#         question.lower()
#         # Display the answer 
#         print(f"{question}")
#     elif question == "no" :
#         question.lower()
#         print(f"{question}")
#         exit()
#     else: 
#         print(f"Your answer wrong {question}")
#         exit()



def Question(question) : 
    while not question :
        question = input("Do you want to login? (yes/no): ")
        if question == "yes" :
            question.lower()
            # Display the answer 
            print(f"{question}")
        elif question == "no" :
            question.lower()
            print(f"{question}")
            exit()
        else: 
            print(f"Your answer wrong {question}")
            exit()
    
   

              

Question(question)


