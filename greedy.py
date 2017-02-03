import cs50
import sys

coins = 0

def check(money):
    while money == 0 and money < 0:
        print("Please put amount in $")
        money = cs50.get_float()
       
def calculation(cents):
    global coins
    while coins >= 25:
        +coins
        cents = cents - 25
    while coins >= 10:
        +coins
        cents = cents - 10
    while coins >= 5:
        +coins
        cents = cents - 5
    while coins >= 1:
        +coins
        cents = cents - 1
    return coins
    print(coins)
        
def main():
    print("O hai! How much change is owed?")
    money = cs50.get_float()
    check(money)
    cents = round(money*100)
    calculation(cents)
          
if __name__ == "__main__":
    main()
