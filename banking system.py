class Customer:
    def __init__(self, acc_no, name, age, account_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.age = age
        self.account_type = account_type
        self.balance = balance

    def display(self):
        print("\nCustomer Details:")
        print(f"Account No    : {self.acc_no}")
        print(f"Name          : {self.name}")
        print(f"Age           : {self.age}")
        print(f"Account Type  : {self.account_type}")
        print(f"Balance       : ₹{self.balance}")
        print("-----------------------------------")


class BankSystem:
    def __init__(self):
        self.customers = []

    def register_customer(self):
        print("\n--- Bank Account Registration Form ---")

        # ------------------------------
        # 🔹 ACCOUNT NUMBER VALIDATION
        # ------------------------------
        while True:
            acc_no = input("Enter 12-digit Account Number: ")

            if acc_no.isdigit() and len(acc_no) == 12:
                break
            else:
                print("❌ Invalid Account Number! It must be exactly 12 digits.")
                print("Please try again.\n")

        # Other inputs
        name = input("Enter Customer Name      : ")
        age = int(input("Enter Age                : "))
        acc_type = input("Enter Account Type (Savings/Current): ")
        balance = float(input("Enter Initial Deposit    : "))

        customer = Customer(acc_no, name, age, acc_type, balance)
        self.customers.append(customer)

        print("\n✅ Customer Registered Successfully!")

    def display_all(self):
        if not self.customers:
            print("\nNo customers registered yet!")
            return

        print("\n====== Registered Bank Customers ======")
        for cust in self.customers:
            cust.display()


# -------- MAIN DRIVER CODE --------
bank = BankSystem()

while True:
    print("\n========= Bank Registration Menu =========")
    print("1. Register Customer")
    print("2. Display All Customers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        bank.register_customer()
    elif choice == "2":
        bank.display_all()
    elif choice == "3":
        print("Exiting Bank System...")
        break
    else:
        print("Invalid choice! Try again.")