from random import choice


def get_winning_ticket(possibilities):
    """Pull winning ticket."""
    winning_ticket = []


    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)


        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket


def check_ticket(played_ticket, winning_ticket):
    # Check every number and letter, if anyone isn't in winning ticket, return False.
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    # If code run here, you win!
    return True


def make_random_ticket(possibilities):
    """Randomly make lottery,"""
    ticket = []
    
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays > max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
