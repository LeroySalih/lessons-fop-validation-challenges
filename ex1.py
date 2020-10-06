age = input("Enter a valid age.")
age = int(age)

while not (14 <= age < 110):
    print("Invalid age.")
    age = input("Enter a valid age.")
    age = int(age)
print("Welcome.")
