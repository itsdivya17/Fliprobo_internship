#!/usr/bin/env python
# coding: utf-8

# # Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
# Sample Text- 'Python Exercises, PHP exercises.'
# Expected Output: Python:Exercises::PHP:exercises:
# 

# In[4]:


import re

def replace_characters(input_text):
    # Define the pattern to match spaces, commas, or dots
    pattern = r'[ ,.]'

    # Use re.sub() to replace matches with colons
    result = re.sub(pattern, ':', input_text)

    return result

# Accept sample text from the user
sample_text = input("Enter sample text: ")

# Call the function and print the result
output_text = replace_characters(sample_text)
print("Expected Output:", output_text)


# # Question 2-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.
# Dictionary- {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
# Expected output-
# 0      hello world
# 1             test
# 2    four five six
# 

# In[6]:


import re

def find_long_words(input_text):
    # Define a regular expression pattern to match words of at least 4 characters
    pattern = re.compile(r'\b\w{4,}\b')

    # Use findall() to find all matches in the input text
    long_words = pattern.findall(input_text)

    return long_words

# Accept input from the user
user_input = input("Enter a string: ")

# Call the function and print the result
result = find_long_words(user_input)
print("Words with at least 4 characters:", result)


# # Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.

# In[5]:


import pandas as pd
import re

# Accept input from the user
data = {'SUMMARY': input("Enter a list of sentences separated by commas: ").split(',')}
df = pd.DataFrame(data)

# Define a function to clean the text using regular expressions
def clean_text(text):
    # Remove commas, !, XXXX, ;, and other non-word characters
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    return cleaned_text

# Apply the clean_text function to the 'SUMMARY' column
df['SUMMARY'] = df['SUMMARY'].apply(clean_text)

# Print the expected output
print("Expected Output:")
print(df)


# # Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.
# 
# 

# In[8]:


import re

def find_specific_length_words(input_text):
    # Define a regular expression pattern to match words of three, four, or five characters
    pattern = re.compile(r'\b\w{3,5}\b')

    # Use findall() to find all matches in the input text
    specific_length_words = pattern.findall(input_text)

    return specific_length_words

# Accept input from the user
user_input = input("Enter a string: ")

# Call the function and print the result
result = find_specific_length_words(user_input)
print("Three, four, and five character words:", result)


# # Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# Expected Output:
# example.com
# hr@fliprobo.com
# github.com
# Hello Data Science World
# Data Scientist
# 

# In[9]:


import re

def remove_parentheses(strings_list):
    # Define a regular expression pattern to match parentheses and their contents
    pattern = re.compile(r'\([^)]*\)')

    # Use sub() to replace matches with an empty string in each string of the list
    result = [pattern.sub('', s) for s in strings_list]

    return result

# Sample Text
sample_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

# Call the function and print the result
output_text = remove_parentheses(sample_text)
print("Expected Output:")
for text in output_text:
    print(text)


# # Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
# Note- Store given sample text in the text file and then to remove the parenthesis area from the text.
# 
# 

# In[10]:


import re

# Step 1: Store the sample text in a text file (e.g., "sample_text.txt")
with open("sample_text.txt", "w") as file:
    file.write('["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]')

# Step 2: Read the text from the file
with open("sample_text.txt", "r") as file:
    text_content = file.read()

# Step 3: Use regular expressions to remove the parenthesis area from each string
pattern = re.compile(r'\([^)]*\)')
modified_text = pattern.sub('', text_content)

# Step 4: Print or store the modified text
print("Modified Text:")
print(modified_text)


# # Question 7- Write a regular expression in Python to split a string into uppercase letters.
# Sample text: “ImportanceOfRegularExpressionsInPython”
# Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]
# 

# In[12]:


import re

# Accept user input for sample text
sample_text = input("Enter a camelCase string: ")

# Use regular expression to split the string into uppercase letters
result = re.findall('[A-Z][^A-Z]*', sample_text)

# Print the expected output
print("Expected Output:", result)


# # Question 8- Create a function in python to insert spaces between words starting with numbers.
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython
# 

# In[13]:


import re

def insert_spaces(text):
    # Use regular expression to insert spaces between words starting with numbers
    result = re.sub(r'(?<=[a-zA-Z])(\d)', r' \1', text)
    return result

# Sample Text
sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"

# Call the function and print the result
output_text = insert_spaces(sample_text)
print("Expected Output:", output_text)


# # Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython
# 

# In[14]:


import re

def insert_spaces(text):
    # Use regular expression to insert spaces between words starting with capital letters or numbers
    result = re.sub(r'(?<=[a-zA-Z\d])(?=[A-Z\d])', r' ', text)
    return result

# Sample Text
sample_text = "RegularExpression1IsAn2ImportantTopic3InPython"

# Call the function and print the result
output_text = insert_spaces(sample_text)
print("Expected Output:", output_text)


# # Question 10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.
# Github Link-  https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv
# 

# In[15]:


import pandas as pd

# GitHub link to the dataset
url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"

# Read the data into a DataFrame
df = pd.read_csv(url)

# Extract the first 6 letters of each country and store in a new column
df['first_five_letters'] = df['Country'].str[:6]

# Display the DataFrame with the new column
print(df.head())


# # Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

# In[16]:


import re

def is_valid_string(input_string):
    # Define the regular expression pattern
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')

    # Use re.match() to check if the entire string matches the pattern
    match = re.match(pattern, input_string)

    # Return True if the string is valid, otherwise False
    return bool(match)

# Accept user input
user_input = input("Enter a string: ")

# Check if the input string is valid
result = is_valid_string(user_input)

# Print the result
if result:
    print("The string is valid.")
else:
    print("The string is not valid.")


# # Question 12- Write a Python program where a string will start with a specific number. 

# In[39]:


import re

def starts_with_specific_number(input_string, specific_number):
    # Define the regular expression pattern to check if the string starts with a specific number
    pattern = re.compile(r'^{}'.format(re.escape(specific_number)))

    # Use re.match() to check if the string matches the pattern at the beginning
    match = re.match(pattern, input_string)

    # Return True if the string starts with the specific number, otherwise False
    return bool(match)

# Accept user input for the string and the specific number
user_input_string = input("Enter a string: ")
user_specific_number = input("Enter the specific number to check if the string starts with: ")

# Check if the input string starts with the specific number
result = starts_with_specific_number(user_input_string, user_specific_number)

# Print the result
if result:
    print(f"The string starts with the specific number {user_specific_number}.")
else:
    print(f"The string does not start with the specific number {user_specific_number}.")


# # Question 13- Write a Python program to remove leading zeros from an IP address

# In[18]:


import re

def remove_leading_zeros(ip_address):
    # Define the regular expression pattern to remove leading zeros
    pattern = re.compile(r'\b0+(\d+)\b')

    # Use re.sub() to remove leading zeros
    result = re.sub(pattern, r'\1', ip_address)

    return result

# Accept user input for the IP address
user_input_ip = input("Enter an IP address: ")

# Remove leading zeros from the IP address
result_ip = remove_leading_zeros(user_input_ip)

# Print the result
print("IP address with leading zeros removed:", result_ip)


# # Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
# Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
# Expected Output- August 15th 1947
# Note- Store given sample text in the text file and then extract the date string asked format.
# 

# In[20]:


import re

# Accept user input for sample text
user_input_text = input("Enter a text containing a date: ")

# Define the regular expression pattern to match the date string
pattern = re.compile(r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:st|nd|rd|th)?\s+\d{4}\b')

# Use re.search() to find the match in the user input text
match = re.search(pattern, user_input_text)

# Extract and print the matched date string
if match:
    date_string = match.group()
    print("Matched Date String:", date_string)
else:
    print("No matching date string found.")


# # Question 15- Write a Python program to search some literals strings in a string. 
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'
# 

# In[21]:


import re

def search_words(text, searched_words):
    results = {}

    for word in searched_words:
        pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
        match = re.search(pattern, text)

        if match:
            results[word] = "Found"
        else:
            results[word] = "Not Found"

    return results

# Sample text
sample_text = 'The quick brown fox jumps over the lazy dog.'

# Words to search for
searched_words = ['fox', 'dog', 'horse']

# Call the function and print the results
search_results = search_words(sample_text, searched_words)

# Print the results
for word, result in search_results.items():
    print(f"Word '{word}': {result}")


# # Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'
# 

# In[22]:


import re

def search_word_with_location(text, searched_word):
    pattern = re.compile(re.escape(searched_word), re.IGNORECASE)
    match = re.search(pattern, text)

    if match:
        start_index = match.start()
        end_index = match.end()
        return f"Found '{searched_word}' at position {start_index}-{end_index}."
    else:
        return f"'{searched_word}' not found in the text."

# Sample text
sample_text = 'The quick brown fox jumps over the lazy dog.'

# Word to search for
searched_word = 'fox'

# Call the function and print the result
result = search_word_with_location(sample_text, searched_word)
print(result)


# # Question 17- Write a Python program to find the substrings within a string.
# Sample text : 'Python exercises, PHP exercises, C# exercises'
# Pattern : 'exercises'.
# 

# In[24]:


import re

def find_substrings(text, pattern):
    matches = re.finditer(pattern, text)

    result = [match.group() for match in matches]

    return result

# Sample text
sample_text = 'Python exercises, PHP exercises, C# exercises'

# Substring to search for
searched_substring = 'exercises'

# Call the function and print the result
result_substrings = find_substrings(sample_text, searched_substring)
print("Occurrences of '{}' in the text:".format(searched_substring))
print(result_substrings)


# # Question 18- Write a Python program to find the occurrence and position of the substrings within a string.

# In[25]:


import re

def find_substrings_with_positions(text, pattern):
    matches = re.finditer(pattern, text)

    result = []

    for match in matches:
        occurrence = match.group()
        start_position = match.start()
        end_position = match.end()
        result.append((occurrence, (start_position, end_position)))

    return result

# Sample text
sample_text = 'Python exercises, PHP exercises, C# exercises'

# Substring to search for
searched_substring = 'exercises'

# Call the function and print the result
result_substrings = find_substrings_with_positions(sample_text, re.escape(searched_substring))
print("Occurrences and positions of '{}' in the text:".format(searched_substring))
for substring, positions in result_substrings:
    print("Substring: '{}' - Position: {}-{}".format(substring, positions[0], positions[1]))


# # Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

# In[26]:


import re

def convert_date_format(date_str):
    # Define the regular expression pattern for yyyy-mm-dd format
    pattern = re.compile(r'(\d{4})-(\d{2})-(\d{2})')

    # Use re.sub() to replace yyyy-mm-dd with dd-mm-yyyy
    result = re.sub(pattern, r'\3-\2-\1', date_str)

    return result

# Sample date in yyyy-mm-dd format
sample_date = '2022-02-28'

# Call the function and print the result
converted_date = convert_date_format(sample_date)
print("Converted Date:", converted_date)


# # Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.
# Sample Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
# Expected Output: ['01.12', '145.8', '3.01', '27.25', '0.25']
# 

# In[27]:


import re

def find_decimal_numbers(input_text):
    # Define the regular expression pattern for decimal numbers with precision of 1 or 2
    pattern = re.compile(r'\b\d+\.\d{1,2}\b')

    # Use re.findall() to find all matches in the input text
    result = pattern.findall(input_text)

    return result

# Sample Text
sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"

# Call the function and print the result
output_numbers = find_decimal_numbers(sample_text)
print("Expected Output:", output_numbers)


# # Question 21- Write a Python program to separate and print the numbers and their position of a given string.

# In[28]:


import re

def extract_numbers_with_positions(input_text):
    # Define the regular expression pattern for finding numbers
    pattern = re.compile(r'\d+')

    # Use re.finditer() to find all matches in the input text along with their positions
    result = [(match.group(), match.start(), match.end()) for match in pattern.finditer(input_text)]

    return result

# Sample Text
sample_text = "The price of the product is $45.99 and the discount is 15%."

# Call the function and print the result
numbers_with_positions = extract_numbers_with_positions(sample_text)
print("Numbers with Positions:")
for number, start_position, end_position in numbers_with_positions:
    print(f"Number: {number} - Position: {start_position}-{end_position}")


# # Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
# Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
# Expected Output: 950
# 

# In[29]:


import re

def extract_maximum_numeric_value(input_text):
    # Define the regular expression pattern to match numeric values
    pattern = re.compile(r'\b\d+\b')

    # Use re.findall() to find all numeric values in the input text
    numeric_values = [int(match) for match in pattern.findall(input_text)]

    # Find the maximum numeric value
    if numeric_values:
        max_value = max(numeric_values)
        return max_value
    else:
        return None

# Sample Text
sample_text = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'

# Call the function and print the result
max_numeric_value = extract_maximum_numeric_value(sample_text)
if max_numeric_value is not None:
    print("Maximum Numeric Value:", max_numeric_value)
else:
    print("No numeric values found in the given text.")


# # Question 23- Create a function in python to insert spaces between words starting with capital letters.
# Sample Text: “RegularExpressionIsAnImportantTopicInPython"
# Expected Output: Regular Expression Is An Important Topic In Python
# 

# In[30]:


import re

def insert_spaces_before_capitals(input_text):
    # Define the regular expression pattern to insert spaces before capital letters
    pattern = re.compile(r'([a-z])([A-Z])')

    # Use re.sub() to insert spaces between words starting with capital letters
    result = re.sub(pattern, r'\1 \2', input_text)

    return result

# Sample Text
sample_text = "RegularExpressionIsAnImportantTopicInPython"

# Call the function and print the result
output_text = insert_spaces_before_capitals(sample_text)
print("Expected Output:", output_text)


# # Question 24- Python regex to find sequences of one upper case letter followed by lower case letters

# In[31]:


import re

def find_sequences(input_text):
    # Define the regular expression pattern
    pattern = re.compile(r'[A-Z][a-z]+')

    # Use re.findall() to find all matches in the input text
    result = pattern.findall(input_text)

    return result

# Sample Text
sample_text = "The Quick Brown Fox Jumps Over The Lazy Dog"

# Call the function and print the result
sequences = find_sequences(sample_text)
print("Sequences of one upper case letter followed by lower case letters:")
print(sequences)


# # Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
# Sample Text: "Hello hello world world"
# Expected Output: Hello hello world
# 
# 

# In[32]:


import re

def remove_continuous_duplicates(input_text):
    # Define the regular expression pattern to match continuous duplicate words
    pattern = re.compile(r'\b(\w+)(\s+\1)+\b', flags=re.IGNORECASE)

    # Use re.sub() to remove continuous duplicate words
    result = re.sub(pattern, r'\1', input_text)

    return result

# Sample Text
sample_text = "Hello hello world world"

# Call the function and print the result
output_text = remove_continuous_duplicates(sample_text)
print("Expected Output:", output_text)


# # Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.

# In[33]:


import re

def ends_with_alphanumeric(input_string):
    # Define the regular expression pattern to check if the string ends with an alphanumeric character
    pattern = re.compile(r'\w$')

    # Use re.match() to check if the string matches the pattern at the end
    match = re.match(pattern, input_string)

    # Return True if the string ends with an alphanumeric character, otherwise False
    return bool(match)

# Accept user input for the string
user_input = input("Enter a string: ")

# Check if the input string ends with an alphanumeric character
result = ends_with_alphanumeric(user_input)

# Print the result
if result:
    print("The string ends with an alphanumeric character.")
else:
    print("The string does not end with an alphanumeric character.")


# # Question 27-Write a python program using RegEx to extract the hashtags.
# Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
# Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']
# 

# In[34]:


import re

def extract_hashtags(input_text):
    # Define the regular expression pattern to match hashtags
    pattern = re.compile(r'#\w+')

    # Use re.findall() to find all matches in the input text
    result = pattern.findall(input_text)

    return result

# Sample Text
sample_text = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""

# Call the function and print the result
hashtags = extract_hashtags(sample_text)
print("Expected Output:", hashtags)


# # Question 28- Write a python program using RegEx to remove <U+..> like symbols
# Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
# Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
# Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders
# 

# In[35]:


import re

def remove_unicode_symbols(input_text):
    # Define the regular expression pattern to match <U+..> symbols
    pattern = re.compile(r'<U\+[0-9A-Fa-f]+>')

    # Use re.sub() to replace <U+..> symbols with an empty string
    result = re.sub(pattern, '', input_text)

    return result

# Sample Text
sample_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"

# Call the function and print the result
output_text = remove_unicode_symbols(sample_text)
print("Expected Output:", output_text)


# # Question 29- Write a python program to extract dates from the text stored in the text file.
# Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
# Note- Store this sample text in the file and then extract dates.
# 

# In[36]:


import re

def extract_dates_from_file(file_path):
    # Read the text from the file
    with open(file_path, 'r') as file:
        text_content = file.read()

    # Define the regular expression pattern to match dates in the format DD-MM-YYYY
    pattern = re.compile(r'\b\d{2}-\d{2}-\d{4}\b')

    # Use re.findall() to find all matches in the text
    result = pattern.findall(text_content)

    return result

# Store the sample text in a text file
with open('sample_text.txt', 'w') as file:
    file.write("Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.")

# Call the function and print the result
extracted_dates = extract_dates_from_file('sample_text.txt')
print("Extracted Dates:", extracted_dates)


# # Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
# The use of the re.compile() method is mandatory.
# Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
# Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly.
# 
# 
# 
# 

# In[37]:


import re

def remove_words_of_length_between_2_and_4(input_text):
    # Define the regular expression pattern to match words of length between 2 and 4
    pattern = re.compile(r'\b\w{2,4}\b')

    # Use re.sub() to replace words with length between 2 and 4 with an empty string
    result = re.sub(pattern, '', input_text)

    return result

# Sample Text
sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

# Call the function and print the result
output_text = remove_words_of_length_between_2_and_4(sample_text)
print("Expected Output:", output_text)


# In[ ]:




