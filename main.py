
from art import logo,vs
from game_data import data
import random as rd
GAME_DATA=data
VERSUS_ART = vs

def select_account(data=GAME_DATA):
    """Select and Return Random Account"""
    return data[rd.randint(0,len(data)-1)]


def account_format(account):
    name=account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"

def print_versus(account_1,account_2,versus=VERSUS_ART):
    """Prints Versus Message For Given Accounts"""
    print(f"Compare A: {account_format(account_1)}")
    print(versus)
    print(f"Against B: {account_format(account_2)}")
    return input("Which has more followers A or B ? \n").upper()


account1=select_account()
account2=select_account()

print(print_versus(account1,account2))
