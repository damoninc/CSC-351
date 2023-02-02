class Account:

    def __init__(self, account_num, owner_name, balance):
        self.account_num = int(account_num)
        self.owner_name = str(owner_name)
        self.balance = float(balance)

    def __str__(self):
        return f"Acct#: {self.account_num}, Owner: {self.owner_name}, Balance: {self.balance}"

    def __repr__(self):
        return f"Account({self.account_num}, {self.owner_name}, {self.balance})"


acct_list = [Account(*x.strip().split(',')) for x in open('accounts.csv').readlines()[1:]]

#### DO NOT MODIFY ANY CODE ABOVE THIS LINE ####

###### INSTRUCTIONS #####
#   The goal of this assignment is to translate function requirements into input validation and error raising code
#   properly as discussed in class. 
#
#   The functions below are part of a core banking system. You need to complete the functions. Other programmers
#   will call your code directly by invoking the functions, e.g., create("Bob", 123.45). Note that the "database"
#   for this bank (a Python list) is already initialized for you.
#
#   You are responsible for detecting and raising errors, but you do not need to handle errors.
#   You can, and should, write test code at the bottom of the file.
#   Assume that the "Precondition" of each function will always be True when your function is invoked.
#
#   Your grade is based on:
#       - the correctness and completeness of the three functions per their requirements
#       - properly validating function input
#       - correctly raising appropriate exceptions
#       - maintaining the postconditions of each function
########################
import random

# Name: Damon Incorvaia
# CSC 350-001, Spring 2023
# Assignment 1 - input validation practice

def create(owner_name: str, balance: float):
    """
    Precondition: acct_list contains a list of 0 or more Account objects.

    Create a new Account object and add it to acct_list.
    - generate an account number. Account numbers are 6 integer digits. Account numbers must be unique, and cannot start with 0.
    - owner_names cannot be empty, can be at most 64 characters, and can only contain Latin alphabet characters and spaces.
    - the balance must be a non-negative float.

    Raise can exception appropriate to the input error as needed. The function can raise exceptions
    in multiple places. Provide some description of the error in the Exception data.

    Postcondition: acct_list contains the new Account if all other conditions are met, otherwise acct_list is unchanged.

    :param owner_name: the desired owner's name
    :param balance: the initial balance
    :return: the function returns nothing
    """
    # Input Validation

    if not isinstance(owner_name, str):
        raise TypeError("Account Owner Name must be a type String")
        
    if not isinstance(balance, float):
        raise TypeError("Account balance must be of type Float")
    
    # Start of Account creation
    try:
        account_num = random.randint(100000,999999)
        for acct in acct_list:
            if account_num == acct.account_num:
                raise KeyError
        new_account = Account(account_num=account_num, owner_name=owner_name, balance=balance)
        with open('accounts.csv') as acct_db:


    except KeyError:
        create(owner_name, balance)
        


    



def deposit(account_num: int, amount: float):
    """
    Precondition: acct_list contains a list of 0 or more Account objects.

    Add 'amount' to the Account object's balance with 'account_num'.
    - amount must be a non-negative float.
    - account_num must be an integer that corresponds to an account in the list.

    Raise can exception appropriate to the input error as needed. The function can raise exceptions
    in multiple places. Provide some description of the error in the Exception data.

    Postcondition: the Account object in acct_list is updated with the new balance. The acct_list is otherwise unchanged.

    :param account_num: the account number to search for
    :param amount: the amount to add to the account's balance
    :return: the function returns nothing
    """

    raise NotImplementedError  # remove this line when you work on this function


def withdraw(account_num: int, amount: float):
    """
    Precondition: acct_list contains a list of 0 or more Account objects.

    Subtract 'amount' from the Account object's balance with 'account_num'.
    - amount must be a non-negative float.
    - account_num must be an integer that corresponds to an account in the list.
    - amount must be less than or equal to the balance of the account.

    Raise can exception appropriate to the input error as needed. The function can raise exceptions
    in multiple places. Provide some description of the error in the Exception data.

    Postcondition: the Account object in acct_list is updated with the new balance. The acct_list is otherwise unchanged.

    :param account_num: the account number to search for
    :param amount: the amount to subtract to the account's balance
    :return: the function returns nothing
    """

    raise NotImplementedError  # remove this line when you work on this function


# print(acct_list[0])
# deposit(796505, 123.45)
# print(acct_list[0])

create()
