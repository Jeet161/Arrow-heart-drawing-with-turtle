class Customer:
    def __init__(self, acc_no, name, age, account_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.age = age
        self.account_type = account_type
        self.balance = balance
        self.frozen = False  # NEW: account freeze status

    def display(self):
        print("\nCustomer Details:")
        print(f"Account No    : {self.acc_no}")
        print(f"Name          : {self.name}")
        print(f"Age           : {self.age}")
        print(f"Account Type  : {self.account_type}")
        print(f"Balance       : ₹{self.balance}")
        print(f"Status        : {'❄ Frozen' if self.frozen else 'Active'}")
        print("-----------------------------------")


class BankSystem:
    def __init__(self):
        self.customers = []

    # -------------------------------
    # REGISTER NEW CUSTOMER
    # -------------------------------
    def register_customer(self):
        print("\n--- Bank Account Registration Form ---")

        while True:
            acc_no = input("Enter 12-digit Account Number: ")
            if acc_no.isdigit() and len(acc_no) == 12:
                break
            print("❌ Invalid Account Number! Must be exactly 12 digits.\n")

        name = input("Enter Customer Name      : ")
        age = int(input("Enter Age                : "))
        acc_type = input("Enter Account Type (Savings/Current): ")
        
        balance = float(input("Enter Initial Deposit    : "))

        cust = Customer(acc_no, name, age, acc_type, balance)
        self.customers.append(cust)

        print("\n✅ Customer Registered Successfully!")
    # -------------------------------
    # SEARCH CUSTOMER
    # -------------------------------
    def find_customer(self, acc_no):
        for cust in self.customers:
            if cust.acc_no == acc_no:
                return cust
        return None

    # -------------------------------
    # DEPOSIT
    # -------------------------------
    def deposit(self):
        acc_no = input("\nEnter Account Number: ")
        cust = self.find_customer(acc_no)

        if cust:
            if cust.frozen:
                print("❌ Account is Frozen! Cannot Deposit.")
                return

            amount = float(input("Enter Amount to Deposit: "))
            cust.balance += amount
            print(f"✅ ₹{amount} Deposited Successfully!")
        else:
            print("❌ Customer Not Found!")

    # -------------------------------
    # WITHDRAW
    # -------------------------------
    def withdraw(self):
        acc_no = input("\nEnter Account Number: ")
        cust = self.find_customer(acc_no)

        if cust:
            if cust.frozen:
                print("❌ Account is Frozen! Cannot Withdraw.")
                return

            amount = float(input("Enter Amount to Withdraw: "))

            if amount > cust.balance:
                print("❌ Insufficient Balance!")
            else:
                cust.balance -= amount
                print(f"✅ ₹{amount} Withdrawn Successfully!")
        else:
            print("❌ Customer Not Found!")

    # -------------------------------
    # CHECK BALANCE
    # -------------------------------
    def check_balance(self):
        acc_no = input("\nEnter Account Number: ")
        cust = self.find_customer(acc_no)

        if cust:
            print(f"\n💰 Current Balance: ₹{cust.balance}")
        else:
            print("❌ Customer Not Found!")

    # -------------------------------
    # TRANSFER MONEY
    # -------------------------------
    def transfer(self):
        sender_acc = input("\nEnter Sender Account Number: ")
        receiver_acc = input("Enter Receiver Account Number: ")

        sender = self.find_customer(sender_acc)
        receiver = self.find_customer(receiver_acc)

        if not sender or not receiver:
            print("❌ One or both accounts do not exist!")
            return

        if sender.frozen:
            print("❌ Sender's Account is Frozen! Cannot Transfer.")
            return

        amount = float(input("Enter Amount to Transfer: "))

        if amount > sender.balance:
            print("❌ Insufficient Balance!")
        else:
            sender.balance -= amount
            receiver.balance += amount
            print(f"✅ ₹{amount} transferred successfully!")

    # -------------------------------
    # UPDATE CUSTOMER DETAILS
    # -------------------------------
    def update_customer(self):
        acc_no = input("\nEnter Account Number to Update: ")
        cust = self.find_customer(acc_no)

        if not cust:
            print("❌ Customer Not Found!")
            return

        print("\n--- Update Menu ---")
        print("1. Update Name")
        print("2. Update Age")
        print("3. Update Account Type")

        choice = input("Enter choice: ")

        if choice == "1":
            cust.name = input("Enter New Name: ")
        elif choice == "2":
            cust.age = int(input("Enter New Age: "))
        elif choice == "3":
            cust.account_type = input("Enter New Account Type: ")
        else:
            print("❌ Invalid Choice!")
            return

        print("✅ Customer Updated Successfully!")

    # -------------------------------
    # FREEZE / UNFREEZE ACCOUNT
    # -------------------------------
    def freeze_account(self):
        acc_no = input("\nEnter Account Number to Freeze/Unfreeze: ")
        cust = self.find_customer(acc_no)

        if cust:
            cust.frozen = not cust.frozen
            status = "Frozen ❄" if cust.frozen else "Active"
            print(f"✅ Account is now: {status}")
        else:
            print("❌ Customer Not Found!")

    # -------------------------------
    # DELETE CUSTOMER
    # -------------------------------
    def delete_customer(self):
        acc_no = input("\nEnter Account Number to Delete: ")
        cust = self.find_customer(acc_no)

        if cust:
            self.customers.remove(cust)
            print("✅ Customer Deleted Successfully!")
        else:
            print("❌ Customer Not Found!")

    # -------------------------------
    # DISPLAY ALL CUSTOMERS
    # -------------------------------
    def display_all(self):
        if not self.customers:
            print("\nNo customers registered!")
            return

        for cust in self.customers:
            cust.display()


# ---------------- MAIN PROGRAM ----------------
bank = BankSystem()

while True:
    print("\n============= BANK SYSTEM MENU =============")
    print("1. Register Customer")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transfer Money")
    print("6. Update Customer Details")
    print("7. Freeze / Unfreeze Account")
    print("8. Delete Customer")
    print("9. Display All Customers")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        bank.register_customer()
    elif choice == "2":
        bank.deposit()
    elif choice == "3":
        bank.withdraw()
    elif choice == "4":
        bank.check_balance()
    elif choice == "5":
        bank.transfer()
    elif choice == "6":
        bank.update_customer()
    elif choice == "7":
        bank.freeze_account()
    elif choice == "8":
        bank.delete_customer()
    elif choice == "9":
        bank.display_all()
    elif choice == "10":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")