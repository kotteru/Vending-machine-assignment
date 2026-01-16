# Class assignment - Vending Machine
# Write Vending machine using python OOPs concept with below functionalities
# 1. Display items available in the vending machine with their prices and quantities.   
# 2. Allow users to select an item by entering its code.
# 3. Check if the selected item is in stock. If not, display an appropriate
#    message and allow the user to make another selection.
# 4. Prompt the user to enter the amount of money they are inserting into the machine
# 5. Check if the inserted amount is sufficient to purchase the selected item.
#    If not, display an appropriate message and allow the user to insert more money or cancel
# 6. Dispense the item and provide change if necessary.



class VendingMachine:                                                                               # class representation of vending machine
    def __init__(self):                                                                             # initializes the vending machine with items, prices, and stock
        self.items = {
            'A1': {'name': 'Coca Cola', 'price': 4.99, 'stock': 10},                                # Dictionary that stores all item codes, names, prices, and stock quantities
            'A2': {'name': 'Bebsi', 'price': 4.89, 'stock': 8},
            'A3': {'name': 'Monster energy', 'price': 9.49, 'stock': 5},
            'A4': {'name': 'Black Coffee', 'price': 12.79, 'stock': 9},
            'A5': {'name': 'Spanish Latte', 'price': 11.79, 'stock': 15},
            'A6': {'name': 'Pocari Sweat', 'price': 5.49, 'stock': 20},
            'A7': {'name': 'Bottled Water', 'price': 1.49, 'stock': 12},
            'A8': {'name': 'Green Tea', 'price': 2.99, 'stock': 12}
        }

    def display_items(self):                                                                        # displays "Available items" in a table format
        print("\nAvailable items:")
        print("-" * 55)                                                                             # prints the table headers
        print(f"{'Code':<6} {'Item':<18} {'Price (AED)':<12} {'stock':<8}")                         # left alignment of text in the table
        print("-" * 55)

        for code, item in self.items.items():                                                       # Loop through each item in the dictionary and prints its details in a specific format       
            print(f"{code:<6} {item['name']:<18} {item['price']:<12.2f} {item['stock']:<8}")

    print("-" * 55)

    def select_item(self, code):                                                                    # allows user to select an item by entering its code                   
        if code in self.items:                                                                      # validates if the entered code exists in the items dictionary
            item = self.items[code]
            if item['stock'] > 0:                                                                   # checks if the selected item is still in stock
                return item
            else:
                print("Sorry, this item is out of stock.")
        else:
            print("Invalid selection.")
        return None                                                                                 # incase something goes wrong, return None              

    def process_transaction(self, item, inserted_amount):                                           # function that processes the transaction, handles the payment and dispenses the item
        if inserted_amount >= item['price']:                                                        # checks if the user inserted sufficient funds
            change = inserted_amount - item['price']                                                # calculates how much change to return to the user
            item['stock'] -= 1                                                                      # deducts one from the stock of paid item
            print(f"Dispensing {item['name']}.")
            if change > 0:                                                                          # only prints change if there is any to return                     
                print(f"Returning change: {change:.2f} AED")
        else:
            print("Insufficient funds.")


def main():                                                                                         # this function runs the vending machine program
    vending_machine = VendingMachine()

    while True:                                                                                     # Program runs forever until the user inputs 'exit' to quit
        vending_machine.display_items()                                                             # Shows the inventory of the vending machine
        code = input("\nEnter item code (or 'exit' to quit): ").strip()                             # prompts user to choose an item or exit

        if code.lower() == 'exit':                                                                  # if statement when the user inputs 'exit', program will terminate     
            print("Thank you for using mugi's vending machine")
            break

        item = vending_machine.select_item(code)                                                    # item selection process
        if not item:                                                                                # in case code is invalid or item is out of stock, restart the loop
            continue

        while True:                                                                                 # Keeps asking for currency until valid input is given or transaction is cancelled
            money_input = input(
                f"The price of {item['name']} is {item['price']} AED. "
                "Insert money (or type 'exit' to cancel): "
            ).strip()

            if money_input.lower() == 'exit':                                                       # if user inputs 'exit', transaction is cancelled and loop breaks            
                print("Transaction cancelled.") 
                break

            try:
                inserted_amount = float(money_input)                                                # converts user input into a decimal number (float)  
                vending_machine.process_transaction(item, inserted_amount)                          # processes the transaction with the selected item and inserted amount
                break
            except ValueError:                                                                      # handles invalid input that cannot be converted to float   
                print("Invalid amount. Please enter a number.")


if __name__ == "__main__":
    main()