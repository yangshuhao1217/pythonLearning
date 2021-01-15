# Started with the orders of sandwiches.
# and an empty list of finished orders.
sandwich_orders = ['tuna', 'pastrami', 'butter', 'pastrami', 'egg', 'pastrami']
# deli has run out of pastrami.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_orders = []

# Print message what sandwich was already made.
# Move each made sandwich into the list of finished sandwiches.

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I have made {current_sandwich}.")
    finished_orders.append(current_sandwich)

# Display all finished sandwiches.
print("\nHere what sandwich was made:")
for finished_order in finished_orders:
    print(finished_order)
