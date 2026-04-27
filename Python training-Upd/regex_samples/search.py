import re
text = "my phone number is 9888123450"
pattern = r'\d{10}'
match = re.search(pattern, text) #search() returns a match object if the pattern is found, otherwise it returns None
if match:
    print("Phone number found:", match.group())
else:    
    print("Phone number not found.")
# find all numbers in the text
text ="Marks: Math-85, Science-90, English-80"
numbers = re.findall(r'\d+', text)
print("All numbers found:", numbers)

# validate email address
email = "example@example.com"
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")

# replace text using regex
text = "The color of the sky is blue."
new_text = re.sub(r'blue', 'red', text) #replaces the first occurrence of 'blue' with 'red' in the text.
print("Original text:", text)
print("Modified text:", new_text)

#extracting dates from text
text = "The event is scheduled for 2024-07-15 and 2024-08-20."
dates = re.findall(r'\d{4}-\d{2}-\d{2}', text)
print("Dates found:", dates)

# extract emails from text
text = "Please contact us at example@example.com or support@company.com."
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
print("Emails found:", emails)
