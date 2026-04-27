text =input("Enter a Sentence: ")
#upper lower length
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
#replace and split
replaced_text = text.replace(" ", "_")  # Replace spaces with underscores   
print("Replaced Text:", replaced_text)
split_text = text.split()  # Split the text into a list of words
print("Split Text:", split_text)
#find and count
word_to_find = input("Enter a word to find: ")
index = text.find(word_to_find)  # Find the index of the first occurrence of the word
if index != -1:
    print(f"'{word_to_find}' found at index: {index}")
else:
    print(f"'{word_to_find}' not found in the text.")
count = text.count(word_to_find)  # Count the occurrences of the word
print(f"'{word_to_find}' occurs {count} times in the text.")
#reverse and slicing
reversed_text = text[::-1]  # Reverse the text using slicing with operator [::]
print("Reversed Text:", reversed_text)
sliced_text = text[0:5]  # Get the first 5 characters of the text
print("Sliced Text (first 5 characters):", sliced_text)

# check substring
substring = input("Enter a substring to check: ") # substring is a string that is part of another string. It can be a single character, a word, or a phrase.    
if substring in text:
    print(f"'{substring}' is present in the text.")
else:    
    print(f"'{substring}' is not present in the text.")
