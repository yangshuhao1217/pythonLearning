def build_profile(first, last, **user_info):
    """Build a dictionary containing everything about me."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile(
        'shuhao', 'yang',
        hobbi='programming',
        language='python',
        os='mac os')
print(user_profile)
