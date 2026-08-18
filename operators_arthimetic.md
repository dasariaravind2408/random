unread_messages = 0
age = 25
cart_total = 45
tickets_left = 8

print(f"Has unread message (more than 0): {unread_messages > 0}")
print(f"Old enough to rent a car (25 or older): {age >= 25}")
print(f"Under the $50 free-shipping minimum: {cart_total < 50}")
print(f"Sold out (0 or fewer tickets left): {tickets_left <= 0}")
