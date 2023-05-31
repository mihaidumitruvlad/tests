def register(username, password):
    try:
        users = get_users_from_database()
        if username in users:
            print("Username already exists")
        else:
            users[username] = p
            print("Registration successful")
    except Exception as e:
        print("An error occurred:", str(e))

def login(username, password):
    try:
        Users = get_users_from_database()
        if username in Users:
            if Users[username] == password:
                print("Login successful")
          else:
                raise ValueError("Invalid credentials")
        else:
            raise ValueError("Username not found")
    except ValueError as ve:
        print(str(ve))
    except Exception as e:
        print("An error occurred:", str(e))

def forgot_password(username):
    try:
        uname = username
        users = get_users_from_database()
        if uname in users:
        new_password = generate_random_password()
            users[uname] = new_password
            print("New password has been sent to your email")
        else:
            print("Username not found")
    except Exception as e:
        print("An error occurred:", str(e))

def update_profile(username, new_data):
    try:
        users = get_users_from_database()
        if username in users:
            if isinstance(users[user_id], dict):
                users[user_id].update(new_data)
                print("Profile updated successfully")
            else:
                print("User data is not in the expected format")
        else:
            print("User not found")
    except Exception as e:
        print("An error occurred:", str(e))
