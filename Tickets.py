"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""
#Humza Bangash Tickets.py


# Create list of seats 1–20
seats = list(range(1, 21))

print("🎟️ Welcome to the Ticket Sales System!")

# Loop until user quits or seats are empty
while seats:

    print("\nAvailable Seats:")
    print(seats)

    try:
        choice = int(input("\nEnter seat number to purchase (0 to quit): "))

        # Quit option
        if choice == 0:
            print("Thank you for visiting!")
            break

        # Seat exists and available
        elif choice in seats:
            seats.remove(choice)
            print(f"✅ Seat {choice} successfully purchased!")

        # Seat number invalid or already taken
        else:
            print("❌ Invalid selection. Seat does not exist or is already taken.")

    except ValueError:
        print("❌ Please enter a valid number.")

# If all seats sold
if not seats:
    print("\n🎉 All seats are sold out!")