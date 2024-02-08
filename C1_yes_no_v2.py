# Functions go here
def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"  
                
        else:
            print("Please answer yes / no")

# Main routine


# Ask the user if they have played before
while True:
    want_instructions = yes_no("Do you want  instructions? ").lower()

    # If they say yes, output 'display instructions'
    # If they say no, output 'program continues'
    # If they say anything else, outputs error

    if want_instructions == "yes":
        print("Instructions")


    print("program continues")
    print()
        