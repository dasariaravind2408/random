import random

words = ["apple", "orange", "banana"]

word = random.choice(words)
print(word)

letters = list(word)
random.shuffle(letters)
scrambled_word = "".join(letters).upper()

print(f"Scrambled: {scrambled_word}")

guess = input("Guess the word or type 'skip' to skip").strip().lower()

if guess == "skip":
  print(f"Skipped The word was '{word}'.")
