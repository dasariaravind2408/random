tasks = ["do laundry", "call mom"]

tasks.insert(0, "pay rent")
print(tasks)

todo = tasks.pop(2)
tasks.insert(0, todo)


def move_to_top(queue):
  position = int(input("Who do you want to move to the top? Enter a number: "))
  print()
  queue.pop(position - 1)
