# Main routine starts here

# Set maximum number of tickerss below
MAX_TICKETS = 3

# Loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("Please enter your name or 'xxx' to quit: ")
    

    if name == 'xxx':
        break

    tickets_sold += 1
    
# Output number of tickets sold

if tickets_sold == MAX_TICKETS:
    print("Comgratulations you have sold all the tickets")
else:
    print(f"You have sold {tickets_sold} ticket/s. There is {MAX_TICKETS - tickets_sold} ticket/s remaining")