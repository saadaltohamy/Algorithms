# Counting Money Problem
'''
You are given coins of different denominations and a total amount of money.
Write a function to compute the number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
'''
coins = [100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.2, 0.1, 0.05, 0.01]
def change(amount):
    chenged = False
    number_of_coins = 0
    for coin in coins:
        while coin <= amount:
            chenged = True
            number_of_coins += 1
            amount -= coin
            amount = round(amount, 2)
    if chenged:
        return number_of_coins
    else:
        return -1


print(change(9.87))
print(change(0.001))