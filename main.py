sandwiches = ["grilled cheese", "ruben", "pb&j", "philly cheese steak", "cucumber sandwich", "tuna melt", "banh mi"]
import random
# for-in loop
'''
for sandwich in sandwiches:
    print(f"Delicious sandwich: {sandwich}")
'''
# numbering the menu
'''
for number in range(1, len(sandwiches)+1):
    print(f"{number}. {sandwiches[number-1]}")
'''
for index in range(len(sandwiches)):
    print(f"{index + 1}. {sandwiches[index]}")

# Creating Random Sandwich Prices
sandwich_prices = {}
price_range = (1,10)
for sandwich in sandwiches:
    sandwich_prices[sandwich] = random.randrange(1, 10) 
    # sandwich_prices[sandwich] = random.randint(price_range[0], price_range[1])
    print(f"{sandwich} ${sandwich_prices[sandwich]}")
# print(sandwich_prices)


display_list = []
display_num = 0
for target_price in range(price_range[0], price_range[1]+1):
    for sandwich, price in sandwich_prices.items():
        if price == target_price:
            display_num += 1
            display_list.append(f"{display_num}. {sandwich} ${price}")
for sandwiches in display_list:
    print(sandwiches)

