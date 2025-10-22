class ATM:
    def __init__(self):
        self.balance = 1000         # Public
        self._user_name = "Rohan"   # Protected
        self.__pin = 1234           # Private

    def __verify_pin(self):  # Private method
        try:
            pincode = int(input("Enter your PIN: "))
            if pincode == self.__pin:
                return True
            else:
                print("Incorrect PIN.")
                return False
        except ValueError:
            print("Invalid input! Enter numbers only.")
            return False

    def check_balance(self):  # Public
        if self.__verify_pin():
            print(f"Hello, {self._user_name}")
            print(f"Your current balance is ₹{self.balance}")

    def deposit(self):  # Public
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                self.balance += amount
                print(f"₹{amount} deposited successfully.")
                print(f"New balance: ₹{self.balance}")
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Invalid amount entered.")

    def withdraw(self):  # Public
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print("Amount must be greater than 0.")
            elif amount > self.balance:
                print("Insufficient funds.")
            elif self.__verify_pin():
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully.")
                print(f"New balance: ₹{self.balance}")
        except ValueError:
            print("Invalid amount entered.")

    def atm_menu(self):  # Public
        print("---------- Welcome to Python ATM ----------")
        while True:
            print("\nChoose an option:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            option = input("Enter your choice (1-4): ")

            if option == "1":
                self.check_balance()
            elif option == "2":
                self.deposit()
            elif option == "3":
                self.withdraw()
            elif option == "4":
                print("Thank you for using Python ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1 to 4.")

# Running the ATM
atm = ATM()
atm.atm_menu()

print(atm.balance)          # Public – Accessible

print(atm._user_name)       # Protected – Accessible but not recommended (convention)

# print(atm.__pin)          # Private – Not directly accessible, will give AttributeError

print(atm._ATM__pin)        # Name-mangled way to access private – Not recommended
