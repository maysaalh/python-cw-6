# write your code here
person=[
    {
        'name':"Maysa",
        'age': 17,
        'hobbies': ["Eating", "sleeping", "reading"]
    

    }
]
name=person[0].get('name')
print(name)

age=person[0].get('age')
print(age)

person[0]['age']= 18
print(person)

person[0]['country']= 'India'
print(person)

print(len(person[0]))

person[0]['hobbies'].append("knitting")
print(person)

def check_hobbies(person):
    if len(person[0]['hobbies'])>=3:
        print(f"WOW YOU ARE AMAZING")
check_hobbies(person)