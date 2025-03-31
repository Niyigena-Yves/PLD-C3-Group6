import json

class Account:
    """Class representing a bank account"""
    
    def __init__(self, acc_no, name, initial_balance=0):
        """Initialize a new account with account number, name and balance"""
        self.acc_no = acc_no
        self.name = name
        self.balance = initial_balance
        self.transactions = [f"Initial deposit: ${initial_balance}"]
    
    def deposit(self, amount):
        """Deposit money into the account"""
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount}")
        return True
    
    def withdraw(self, amount):
        """Withdraw money from the account if sufficient funds available"""
        if amount > self.balance:
            return False
        self.balance -= amount
        self.transactions.append(f"Withdrew: ${amount}")
        return True
    
    def get_balance(self):
        """Return the current balance"""
        return self.balance
    
    def get_transaction_history(self):
        """Return the transaction history"""
        return self.transactions
    
    def to_dict(self):
        """Convert account object to dictionary for storage"""
        return {
            "name": self.name,
            "balance": self.balance,
            "transactions": self.transactions
        }
    
    @classmethod
    def from_dict(cls, acc_no, account_data):
        """Create an Account object from stored dictionary data"""
        account = cls(acc_no, account_data["name"], account_data["balance"])
        account.transactions = account_data["transactions"]
        return account


class BankingSystem:
    """Class managing the banking system operations"""
    
    DATA_FILE = "bank_data.json"
    
    def __init__(self):
        """Initialize the banking system with stored account data"""
        self.accounts = {}
        self.load_data()
    
    def load_data(self):
        """Load existing accounts from file"""
        try:
            with open(self.DATA_FILE, "r") as file:
                accounts_data = json.load(file)
                for acc_no, account_data in accounts_data.items():
                    self.accounts[acc_no] = Account.from_dict(acc_no, account_data)
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}
    
    def save_data(self):
        """Save account data to file"""
        accounts_data = {}
        for acc_no, account in self.accounts.items():
            accounts_data[acc_no] = account.to_dict()
            
        with open(self.DATA_FILE, "w") as file:
            json.dump(accounts_data, file, indent=4)
    
    def create_account(self, acc_no, name, initial_balance):
        """Create a new bank account"""
        if acc_no in self.accounts:
            return False
        
        self.accounts[acc_no] = Account(acc_no, name, initial_balance)
        self.save_data()
        return True
    
    def get_account(self, acc_no):
        """Retrieve an account by account number"""
        return self.accounts.get(acc_no)
    
    def deposit(self, acc_no, amount):
        """Deposit money into an account"""
        account = self.get_account(acc_no)
        if not account:
            return False
        
        success = account.deposit(amount)
        if success:
            self.save_data()
        return success
    
    def withdraw(self, acc_no, amount):
        """Withdraw money from an account"""
        account = self.get_account(acc_no)
        if not account:
            return False
        
        success = account.withdraw(amount)
        if success:
            self.save_data()
        return success


class BankingInterface:
    """Class handling user interaction with the banking system"""
    
    def __init__(self):
        """Initialize the interface with a banking system"""
        self.bank = BankingSystem()
    
    def create_account(self):
        """Handle account creation input and output"""
        acc_no = input("Enter new account number: ")
        if acc_no in self.bank.accounts:
            print("Account already exists!")
            return
        
        name = input("Enter account holder's name: ")
        try:
            initial_balance = float(input("Enter initial deposit amount: "))
            if initial_balance < 0:
                print("Initial deposit cannot be negative!")
                return
        except ValueError:
            print("Please enter a valid amount!")
            return
        
        success = self.bank.create_account(acc_no, name, initial_balance)
        if success:
            print("Account created successfully!")
        else:
            print("Failed to create account!")
    
    def deposit(self):
        """Handle deposit input and output"""
        acc_no = input("Enter account number: ")
        if acc_no not in self.bank.accounts:
            print("Account not found!")
            return
        
        try:
            amount = float(input("Enter deposit amount: "))
            if amount <= 0:
                print("Deposit amount must be positive!")
                return
        except ValueError:
            print("Please enter a valid amount!")
            return
        
        success = self.bank.deposit(acc_no, amount)
        if success:
            print("Deposit successful!")
        else:
            print("Deposit failed!")
    
    def withdraw(self):
        """Handle withdrawal input and output"""
        acc_no = input("Enter account number: ")
        if acc_no not in self.bank.accounts:
            print("Account not found!")
            return
        
        try:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Withdrawal amount must be positive!")
                return
        except ValueError:
            print("Please enter a valid amount!")
            return
        
        success = self.bank.withdraw(acc_no, amount)
        if success:
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")
    
    def check_balance(self):
        """Handle balance check input and output"""
        acc_no = input("Enter account number: ")
        account = self.bank.get_account(acc_no)
        if not account:
            print("Account not found!")
            return
        
        print(f"Account Balance: ${account.get_balance()}")
    
    def transaction_history(self):
        """Handle transaction history input and output"""
        acc_no = input("Enter account number: ")
        account = self.bank.get_account(acc_no)
        if not account:
            print("Account not found!")
            return
        
        print("Transaction History:")
        for transaction in account.get_transaction_history():
            print("-", transaction)
    
    def run(self):
        """Run the banking interface main loop"""
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
                self.create_account()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.check_balance()
            elif choice == "5":
                self.transaction_history()
            elif choice == "6":
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again!")


# Run the banking system
if __name__ == "__main__":
    banking_interface = BankingInterface()
    banking_interface.run()