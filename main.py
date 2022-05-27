# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = str(input("Enter a word: "))
    anagram = str(input("Enter another word: "))
    word_1 = sorted(word)
    word_2 = sorted(anagram)

    if word_1 == word_2:
        return True

    else:
        return False

output = find_anagram("elbow", "below")

print(output)