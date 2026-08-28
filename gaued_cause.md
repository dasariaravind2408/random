def serve_order(orders):
  if len(orders) == 0:
    print("Nothing left to serve.")
    return
    
  item = orders.pop(0)
  print(f"Serving: {item}")

serve_order([])

