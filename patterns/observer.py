class Observer:
    def update(self, message):
        raise NotImplementedError("Subclasses should implement this!")


class UserObserver(Observer):
    def __init__(self, username):
        self.username = username

    def update(self, message):
        print(f"📣 [Notification to {self.username}] {message}")
