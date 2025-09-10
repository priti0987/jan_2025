import random

subjects =[
    "neel",
    "bhavika",
    "pratap",
    "shriya"
    ]
actions=[
    "eats",
    "cancels",
    "drinks",
    ]
places_or_things =[
    "banana",
    "juice",
    "a plate of samosa",
    "milk"
]

while True:
    subject = random.choice(subjects)
    action= random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headLines = f"Breaking News : {subject} {action} {place_or_thing} "
    print("\n",headLines)

    user_input = input("\n Do you want another headline ? yes/no? ".strip().lower())
    if user_input == "no":
        break

print("\n Thank you for fake news generator")