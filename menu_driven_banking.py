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

# Run the banking system
if __name__ == "__main__":
    main()
