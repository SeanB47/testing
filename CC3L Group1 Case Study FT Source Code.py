import pandas as pd #to create DataFrame(df)

class RentalItem:
    def __init__(self, item_number, days):
        self.item_number = item_number
        self.days = days
        self.item_name, self.daily_rate = self.item_Details()
        self.cost = self.daily_rate * self.days  #Mulitplying the days in daily rate of the items
        self.discount = 0.10 if self.days > 7 else 0  #Gives a discount if the days is more than 7
        self.discount_amount = self.cost * self.discount  #Multiplying the cost to the discount
        self.final_price = self.cost - self.discount_amount  #Subtracting the discount to the final cost

    def item_Details(self):
        if self.item_number == 1:
            return "Car", 50
        elif self.item_number == 2:
            return "Gown", 5
        elif self.item_number == 3:
            return "Establishment", 25
        # the if-else condition is to make sure that the item is corresponded with the input number
        else:
            raise ValueError("Invalid item number.") # This will raise an error when you enter an invalid number

    def to_Store(self, rental_number): # This function stores the details for the DataFrame
        return {
            "Rental #": rental_number,
            "Item": self.item_name,
            "Days": self.days,
            "Rate": self.daily_rate,
            "Cost Before Discount": self.cost,
            "Discount Applied": f"{int(self.discount * 100)}%",
            "Final Price": self.final_price
        }

class RentalSystem: # This class is the system itself that you see in the terminal

    def __init__(self):
        self.rental_records = []
        self.total_final_price = 0

    def start(self):
        print("============= Welcome to the Rental System ==============\n")
        print("Items Available: 1) Car ($50/day) \t 2) Gown ($5/day) \t 3) Establishment ($25/day)\n")
        print("=========================================================\n")

        while True: # The while loop is to make a loop when the user made a mistake
            try:
                total_rentals = int(input("How many items would you like to rent? "))
                if total_rentals > 0:
                    break # This will stop the system when the number input is more than 0
                else:
                    print("Please enter a positive number.") # This is when you enter a negative number
            except ValueError:
                print("Invalid input. Please enter a number.") # This is when you enter a string or char

        for i in range(1, total_rentals + 1):
            print(f"\nRental {i}:") # This statement is to loop through each rental

            # This statement prompt if what number you will rent and how many days
            item_number = self.get_valid_input("Enter the number of the item you want to rent (1-3): ", [1, 2, 3]) #This is the valid options
            days = self.get_positive_int(f"Enter the number of days you want to rent the item for: ")

            # The statement creates a RentalItem and stores the data and add to the final price
            rental = RentalItem(item_number, days)
            self.rental_records.append(rental.to_Store(i))
            self.total_final_price += rental.final_price

            # This prints the rental details
            print(f"""
Rental {i} Summary:
- Item: {rental.item_name}
- Duration: {rental.days} days
- Daily Rate: ${rental.daily_rate}
- Total Cost Before Discount: ${rental.cost:.2f}""")
            if rental.discount > 0:
                print(f"A 10% discount is applied. Final price for this rental: ${rental.final_price:.2f}") # If a discount is applied this will print

        self.display_summary(total_rentals)

    # This is for checking if the input is a valid number
    def get_valid_input(self, prompt, valid_options):
        while True:
            try:
                value = int(input(prompt))
                if value in valid_options:
                    return value
                else:
                    print(f"Invalid option. Choose from {valid_options}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # This is to check if the number the user entered is positive
    def get_positive_int(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def display_summary(self, total_rentals): # This function will print the Final Receipt
        print("\n=========== Final Receipt ===========")
        print(f"Total amount for {total_rentals} rentals: ${self.total_final_price:.2f}")

        df = pd.DataFrame(self.rental_records) # This function will print the DataFrame(df)
        print("\n========= Rental Data Table =========")
        print(df)

        self.ask_to_rerun()

    def ask_to_rerun(self): # This function will ask the user if they want to rent more
        while True:
            again = input("\nDo you want to rent more items? (yes/no): ").strip().lower()
            if again in ['yes', 'no']:
                break
            print("Invalid input. Please enter 'yes' or 'no'.")

        if again == 'yes': # If the user input 'yes' it will restart the system and ask again
            print("\nRestarting the rental process...\n")
            self.__init__() # pang reset to
            self.start()
        else:
            print("Thank you for using the Rental System!") # Else it will print this

if __name__ == "__main__":
    system = RentalSystem() # This statement creates the rental system then it starts it
    system.start()