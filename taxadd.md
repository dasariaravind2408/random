lineup = [
    ("The Wailers", "reggae", 45),
    ("Daft Punk", "electronic", 90),
    ("Adele", "pop", 60),
    ("Metallica", "metal", 100),]

for act in lineup:
  band, genre, minutes = act
  if minutes >= 90: 
    print(f"{band} ({genra}) plays a long set: {minutes} minutes")
  else: 
    print(f"{band} ({genre}) plays {minutes} minutes")
