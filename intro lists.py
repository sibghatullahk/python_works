question=input("What is your name? ")
print('Hello,', question.title())
bicycles=['trek', 'cannondole','redline','specialized']
print(bicycles)
print(bicycles[0].lower())
print(bicycles[3].upper())
print(bicycles[2].title())
print(bicycles[-1].title()) #returns the last element of a list,-2 will bring up the 2nd last and so forth.
message=f"My first bicycle was a {bicycles[0].title()}."
print(message)
print(f"My first bicycle was a {bicycles[-1].upper()}")
print(f"My first bicycle was a {bicycles[2].lower()}")
friends=['Trent', 'Salah','Van Dijk','Allison','Robertson','Nunez']
print(f"Hello,{friends[1].casefold()}")
print(f"Hello,{friends[2].title()}")
print(f"Hello,{friends[3].upper()}")
print(f"Hello,{friends[1].lower()}")
motorcycles=['honda','yamaha','suzuki']
motorcycles.append('royal') #adds an item to the list
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)
cars=['buggati','toyota','honda','suzuki','nissan',]
cars.insert(0, 'mazda')
cars.insert(2, 'lexus')
print(cars)
del cars[1] #can not use a deleted item now
print(cars)
#pop method; you can use the popped item unlike the del method
popped_cars=cars.pop()
print(cars)
print(popped_cars)
last_owned=cars.pop(4)
first_owned=cars.pop(2)
print(f"The last car i owned was a {last_owned.title()}")
print(f"The first car i owned was a {first_owned.title()}")
print(cars)
too_expensive='honda'
cars.remove(too_expensive) #to remove an item you don't know the position for
print(f"\nA {too_expensive.title()} is just crap.")