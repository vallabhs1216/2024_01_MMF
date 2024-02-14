# Calculate the ticket price based on the age
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



while True:

    # Get age (assume users input valid integer)
    age = int(input("Age: "))

    # calculate ticket cost
    ticket_cost = calc_ticket_price(age)
    print(f"Age: {age}, Ticket Price: ${ticket_cost:.2f}")