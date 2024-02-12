# Function goes here

# Checks that response is not blank
def not_blank(question):

    while True:
        respose = input(question)

        if respose == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return respose


# Main routine
while True:
    name = not_blank("Enter your name (or 'xxx' to quit) ")
    if name == "xxx":
        break

print("Finish")