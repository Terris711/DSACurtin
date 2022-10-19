from checkPrime import isPrime
from nextPrime import nextPrime
from DSAHashEntry import HashEntry, HashTable


Hash = HashTable(6)

print("Testing Hashtable using seperate chaining")
print()

print("1. Check prime number")
print("2. Find the next prime number")
print("3. Add data")
print("4. Get data")
print("5. Remove data")
print("6. Display data")
print("7. Exit")
print()
activity = int(input("Enter your option: "))
while activity != 7:
    if activity == 1:
       number = int(input("Enter a number you wanna check: "))
       print(isPrime(number))

    elif activity == 2:
       number = int(input("Enter a number: "))
       print(nextPrime(number))

    elif activity == 3:
        Hash.put(1, "Anna")
        Hash.put(2, "Neeraj")
        Hash.put(3, "Vincent")
        Hash.put(4, "Jevi")
        Hash.put(5, "Maria")

    elif activity == 4:
        key = int(input("Enter a key: "))
        print(Hash.get(key))

    elif activity == 5:
        key = int(input("Enter a key you wanna remove: "))
        Hash.remove(key)

    elif activity == 6:
        Hash.hashdisplay()

        
    else:
        print("Please enter a valid option!")
    activity = int(input("Enter your option: "))






