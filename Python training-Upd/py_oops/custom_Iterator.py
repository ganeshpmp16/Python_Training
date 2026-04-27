# customer iterator demonstration
class CustomIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self): # return the iterator object itself
        return self

    def __next__(self):
        if self.index < len(self.data): # check if there are more items to iterate over
            result = self.data[self.index] # retrieve the current item
            self.index += 1 # move to the next index for the next iteration
            return result
        else:
            raise StopIteration # signal that there are no more items to iterate over

# Example usage
data = [1, 2, 3, 4, 5]
custom_iter = CustomIterator(data)
for item in custom_iter:
    print(item)  # Output: 1 2 3 4 5    
