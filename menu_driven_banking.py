import json

# File to store user data
DATA_FILE = "bank_data.json"

# Load existing accounts (if any)
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save account data
def save_data(accounts):
    with open(DATA_FILE, "w") as file:
        json.dump(accounts, file, indent=4)

# Initialize accounts data
accounts = load_data()

# Function to create an account
def create_account():
    acc_no = input("Enter new account number: ")
    if acc_no in accounts:
        print("Account already exists!")
        return
    name = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial deposit amount: "))
    accounts[acc_no] = {"name": name, "balance": initial_balance, "transactions": [f"Initial deposit: ${initial_balance}"]}
    save_data(accounts)
    print("Account created successfully!")

# Function to deposit money
def deposit():
    acc_no = input("Enter account number: ")
    if acc_no not in accounts:
        print("Account not found!")
        return
    amount = float(input("Enter deposit amount: "))
    accounts[acc_no]["balance"] += amount
    accounts[acc_no]["transactions"].append(f"Deposited: ${amount}")
    save_data(accounts)
    print("Deposit successful!")

# Function to withdraw money
def withdraw():
    acc_no = input("Enter account number: ")
    if acc_no not in accounts:
        print("Account not found!")
        return
    amount = float(input("Enter withdrawal amount: "))
    if amount > accounts[acc_no]["balance"]:
        print("Insufficient balance!")
        return
    accounts[acc_no]["balance"] -= amount
    accounts[acc_no]["transactions"].append(f"Withdrew: ${amount}")
    save_data(accounts)
    print("Withdrawal successful!")

# Function to check balance
def check_balance():
    acc_no = input("Enter account number: ")
    if acc_no not in accounts:
        print("Account not found!")
        return
    print(f"Account Balance: ${accounts[acc_no]['balance']}")

# Function to display transaction history
def transaction_history():
    acc_no = input("Enter account number: ")
    if acc_no not in accounts:
        print("Account not found!")
        return
    print("Transaction History:")
    for transaction in accounts[acc_no]["transactions"]:
        print("-", transaction)

# Main menu function
def main():
    while True:
        print("\n=== BANKING SYSTEM MENU ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            transaction_history()
        elif choice == "6":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

# Run the banking system
if _name_ == "_main_":
    main()