# count the number of vowels in a string
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
print(f"The number of vowels in the string is: {vowel_count}")
#reverse the string and count the vowels in the reversed string
reversed_text = text[::-1]
reversed_vowel_count = 0
for char in reversed_text:
    if char in vowels:
        reversed_vowel_count += 1
print(f"The number of vowels in the reversed string is: {reversed_vowel_count}")
