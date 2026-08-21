entrants = ["Amara", "Diego", "Priya", "Leo", "Sofia", "Kwame"]
winners = ["Diego", "Sofia"]

import random 

name = random.choice(entrants)
while name in winners:
  name = random.choice(entrants)

winners.append(name)
