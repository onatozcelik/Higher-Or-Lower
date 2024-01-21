
from art import logo,vs
from game_data import data
import random as rd
import os
GAME_DATA=data
VERSUS_ART = vs

def console_clear() -> None:
    """Clears Console"""
    os.system("clear") if os.name == "posix" else os.system("cls")

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

def check_guess(guess,account1_followers,account2_followers):
    """Compares user guess with actual followers and returns true or false"""
    if account1_followers> account2_followers:
        return guess=='A'
    elif account2_followers > account1_followers:
        return guess== 'B'


def game():
    console_clear()
    print(logo)
    game_continue = True
    score=0
    account1=select_account()
    account2=select_account()
    while game_continue:
        account1=account2
        account2=select_account()
        while account1 == account2:
            account2=select_account()
        guess=print_versus(account1,account2)
        account1_followers = int(account1["follower_count"])
        account2_followers = int(account2["follower_count"])
        guess_correct= check_guess(guess,account1_followers,account2_followers)
        if guess_correct:
            score +=1
            console_clear()
            print(f"Correct ! Current Score: {score}")
        else:
            game_continue=False
            print(f"You Lose ! Score : {score} ")
            if input("Do You Want To Play Aagain Y or N ?").upper() =="Y":
                game()
            else:
                print("Goodbye !")
game()
