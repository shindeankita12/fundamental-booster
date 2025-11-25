                        #   Fundamental Booster:


print ("welcome the interactive personal data collection")

name = input("enter your name :")
age = int(input("enter your age :"))
height =float(input("enter your hieght in meter :"))
favourite_number = int(input("enter your favourite number :"))
 
print("thank you! here is the information we collected: ")

print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favourite Number: {favourite_number} (Type: {type(favourite_number)}, Memory Address: {id(favourite_number)})")

current_year= 2025
birth_year= current_year - age
print(f"your birth year is approximately:{birth_year} (based on your age of {age})")

print("thank you for using the personal data collector.goodbye!")