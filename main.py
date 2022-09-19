sandwiches = ["grilled cheese", "ruben", "pb&j", "philly cheese steak", "cucumber sandwich", "tuna melt", "banh mi"]

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
