try: 
  number = int("banana")
except ValueError:
  print("Please enter a number.")



  try: 
  age = int(input("How old are you? "))
  print(f"You'll be {age + 1} next year.")
except ValueError:
  print("Please enter a number.")
