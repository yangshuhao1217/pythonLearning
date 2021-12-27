def send_messages(unsent_messages, sent_messages):
    """
    Simulate sending messages, until none are left.
    Move each message to sent_messages.
    """
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    """Show all the sent messages."""
    print("\nThe following messages have been sent:")
    for sent_message in sent_messages:
        print(sent_message)

unsent_messages = ['Hello', 'Hola', 'Nihao']
sent_messages = []

send_messages(unsent_messages[:], sent_messages)
show_sent_messages(sent_messages)
print(unsent_messages)
