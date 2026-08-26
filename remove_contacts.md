contacts = ["Aravind", "siddhu", "Harika","Rashmitha"]

def remove_contacts(contacts, name):
  for contact in contacts:
    if contact == name:
      contacts.remove(contact)
      print(f"Removed {name}.")
      return # bare return means it will stoppes the function 
  print(f"{name} isn't in your contacts.")

remove_contacts(contacts, "Aravind")




def remove_singer(queue): 
  name = input("Who do you want to remove? ").strip().title()
  print()
  for singer in queue:
    if singer[0] == name:
      queue.remove(singer)
      print(f"Removed {name} from the queue.")
      return 
  print(f"There's no one named {name} in the queue.")
  this is in the game 
  
