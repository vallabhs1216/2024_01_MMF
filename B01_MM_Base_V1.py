# Functions go here

# Checks user has entered yes / no to a question
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"  
                
        else:
            print("Please answer yes / no")

# Checks that response is not blank
def not_blank(question):

    while True:
        respose = input(question)

        if respose == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return respose

# Checks the input given byt he user is an integer
def num_checker(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("please enter an integer")
        
        

# Main routine
        


# Set maximum number of tickerss below
MAX_TICKETS = 3
tickets_sold = 0

# Asks user if they want instructions

want_instructions = yes_no("Do you want  instructions? ").lower()

# If they yes, output 'display instructions'
# If they no, output 'program continues'

if want_instructions == "yes":
    print("Instructions")

print()

        
# Loop to sell tickets

while tickets_sold < MAX_TICKETS:

    name = not_blank("Enter your name (or 'xxx' to quit) ")
    

    if name == 'xxx':
        break

    # Asks user for age, 
    age = num_checker("Age: ")

    if 12 <= age <= 120:
        pass

    elif age < 12:
        print("Sorry you are too young for this movie")
        continue
    
    else:
        print("That looks like a typo, please try again.")
        continue


    tickets_sold += 1
    
# Output number of tickets sold

if tickets_sold == MAX_TICKETS:
    print("Comgratulations you have sold all the tickets")
else:
    print(f"You have sold {tickets_sold} ticket/s. There is {MAX_TICKETS - tickets_sold} ticket/s remaining")