# functions go here

# Checks the input given byt he user is an integer
def num_checker(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("please enter an integer")
        
        

# Checks that response is not blank
def not_blank(question):

    while True:
        respose = input(question)

        if respose == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return respose
            

# Main routine goes here
tickets_sold = 0

while True:

    
            
    # Loop to sell tickets

    name = not_blank("Enter your name (or 'xxx' to quit) ")
    

    if name == 'xxx':
        break

    # Asks user for age, 
    age = num_checker("Age: ")

    if 12 <= age <= 120:
        pass

    elif 12 > age:
        print("Sorry you are too young for this movie")
        continue

    else:
        print("That looks like a typo, please try again.")
        continue


    tickets_sold += 1

print(f"You have sold {tickets_sold} ticket/s.")    
