from patterns.proxy import BookingProxy
from patterns.observer import UserObserver
from utils.notifier import Notifier


def process_booking(user, vehicle):
    # Proxy check
    proxy = BookingProxy()
    result = proxy.make_booking(user, vehicle)

    # Observer notify
    notifier = Notifier()
    observer = UserObserver(user.username)
    notifier.subscribe(observer)
    notifier.notify(result)
