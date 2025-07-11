# 1. Indexing and Slicing
s = "PythonPractice"
print("1. Indexing and Slicing")
print("s[1]:", s[1])         # 'y'
print("s[-3:]:", s[-3:])     # 'ice'
print("s[2:7]:", s[2:7])     # 'thonP'

print("\n2. Reverse a String")
# 2. Reverse a String (One-liner)
print("Reversed:", "developer"[::-1])  # 'repoleved'


print("\n3. Count Vowels")
# 3. Count Vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print("Vowels in 'Hello World':", count_vowels("Hello World"))


print("\n4. Check for Palindrome")
# 4. Check for Palindrome
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

print("Is 'A man a plan a canal Panama' palindrome?:", is_palindrome("A man a plan a canal Panama"))


print("\n5. Clean and Format String")
# 5. Clean and Format String
text = "   hello world! welcome to Python.   "
cleaned = text.strip().title().replace("Python", "Programming")
print("Formatted Text:", cleaned)


print("\n6. Find Longest Word")
# 6. Find Longest Word
def find_longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print("Longest word:", find_longest_word("Practice makes a programmer perfect"))


print("\n7. String Operators")
# 7. String Operators
s1 = "Py"
s2 = "thon"
print("s1 + s2:", s1 + s2)         # 'Python'
print("s1 * 3:", s1 * 3)           # 'PyPyPy'
print("'y' in s1:", "y" in s1)     # True


print("\n8. Remove Duplicate Characters")
# 8. Remove Duplicate Characters
def remove_duplicates(s):
    seen = set()
    result = ""
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    return result

print("After removing duplicates:", remove_duplicates("programming"))


print("\n9. Check for Anagram")
# 9. Check for Anagram
def are_anagrams(str1, str2):
    s1 = ''.join(str1.lower().split())
    s2 = ''.join(str2.lower().split())
    return sorted(s1) == sorted(s2)

print("Are 'listen' and 'silent' anagrams?:", are_anagrams("listen", "silent"))


print("\n10. Word Frequency Counter")
# 10. Word Frequency Counter
def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print("Word frequencies:", word_frequency("Hello world! Hello Python world!"))