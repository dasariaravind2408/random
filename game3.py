queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]

def show_queue(queue):
  print()
  print("Current queue:")
  print()
  for singer in queue:
    name, song = singer
    print(f"{name} - {song}")
  print()
  print("Options:  add / remove / quit")

def prompt_for_singer():
  name = input("Name: ").strip().title()
  song = input("Song: ").strip().title()
  return name, song

def add_singer(queue):
  name, song = prompt_for_singer()
  queue.append((name, song))
  print()
  print(f"Added {name} to the queue.")


def remove_singer(queue): 
  print("[remove a singer]")

def run_app(queue):
    print("=" * 44)
    print("Welcome to Sing Out: A Karaoke Queue Manager")
    print("=" * 44)

    is_running = True 

    while is_running: 
      show_queue(queue)
      command = input("> ")

      if command == "quit": 
        is_running = False
        print("The queue is closed. Good night!")
      # your commands go here 
      elif command == "add": 
        add_singer(queue)
      elif command == "remove":
        remove_singer(queue)
      else: 
        print(f"Sorry, I don't know the command '{command}'")

run_app(queue)
