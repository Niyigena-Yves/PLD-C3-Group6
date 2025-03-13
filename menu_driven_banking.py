#!/usr/bin/python3

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
<<<<<<< HEAD
    print("Withdrawal successful!")
    
    # Function to display transaction history
def transaction_history():
=======

print("Withdrawal successful!")

#Function to check balance
def check_balance():
>>>>>>> 5527c7dabd8a66131eb786526ee83f571307ab14
    acc_no = input("Enter account number: ")
    if acc_no not in accounts:
        print("Account not found!")
        return
<<<<<<< HEAD
    print("Transaction History:")
    for transaction in accounts[acc_no]["transactions"]:
        print("-", transaction)
=======
    print(f"Account Balance: ${accounts[acc_no]['balance']}")

# Run the banking system
if __name__ == "__main__":
    main()
>>>>>>> 5527c7dabd8a66131eb786526ee83f571307ab14
