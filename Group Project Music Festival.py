print("Hello, and thank you for waiting for the ticket presale for The ALTraVerse Music Festival")
print("This year we are hosting the festival at the Las Vegas Festival Grounds in Las Vegas, Nevada")
print("311 W Sahara Ave, Las Vegas, NV 89102")
line_length = 60
horizontal_line = '_' * line_length
print(horizontal_line)

print("For our presale we are selling two types of ticket packages they are listed below:")
option1_name = "Legend Ticket Option"
option1_quantity = 150
option1_cost = 1500

option2_name = "Icon Ticket Option"
option2_quantity = 450
option2_cost = 750
print(f"{option1_name} (Quantity: {option1_quantity}, Cost: ${option1_cost})")
print(f"{option2_name} (Quantity: {option2_quantity}, Cost: ${option2_cost})")
print("**Discounted tickets if purchased as Group**")

line_length = 60
horizontal_line = '_' * line_length
print(horizontal_line)

status_choice = input("Enter you ticket status of choice (Icon Status or Legend Status): ")
if status_choice == "Icon Status":
    print("You have chosen he Icon Status Package.")
    print("This includes the following:")
    print("-Exclusive Front Row Stage Viewing Access")
    print("-Access onto festival grounds & VIP Areas")
    print("-10 Meal Tickets to experience all of our food options")
    print("-Thank YOU SO MUCH, ticket presale begins January 21st 2024. Artist and Perfomers will be anncounced New Years 2024")
elif status_choice == "Legend Status":
    print("You have chosen he Legend Status Package.")
    print("This includes the following:")
    print("-Exclusive Front Row Stage Viewing Access")
    print("-Access onto festival grounds & VIP Areas")
    print("-Luxury Air conditioned restrooms")
    print("-Expedited entry into the festival")
    print("-Unlimited Meals Vouchers to experience all of our food options")
    print("-Thank YOU SO MUCH, ticket presale begins January 21st 2024. Artist and Perfomers will be anncounced New Years 2024")
line_length = 60
horizontal_line = '_' * line_length
print(horizontal_line)
