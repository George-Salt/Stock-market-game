import os
import random


def start_game():
    print("Welcome to the STOCK MARKET game!\n\nIf you want to start the game, press '1'\nIf you want to know more about the game, press '2'")

    choice = int(input("Your choice? "))
    if choice == 1:
        os.system("cls")
        play_all_days()
    if choice == 2:
        os.system("cls")
        tell_about_game()


def tell_about_game():
    print("This game was created by George Salt at the 17th of March, 2022.\nIn this game you have to buy or sell stocks at a good price for that.\nCollect as much money as possible!")


def calculate_allowed_shares_number(balance, price):
    allowed_shares_number = int(balance / price)
    return allowed_shares_number


def play_all_days():
    dollars = 1000
    shares = 0
    days = int(input("How many game days do you want to play? "))
    for day in range(days):
        os.system("cls")
        random_price = random.randint(30, 1100)
        print(f"Your balance: ${dollars}, {shares} shares.\nToday the shares are worth ${random_price}.\n\nIf you want to buy the shares, press '1'.\nIf you want to sell the shares, press '2'.\nTo wait for the next day, press '3'.")
        choice = int(input("Your choice? "))
        if choice == 1:
            print(f"Allowed shares number: {calculate_allowed_shares_number(dollars, random_price)}.")
            new_shares = int(input("How many shares do you want to buy? "))
            os.system("cls")
            if new_shares * random_price > dollars:
                print("Too many shares...")
            if new_shares * random_price <= dollars:
                print(f"You bought {shares} shares.")
                dollars -= new_shares * random_price
                shares = new_shares
        if choice == 2:
            print(f"Allowed shares number: {shares}.")
            new_shares = int(input("How many shares do you want to buy? "))
            os.system("cls")
            if new_shares * random_price > shares:
                print("Too many shares...")
            if new_shares * random_price <= shares:
                print(f"You sold out {shares} shares.")
                dollars -= new_shares * random_price
                shares = new_shares
        if choice == 3:
            continue
    os.system("cls")
    print(f"For the game you scored ${dollars}")


if __name__ == "__main__":
    while True:
        try:
            start_game()
        except ValueError:
            os.system("cls")
            continue
