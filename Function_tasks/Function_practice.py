# Level 1: The Warm-Ups
# 1. The "Hype Man"

def hype_man(name, skill):
    print(f"Make some noise for {name}, the absolute master of {skill}!")
hype_man(input("Enter name: "), input("Enter skill: "))


# 2. The Digital Bouncer
def check_age(age):
    if age >= 12:
        print("Enjoy the ride!")
    else:
        print("Sorry, maybe next year.")
check_age(int(input("Enter your age: ")))


# Level 2: Data Structures & Loops
# 3. The Vowel Vacuum
def vowel_vacuum(text):
    s = ""
    for ch in text:
        if ch not in "aeiouAEIOU":
            s += ch
    return s
print(vowel_vacuum(input("Enter a text: ")))



# 4. The Splurge Calculato
def calculate_total(cart_prices):
    total = 0
    for i in cart_prices:
        total += i

    if total > 100:
        return f"Your total today is ${total - (total*(10/100))}"
    else:
        return f"Your total today is ${total}"

print(calculate_total([25.50, 40.00, 50.00]))


# Level 3: Dictionary & Set Integration
# 5. The Emoji Translator
def emojify(sentence, emoji_dict):
    words = sentence.split()

    for index, word in enumerate(words):
        if word in emoji_dict:
            words[index] = emoji_dict[word]

    print(" ".join(words))

my_dict = {"happy": "😊", "pizza": "🍕", "python": "🐍"}
emojify("I am so happy to eat pizza and code python", my_dict)


# 6. The Unique Ingredient Finder
def print_shopping_list(recipe1, recipe2):
    set1 = set(recipe1)
    set2 = set(recipe2)
    print(list(set1.union(set2)))

print_shopping_list(["flour", "sugar", "eggs"], ["eggs", "butter", "sugar", "vanilla"])



# Level 4: The Boss Fight
# 7. The Anagram Detective
def check_anagram(word1, word2):
	w1 = word1.lower().replace(" ", "")
	w2 = word2.lower().replace(" ", "")

	if sorted(w1) == sorted(w2):
		print("Yes, those are anagrams!")
	else:
		print("Nope, not an anagram.")

check_anagram("Clint Eastwood", "Old West Action")
