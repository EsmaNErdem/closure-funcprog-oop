class createAccount():
    """Creates an account with a pin and initial amount"""
    def __init__(self, pin, initial):
        self.pin = pin
        self.account = initial

    def checkBalance(self, pin):
        """checks balance with a correct PIN"""
        if self.pin == pin:
            return self.account
        else:
            return "Invalid PIN"
        
    def deposit(self, pin, amount):
        """Deposit money into the bank acount with correct PIN, returns current amount"""
        if self.pin == pin:
            self.account += amount
            return self.account
        else:
            return "Invalid PIN"
        
    def withdraw(self, pin, amount):
        """withdraw money from bank account with correct PIN, returns current amount"""
        if self.pin == pin:
            self.account -= amount
            return self.account
        else:
            return "Invalid PIN"
        
    def changePin(self, pin, new_pin):
        """Changes PIN and confirms"""
        if self.pin == pin:
            self.pin = new_pin
            return "PIN successfully changed!"
        else:
            return "Invalid PIN"