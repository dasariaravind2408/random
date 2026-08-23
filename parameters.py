def add_numbers(num1, num2):
  print(num1 + num2)

add_numbers(2, 3)
add_numbers(10, 45)

def scramble(word):
  letters = list(word)
  random.shuffle(letters)
  print("".join(letters))

scramble("treasure")
