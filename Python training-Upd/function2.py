def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
numbers =[]
count = int(input("How many numbers do you want to check? "))
for i in range(count):
    number = int(input("Enter a number: "))
    numbers.append(number)
print("Numbers :", numbers)
for num in numbers:
    print(f"{num} is {check_even_odd(num)}")