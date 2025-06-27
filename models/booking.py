class Booking:
    def __init__(self, user, vehicle):
        self.user = user
        self.vehicle = vehicle

    def confirm(self):
        return f"Booking confirmed for {self.user} - {self.vehicle}"
