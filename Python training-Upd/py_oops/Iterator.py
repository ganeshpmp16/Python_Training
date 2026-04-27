# iterator 
nums = [1, 2, 3, 4, 5]
iterator = iter(nums)
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
print(next(iterator))  # Output: 4
print(next(iterator))  # Output: 5
# using for loop to iterate through the list
for num in nums:
    print(num)  # Output: 1 2 3 4 5
    