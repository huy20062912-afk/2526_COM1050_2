# Exercise 387: First Unique Character in a String

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s) # Count occurrences of each character in the string
        for i, char in enumerate(s): # Iterate through the string with index
            if count[char] == 1: # Check if the character is unique
                return i # Return the index of the first unique character
        return -1

# I used Ai for this...
# P new to counter and dictionary as a whole
# Code explanation:
# Importing Counter from collections module to count occurrences of each character in the string.
# Defining a class Solution with a method firstUniqChar that takes a string s as input and returns an integer.
# Using Counter to create a dictionary-like object that counts the occurrences of each character in the string.
# Iterating through the string with enumerate to get both index and character.
# Checking if the count of the character is 1 (i.e., it is unique).