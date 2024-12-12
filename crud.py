class User:
    def __init__(self, username, password, active=True):
        self.username = username
        self.password = password
        self.active = active

    def __repr__(self):
        return f"User(username='{self.username}', active={self.active})"


class UserService:
    def __init__(self):
        self.users = []

    # Create a new user
    def create_user(self, username, password, active=True):
        if any(user.username == username for user in self.users):
            raise ValueError("User with this username already exists.")
        user = User(username, password, active)
        self.users.append(user)
        return user

    # Read all users
    def read_users(self):
        return self.users

    # Read a specific user by username
    def read_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        raise ValueError("User not found.")

    # Update a user
    def update_user(self, username, password=None, active=None):
        user = self.read_user(username)
        if password is not None:
            user.password = password
        if active is not None:
            user.active = active
        return user

    # Delete a user
    def delete_user(self, username):
        user = self.read_user(username)
        self.users.remove(user)
        return user


# Example usage
if __name__ == "__main__":
    service = UserService()

    # Create users
    service.create_user("rahul_krishnan", "password123")
    service.create_user("lekshmi_nair", "securepass", active=False)

    # Read all users
    print("All Users:", service.read_users())

    # Read a specific user
    print("Read User:", service.read_user("rahul_krishnan"))

    # Update a user
    service.update_user("rahul_krishnan", password="newpassword", active=False)
    print("Updated User:", service.read_user("rahul_krishnan"))

    # Delete a user
    service.delete_user("lekshmi_nair")
    print("All Users after Deletion:", service.read_users())
