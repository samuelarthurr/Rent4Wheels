from models.booking import Booking


class BookingProxy:
    def __init__(self, booking_class=Booking):
        self.booking_class = booking_class

    def make_booking(self, user, vehicle):
        if not user.is_verified:
            return f"Booking denied. {user} is not a verified user."
        booking = self.booking_class(user, vehicle)
        return booking.confirm()
