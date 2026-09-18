def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

user_text = input("Enter a sentence to count its vowels: ")
total_vowels = count_vowels(user_text)
print(f"There are {total_vowels} vowels in your sentence.")