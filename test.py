# txt = "I love apples, apple are my favorite fruit"

# x = txt.count("apple", 0, 24)

# print(x)

# import random

# print(random.randint(0, 1))
# print(round(random.random() * 100, 2))

# import random

# mylist = ["apple", "banana", "cherry"]

# print(random.sample(mylist, len(mylist)))

# def greet():
#     print('This function')
#     print('Just prints')
#     print('Random things thrice')

# greet()

# Parameter is the name of the data that is being passed into a fucntion.
# Arguments are the actual values of the data that is passed into a function

# def greet_with_name(name, age):
#     print(f'Hello {name}')
#     print(f'You are {age} years old')
    
# greet_with_name("Kevin", 22)

# def greet_with_location(name, location):
#     print(f"Hello {name}!")
#     print(f"How is it like in {location}")

# greet_with_location(name= "Kevin", location= "London")

# Learning about dictionaries.
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

# for i in travel_log:
#     new_val = travel_log.get(i)
#     new_dic = dict(new_val)
#     print(new_dic.get('cities_visited'))
    
def add_new(country, cities_visited, total_visits):
    new_dict = {}
    new_dict[country] = {
        'cities': cities_visited,
        'visits': total_visits
    }
    travel_log.update(new_dict)
    
add_new('UK', ['London', 'Birmingham', 'Manchester', 'Chelsea'], 50)
print(travel_log)