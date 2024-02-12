

# ask the user if they have played before
want_instructions = input("Do you want instructions? ").lower()

# If they say yes, output 'display instructions'
# If they say no, output 'program continues'
# If they say anything else, outputs error

if want_instructions == "yes" or want_instructions == "y":
    print("Instructions")

elif want_instructions == "no" or want_instructions == "n":
    print("Program continues")

else:
    print("Please answer yes / no")