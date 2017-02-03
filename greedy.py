import cs50
import sys

def check(money):
    while money == 0 and money < 0:
        print("Please put amount in $")
        money = cs50.get_float()
    cents = round(money*100)
    coins = 0
    while cents >= 25:
        coins = coins + 1
        cents = cents - 25
    while cents >= 10:
        coins = coins + 1
        cents = cents - 10
    while cents >= 5:
        coins = coins + 1
        cents = cents - 5
    while cents >= 1:
        coins = coins + 1
        cents = cents - 1
    print(coins)
        
def main():
    print("O hai! How much change is owed?")
    money = cs50.get_float()
    check(money)

if __name__ == "__main__":
    main()
