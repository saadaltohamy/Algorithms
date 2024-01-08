# Fractional Knapsack Problem
'''
You are given a list of items and a knapsack with a certain capacity.
Each item has a weight and a value.
Your goal is to maximize the value of the knapsack.
You can put items in the knapsack fractionally.
'''

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def fractional_knapsack(items, capacity):
    # Sort the items by value
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    total_value = 0
    for item in items:
        # if you can take the whole item, take it
        if capacity - item.weight >= 0:
            capacity -= item.weight
            total_value += item.value
            
        # else, take a fraction of it
        else:
            fraction = capacity / item.weight
            total_value += item.value * fraction
            break

    return total_value

items = [Item(10, 60), Item(40, 40), Item(20, 100), Item(30, 120)]
capacity = 50
print(fractional_knapsack(items, capacity))