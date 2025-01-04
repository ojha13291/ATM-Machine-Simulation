class ATM:
    def __init__(self, pin):
        self.balance = 0
        self.pin = pin
        self.transaction_history = []

    def check_pin(self, input_pin):
        return self.pin == input_pin

    def balance_inquiry(self):
        """Displays the current account balance."""
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        """Deposits the specified amount into the account."""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount:.2f}")
            print(f"${amount:.2f} has been deposited to your account.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Withdraws the specified amount from the account if sufficient balance is available."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount:.2f}")
            print(f"${amount:.2f} has been withdrawn from your account.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def change_pin(self, old_pin, new_pin):
        """Changes the account PIN if the old PIN is correct."""
        if self.check_pin(old_pin):
            self.pin = new_pin
            self.transaction_history.append("PIN changed.")
            print("Your PIN has been changed successfully.")
        else:
            print("Incorrect old PIN.")

    def show_transaction_history(self):
        """Displays the transaction history."""
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")

def main():
    atm = ATM(pin="1234")
    
    while True:
        print("\n--- ATM Menu ---")
        print("1: Balance Inquiry")
        print("2: Deposit Cash")
        print("3: Withdraw Cash")
        print("4: Change PIN")
        print("5: Transaction History")
        print("6: Exit")
        
        choice = input("Please select an option: ")
        
        if choice == "1":
            atm.balance_inquiry()
        
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        
        elif choice == "4":
            old_pin = input("Enter old PIN: ")
            new_pin = input("Enter new PIN: ")
            atm.change_pin(old_pin, new_pin)
        
        elif choice == "5":
            atm.show_transaction_history()
        
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()