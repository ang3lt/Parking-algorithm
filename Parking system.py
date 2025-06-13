# Initializing variables

option = 0  # The option for the main menu selection
hours = 0  # The variable to store the number of hours for parking

# Dictionary of parking slots: keys represent parking spots, values represent their current status
# "FREE" indicates the spot is available, else it's occupied by a registration number

slots = {"1": "HK73LGN",    # Slot 1 is occupied by "HK73LGN"
         "2": "PL74DTO",    # Slot 2 is occupied by "PL74DTO"
         "3": "FREE",       # Slot 3 is available
         "4": "FREE",       # Slot 4 is available
         "V1": "LX06OYC",   # VIP Slot 1 is occupied by "LX06OYC"
         "V2": "FREE"}      # VIP Slot 2 is available

# Function to validate the car's registration number
def reg_validation():
    flag = True  # Flag to control the while loop for validation
    while flag:
        reg = input("Please enter your car registration: ")  # Input registration number from user
        # Check if the registration is 7 characters long and alphanumeric
        if len(reg.strip()) == 7 and (reg.strip()).isalnum():
            flag = False  # Stop the loop if valid registration number
        else:
            print("Please enter a valid registration plate in the format XX00XXX ")  # Error message for invalid input
            flag = True  # Keep the loop running if invalid registration
    return reg  # Return the valid registration number



# Function to handle parking a car
def park_car(reg, hours, slots):
    flag = True  # Flag to control the while loop
    while flag:
        spot = input("Please input the parking space of your choice: ")  # Ask user to choose a spot
        if slots[spot] == "FREE":  # Check if the chosen spot is free
            slots.update({spot: reg})  # If free, update the slot with the registration number
            if spot == "V1" or spot == "V2":  # Check if the spot is a VIP parking spot
                total = hours * 5  # VIP spots cost £5/hr
            else:
                total = hours * 2.50  # Normal spots cost £2.50/hr
            flag = False  # Exit the loop after parking
            print("Your total will be £" + str(total) + ".")  # Display the total cost
        else:
            print("Unfortunately this spot isn't free, please choose another one! ")  # Error message if the spot is taken
    return total  # Return the total cost for parking



# Function to handle removing a car (checking out)
def remove_car(spot, reg, slots):
    flag = True  # Flag to control the while loop
    while flag:
        if slots[spot] == reg:  # Check if the spot is occupied by the car with given registration
            slots.update({spot: "FREE"})  # Mark the spot as free after removing the car
            print("####### Thank you for choosing us! ########")  # Confirmation message
            flag = False  # Exit the loop
        else:
            print("Sorry, please make sure you have entered the registration and parking space correctly! ")  # Error message if incorrect details

            flag = True  # Continue the loop if registration or spot is incorrect




while option != 5:  # Loop until option 5 (Exit) is selected
    print(" ")
    print("""############ Main menu: #############
      1. Register a car entering
      2. Register a car leaving
      3. View available spots
      4. View pricing
      5. Exit""")  # Display the main menu options

    try:
        option = int(input("Please enter your choice here: "))  # Get the menu option from user input
    except ValueError:
        print("#############################")
        print("Please make sure you enter a number! ")  # Error if input is not a valid number
        print("#############################")

    
    
    # Error handling if the option is out of valid range (1 to 5)
    if option < 1 or option > 5:
        print("#############################")
        print("Please make sure your choice is between 1 and 5! ")
        print("#############################")

    
    
    if option == 1:  # If option 1 is chosen, register a car entering
        reg = reg_validation()  # Validate car registration
        try:
            hours = int(input("Please enter the length of your stay in hours: "))  # Get number of hours for parking
        except ValueError:
            print("Please make sure you enter a number! ")

        print("""############ Choose one of the following slots ###########""")
        print(slots)  # Show available parking slots

        park_car(reg, hours, slots)  # Call function to park the car and calculate total cost

    
    
    elif option == 2:  # If option 2 is chosen, register a car leaving
        reg = reg_validation()  # Validate the car registration
        spot = input("Please input the parking space you parked in: ")  # Get the spot where the car is parked
        
        remove_car(spot, reg, slots)  # Call function to remove the car

    
    
    elif option == 3:  # If option 3 is chosen, show available spots
        print("##########################")
        print(slots)  # Display the current state of parking slots
        print("##########################")
        
    
    
    elif option == 4:  # If option 4 is chosen, show pricing details
        print("""########################## Price list ##########################
                1. Normal parking spots: £2.50/hr
                2. VIP parking spots £5/hr 
                ###################################################################
                """)
