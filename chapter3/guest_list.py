guest_list = ['Eric', 'Robert', 'Charlie', 'Kale']
guest_list[0] = 'Irwin'
guest_list.insert(0, 'Marco')
guest_list.insert(2, 'Geni')
guest_list.append('John')
print("My new table can't arrive on dinner, so I can only invite two guest.")
popped_guest1 = guest_list.pop()
print(f"{popped_guest1}, I am very sorry, that I can't invite you.")
popped_guest2 = guest_list.pop()
print(f"{popped_guest2}, I am very sorry, that I can't invite you.")
popped_guest3 = guest_list.pop()
print(f"{popped_guest3}, I am very sorry, that I can't invite you.")
popped_guest4 = guest_list.pop()
print(f"{popped_guest4}, I am very sorry, that I can't invite you.")
popped_guest5 = guest_list.pop()
print(f"{popped_guest5}, I am very sorry, that I can't invite you.")
del guest_list[0]
del guest_list[0]
print(guest_list)

print("I have {len(guest_list))} guest today}.")

