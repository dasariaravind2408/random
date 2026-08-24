import math

queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]


def show_queue(queue):
  
  print("[the queue goes here]")

# Function stubs go here
def add_singer(queue):
  print("[add a singer]")


def remove_singer(queue): 
  print("[remove a singer]")

def run_app(queue):
    print("=" * 44)
    print("Welcome to Sing Out: A Karaoke Queue Manager")
    print("=" * 44)

    is_running = True 

    while is_running: 
      show_queue(queue)
      print()
      print("Options:  add / remove / quit")
      command = input("> ")

      if command == "quit": 
        is_running = False
        print("Goodnight!")
      elif command == "add": 
        add_singer(queue)
      elif command == "remove":
        remove_singer(queue)
      else: 
        print(f"Sorry, I don't know the command '{command}'")

run_app(queue)
