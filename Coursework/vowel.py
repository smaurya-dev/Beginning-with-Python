def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count = count + 1
    return count

word = input("What's the word? ")
print("Vowels in", word, "=", count_vowels(word))