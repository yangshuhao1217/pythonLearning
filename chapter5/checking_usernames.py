current_users = ['mike', 'kai', 'ray', 'MIKE', 'marina', 'maria']
new_users = ['henry', 'jef', 'mike', 'maria', 'KAI', 'robert']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user.title()}, you need to enter a new username.")
    else:
        print(f"{new_user.title()}, your username is available.")
