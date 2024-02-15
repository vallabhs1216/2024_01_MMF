# Functions go here

# Checks that response is not blank.
def not_blank(question):

    while True:
        respose = input(question)

        if respose == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return respose

# Checks the input given byt he user is an integer.
def num_checker(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("please enter an integer")

# Calculate the ticket price based on the age.
def calc_ticket_price(var_age):
    
    # Ticket is $7.50 for users under 16
    if var_age <= 15:
        price = 7.5

    # Ticket is $10.50 for users under 65
    elif var_age <= 64:
        price = 10.5

    # Ticket is $6.50 for users 65 and over
    else:
        price = 6.5
    
    return price

# Checks that users enter a valid response (eg yes / no, cash / credit) based on a list of options

def string_checker(question, num_letters, valid_responses):
    
    error = f"Please choose {valid_responses[0]} or {valid_responses[1]}"
    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item
                
        print(error)
 

# Main routine
        


# Set maximum number of tickerss below
MAX_TICKETS = 3
tickets_sold = 0

# Valid response lists
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Asks user if they want instructions

want_instructions = string_checker("Do you want to read the instructions (y/n): ", 1, yes_no_list)

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

    # Calculates ticket cost        

    ticket_cost = calc_ticket_price(age)
    
    # Get payment method
    pay_method = string_checker("Choose a payment method (cash / credit): ", 2, payment_list)

    tickets_sold += 1
        
# Output number of tickets sold

if tickets_sold == MAX_TICKETS:
    print("Comgratulations you have sold all the tickets")
else:
    print(f"You have sold {tickets_sold} ticket/s. There is {MAX_TICKETS - tickets_sold} ticket/s remaining")