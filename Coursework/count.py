def count_letter(text, letter):
    count = 0
    for ch in text.lower():
        if ch == letter.lower():
            count = count + 1
    return count

sentence = input("What's the word or sentence? ")
target = input("What's the target letter? ")
if target in sentence: 
    print("The letter", target, "appears", count_letter(sentence, target), "times")
else: 
    print("Sure about the target?")