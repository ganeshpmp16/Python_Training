#for loop
fruits = ["apple", "banana", "cherry"] # is a array of strings
for fruit in fruits:
    print(fruit)
print ("Numbers from 1 to 5:")
for i in range(1, 6):  # range(start, stop) generates numbers from start to stop-1  range is a built-in function that generates a sequence of numbers
    print(i)
#while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1  # increment the count by 1  
#nested loop
for i in range(1, 4):
    for j in range(1, 4):
        print("i:", i, "j:", j)
#user input in loop
n = int(input("Enter a number: "))
print("Even numbers from 1 to", n, ":")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)