class FileStoreBot:
    def init(self):
        self.users = {}
        self.requests = []

    def add_user(self, user_id, username):
        self.users[user_id] = username

    def remove_user(self, user_id):
        del self.users[user_id]

    def request_to_join(self, user_id):
        if user_id not in self.users and user_id not in self.requests:
            self.requests.append(user_id)

    def approve_request(self, user_id):
        if user_id in self.requests:
            username = self.users[user_id]
            self.add_user(user_id, username)
            self.requests.remove(user_id)

    def print_users(self):
        print("Users:")
        for user_id, username in self.users.items():
            print(f"User ID: {user_id}, Username: {username}")

    def print_requests(self):
        print("Join Requests:")
        for user_id in self.requests:
            print(f"User ID: {user_id}")


# Example usage
bot = FileStoreBot()

# Adding users
bot.add_user(1, "Alice")
bot.add_user(2, "Bob")
bot.add_user(3, "Charlie")

# Printing users
bot.print_users()

# Requesting to join
bot.request_to_join(4)
bot.request_to_join(5)

# Printing requests
bot.print_requests()

# Approving a request
bot.approve_request(4)

# Printing users after approval
bot.print_users()
