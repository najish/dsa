# 1. Create an array and print all elements

'''
Basic String Problems
These focus on fundamentals like iteration, indexing, and basic transformations.

Print each character of a string.

Find the length of a string without using len().

Count vowels and consonants in a string.

Convert string to uppercase and lowercase.

Reverse a string (without using slicing [::-1]).

Check if a string is a palindrome.

Count how many times a character appears in a string.

Find the first non-repeating character.

Replace all spaces in a string with -.

Remove all whitespace from a string.

Check if a substring exists in a string.

Find the index of first and last occurrence of a substring.

Remove all digits from a string.

Count the number of words in a sentence.

Swap the case of all characters in a string.

Remove punctuation from a string.

Find ASCII value of each character in a string.

Join a list of words into a single string.

Split a string into a list of words.

Check if two strings are equal (case-sensitive and case-insensitive).

Intermediate String Problems
These require a bit more logic, pattern matching, and string manipulation.

Check if two strings are anagrams.

Find the longest word in a sentence.

Reverse the order of words in a sentence.

Find the most frequent character in a string.

Remove all duplicate characters from a string.

Find all permutations of a string.

Check if a string contains only digits.

Count the frequency of each word in a sentence.

Implement your own startswith() and endswith() function.

Compress a string (e.g., "aaabbc" → "a3b2c1").

Find the longest common prefix among an array of strings.

Check if a string is a valid palindrome ignoring spaces and punctuation.

Find all substrings of a given string.

Implement a simple pattern matching function (without regex).

Rotate characters in a string by k positions.

Convert a Roman numeral string to an integer.

Find the first repeated word in a sentence.

Check if a string can be rearranged into a palindrome.

Find the longest substring without repeating characters.

Replace multiple spaces in a string with a single space.
'''


from os import replace


def first_array():
    arr = [1,2,3,4,5]
    for item in arr:
        print(item)

    return arr 

def length_array(arr):
    return len(arr)



def find_length(arr):
    count = 0
    for item in arr:
        count += 1
    return count


def reverse_string(str1):
    result = ""
    for i in range(len(str1) - 1, -1, -1):
        result = result + str1[i]        
    return result 


def palindrome(str1):
    j = len(str1) - 1
    for i in range(len(str1) // 2):
        if str1[i] != str1[j]:
               return False
        j -= 1
    return True


def countVowelConsonants(str1):
    vowel = consonant = 0
    for c in str1:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            vowel += 1
        else:
            consonant += 1

    return vowel, consonant


def character_occurances(str1, x):
    result = {}
    for c in str1:
        if result.__contains__(c):
            result[c] += 1
        else:
            result[c] = 1
    return result[x] 




    for c in str1:
        pass 



def find_ascii(char):
    return ord(char)


def find_non_repeating_character(str1):
    list = []
    test = True
    for c in str1:
        if test:
            test = False 
            list.append(c)
        elif c in list:
            continue
        else:
            return c


def find_non_repeating_character2(str1):
    flag = None
    test = True
    for c in str1:
        if test:
            test = False 
            flag = c 
        elif c == flag:
            continue
        else:
            return c
        
def first_non_repeating_character(str1):
    result = {}

    for c in str1:
        if result.__contains__(c):
            result[c] += 1
        else:
            result[c] = 1
    
    for c in str1:
        if result[c] == 1:
            return c
    return None



def replace_space_with_hyphen(str1):
    result = ""
    for i in range(len(str1)):
        if str1[i] == ' ':
            result = result + '-'
        else: 
            result = result + str1[i]
    return result 


def remove_all_white_spaces(str1):
    result = ''
    for c in str1:
        if c == ' ':
            continue
        result = result + c
    return result 




def substring_in_string_builtin(str1, substr):
    return str1.__contains__(substr)



print(substring_in_string_brute('zafer eqbal','afer-eq'))