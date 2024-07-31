from helper import d 

# Nesting dictionaries and lists 

# list inside of dictionaries

pet_names = {
    "Dog" : ['Toast', 'Oreo', 'Punkin', 'Pinky', 'Douge', 'Rover',  'Rex', 'Fido', 'Trouble'],
    'Cat' : ['Mittens', 'Ziggy', 'Hot Pocket', 'Miso', 'Catkeisha', 'Randolf', 'Snowball', 'Smokey'],
    'Hamster' : ['Hamtarro', 'Lightening', 'nugget', 'cheddar', 'hammie', 'turbo'],
    'Lizzard' : 'Lizzy'
}

pet_names['Lizzard'] = ['Lizzy', 'Izzy']
# print pet_names

print(pet_names['Cat'][3])
miso_index = pet_names['Cat'].index("Miso") # finding the index of "Miso"
print(miso_index)
print(pet_names['Cat'][3]) # we can chain keys and indecies together, similar to nested lists

for pet, names in pet_names.items():
    print(f"\nCommon {pet} names: ")
    if isinstance(names, list):
        for name in names:
            print(name)
    else:
        print(names)

d()

# Dictionaries inside of lists

books = [
    {'Title' : 'Diary of a Wimpy Kid', 'Author' : "Jeff Kiney", 'Genre': 'YAF'},
    {'Title' : 'Rich Dad Poor Dad', 'Author' : 'Robert Kiwaske', "Genre": 'Self Help'},
    {'Title' : 'Dune', 'Author' : 'Frank Herbert', 'Genre': 'Science Fiction'},
]
# We can chain indecies and keys after one another 
print(books[0]['Author'])

for book in books:
    print(f"{book['Title']} is written by {book['Author']}")

d()

user = {
'dk@email.com' : {'username': 'dylank', 'password': '12345', 'likes': ['dogs', 'tacos']},
'tp@email.com' : {'username': 'traviicii', 'password': '67890', 'likes': ['key lime pie', 'long walks on the beach']},
'toast@email.com': {'username': 'toast-struddle', 'password': 'iamadawg', 'likes': ['treats', 'walks to the park']}
}

print(user['tp@email.com']['likes'][0])

def login(user_dict):
    while True:
        try:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            user = user_dict[email]
            if password == user['password']:
                raise ValueError
        except Exception as e:
            print(e)
            print("invalid email or password")
        else:
            print(f"Welcome back {user['username']}")

login(user)
