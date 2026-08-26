contacts = ["Aravind", "siddhu", "Harika","Rashmitha"]

def remove_contacts(contacts, name):
  for contact in contacts:
    if contact == name:
      contacts.remove(contact)
      print(f"Removed {name}.")
      return # bare return means it will stoppes the function 
  print(f"{name} isn't in your contacts.")

remove_contacts(contacts, "Aravind")
