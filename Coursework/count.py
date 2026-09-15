def count_letter(text, letter):
    count = 0
    for ch in text.lower():
        if ch == letter.lower():
            count = count + 1
    return count

sentence = input("What's the word or sentence? ")
target = input("What's the target letter? ")

if len(target) != 1:
    print("Please enter one letter as the target.")
else:
    times = count_letter(sentence, target)
    if times == 0:
        print("Sure about the target?")
    else:
        print("The letter", target, "appears", times, "times")