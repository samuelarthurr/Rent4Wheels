class User:
    def __init__(self, username, is_verified=False):
        self.username = username
        self.is_verified = is_verified

    def __str__(self):
        return self.username
