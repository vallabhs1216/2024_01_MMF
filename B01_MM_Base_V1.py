import pandas
import random
from datetime import date


# Functions go here

# Shows instructions
def show_instructions():
    print('''\n
***** Instructions *****

For each ticket, enter ...
- The person's name (can't be blank)
- Age (between 12 and 120)
- Payment method (cash / credit)

When you have entered all the users, press 'xxx' to quit.

The program will then display the ticket details
including the cost of each ticket, the total cost
and the total profit.

This information will also be automatically written to
 a text file.
 
 ******************************''')


# Checks that response is not blank.
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


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


# Checks that users enter a valid response (e.g. yes / no, cash / credit) based on a list of options
def string_checker(question, num_letters, valid_responses):
    error = f"Please choose {valid_responses[0]} or {valid_responses[1]}"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item


# currency formatting function
def currency(x):
    return f"${x:.2f}"


# Main routine


# Set maximum number of tickets below
MAX_TICKETS = 5
tickets_sold = 0

# Valid response lists
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Lists to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

# Dictionary used to create data frame ie: column_name:list
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

# Asks user if they want instructions
want_instructions = string_checker("Do you want to read the instructions (y/n): ", 1, yes_no_list)

# If they yes, output 'display instructions'
# If they no, output 'program continues'

if want_instructions == "yes":
    show_instructions()

print()

# Loop to sell tickets

while tickets_sold < MAX_TICKETS:

    name = not_blank("Enter your name (or 'xxx' to quit) ")

    if name == 'xxx' and len(all_names) > 0:
        break
    elif name == 'xxx':
        print("You must sell at least ONE ticket before quitting")
        continue

    # Asks user for age
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
    print(f"Ms G said you chose {pay_method}")

    if pay_method == "cash":
        surcharge = 0
    else:
        # Calculate 5% surcharge for users paying with credit card
        surcharge = ticket_cost * 0.05

    tickets_sold += 1

    # add ticket name, cost and surcharge to lists
    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)

# Create data frame from dictionary to organise information
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# Calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Choose winner amd look up total won
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# Currency formatting (uses currency function)
add_dollars = ["Ticket Price", 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# ser index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')

# **** Get current date for heading and filename ****

# Get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = f"\nMini Movie Fundraiser Ticket Data {day}/{month}/{year}"
filename = f"MMF_{year}_{month}_{day}"

mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# Create strings for printing
ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
total_ticket_sales = f"Total Ticket Sales: {total:.2f}"
total_profit = f"Total Profit: {profit:.2f}"

# Show users how many tickets have been sold
if tickets_sold == MAX_TICKETS:
    sales_status = "\n*** All the tickets have been sold ***"
else:
    sales_status = f"\n**** You have sold {tickets_sold} out of {MAX_TICKETS} " \
                   f"tickets ****"

# Outputs raffle results
winner_heading = "\n---- Raffle Winner ----"
winner_text = f"The winner of the raffle is {winner_name}. " \
              f"They have won ${total_won:.2f} ie: Their ticket is" \
              f" free!"

# List holding content to print / write file
to_write = [heading, mini_movie_string, ticket_cost_heading,
            total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]

# Print output
for item in to_write:
    print(item)

# write output to file
# Create file to hold data (add .txt extension)
write_to = f"{filename}.txt"
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# Close file
text_file.close()

print()
# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")

else:
    print(f"You have sold {tickets_sold} ticket/s. There is {MAX_TICKETS - tickets_sold} ticket/s remaining")
