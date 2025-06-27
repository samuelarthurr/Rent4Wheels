from models.user import User
from models.vehicle import Vehicle
from services.booking_service import process_booking

if __name__ == "__main__":
    # Test users
    verified_user = User("Alice", is_verified=True)
    unverified_user = User("Bob", is_verified=False)

    # Test vehicle
    car = Vehicle("V123", "Toyota Camry")

    # Process bookings
    print("--- Booking by Verified User ---")
    process_booking(verified_user, car)

    print("\n--- Booking by Unverified User ---")
    process_booking(unverified_user, car)
