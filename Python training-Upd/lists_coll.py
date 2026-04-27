numbers =[10, 20, 30, 40, 50] # is a array of integers
print("Numbers:", numbers)
#add an element to the list
numbers.append(60)
print("Numbers after appending 60:", numbers)
# add an element using the user input
numbers.append(int(input("Enter a number to add to the list: ")))
print("Numbers after appending user input:", numbers)
#loop through the list
print("Looping through the list:")
for number in numbers:
    print(number)
#sum of the list
total = sum(numbers)
print("Sum of the numbers in the list:", total)
#average of the list
average = total / len(numbers)
print("Average of the numbers in the list:", average)