# Chapter 4 - If statements
# First exercise - Conditional tests
flower = 'lotus'
print("Is flower=='lotus'? I predict True.")
print(flower=='lotus')
print("Is flower=='tulip'? I predict False.")
print(flower=='tulip')
plant = 'Ficus'
print(plant=='ficus')
print(plant.lower()=='ficus')
age = 30
print(age<35)
requested_sides = ['fries', 'rice', 'salad']
print('fries' in requested_sides)
print('vegetables' in requested_sides)
food_allergies = ['peanut', 'gluten', 'oranges']
food = 'apples'
if food not in food_allergies:
    print(f"{food.title()} do not contain the listed allergies, you can eat it!")
sentence = "I liked to go to the market."
if sentence!="I like to go to the market.":
    print("Try to formulate the sentence in a different way, check your spelling!")
# Next exercise - If statements
alien_color = 'red'
if alien_color=='green':
    print("\nYou just earned 5 points!")
else:
    print("\nYou just earned 10 points!")
shooting_colors = ['red']
if 'green' in shooting_colors:
    print("You earned 5 points!")
elif 'yellow' in shooting_colors:
    print("You earned 10 points!")
elif 'red' in shooting_colors:
    print("You earned 15 points!")
age = 80
if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")
favorite_fruits = ['watermelon', 'mango', 'banana']
if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'mango' in favorite_fruits:
    print("You really like mangos!")
if 'strawberry' in favorite_fruits:
    print("You really like strawberries!")
# Next exercise - Lists + if statements
# ['maria', 'macy', 'mary', 'jay', 'jacob']
current_users = ['joe', 'jay', 'jacob', 'jonah', 'joseph']
new_users = ['maria', 'macy', 'mary', 'jay', 'jacob']
for new_user in new_users:
    if new_user in current_users:
        print(f"\nUsername {new_user} is already taken. Please provide a new name.")
    else:
        print(f"\nWelcome {new_user} to this game.")
ordinal_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for number in ordinal_numbers:
    if number=='1':
        print("1st")
    elif number=='2':
        print("2nd")
    elif number=='3':
        print("3rd")
    else:
        print(f"{number}th")