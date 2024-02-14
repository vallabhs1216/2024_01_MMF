# Functions go here
def cash_credit(question):

    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            return "cash"

        elif response == "credit" or response == "cr":
            return "credit"  
                
        else:
            print("Please choose a valid payment method")

# Main routine


# Ask the user if they have played before
while True:
    payment_method = cash_credit("Choose a payment method (cash pr credit): ").lower()
