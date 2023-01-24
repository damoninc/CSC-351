# Damon Incorvaia
# CSC 351 Spring 2023

class PiggyBank:

    def __init__(self, amount):
        self.amount = amount

    def deposit(self, dep_amount):
        self.amount += dep_amount
        return self.amount

    def withdraw(self, with_amount):
        if with_amount > self.amount:
            real_amount = self.amount
            self.amount = 0
            return real_amount

        else:
            self.amount -= with_amount
            return with_amount

def main():
    pig = PiggyBank(25)
    print(f"Piggy Bank Initialized with {pig.amount} dollars.")

    escape = 0
    while escape != 3:
        print("="*15)
        print("Select an option:")
        print("1. Deposit\n2. Withdraw\n3. Exit")
        escape = input()
        escape = int(escape)

        if escape == 1:
            dep_input = input("Enter the amount to deposit: ")
            dep_input = int(dep_input)
            print(f"You deposited {dep_input}. You now have {pig.deposit(dep_input)}.")

        if escape == 2:
            with_input = input("Enter the amount to withdraw: ")
            with_input = int(with_input)
            print(f"You attempted to withdraw {with_input}. You got {pig.withdraw(with_input)}.")
            
main()