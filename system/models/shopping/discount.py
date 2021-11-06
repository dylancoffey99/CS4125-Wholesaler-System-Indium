import datetime
from system.models.shopping import calendar
from system.models.shopping.observer import IObserver


class DiscountCategory:
    def __init__(self, discount_id: int, discount_name: str, discount_percentage: int):
        self._discount_id = discount_id
        self._discount_name = discount_name
        self._discount_percentage = discount_percentage

    def get_discount_id(self) -> int:
        return self._discount_id

    def get_discount_name(self) -> str:
        return self._discount_name

    def get_discount_percentage(self) -> int:
        return self._discount_percentage


class SeasonalDiscount(IObserver):
    def __init__(self, name, start_date, end_date):
        self._name = name
        self._start_date = start_date
        self._end_date = end_date
        self._current_date = None  # will be updated immediately when calendar subject attaches

    def update(self, subject):
        # can only perform this update if the subject is a calendar as defined in calendar.py
        if isinstance(subject, calendar.Calendar):
            self._current_date = subject.get_date()

    def check_if_active(self):
        bool(self._start_date <= self._current_date <= self._end_date)


# brief test to see if this works
discount_start = datetime.datetime(2021, 1, 1)
discount_end = datetime.datetime(2021, 1, 31)
jan_discount = SeasonalDiscount("January", discount_start, discount_end)

cal = calendar.Calendar()
cal.attach(jan_discount)
print(cal.get_date())
print(jan_discount.check_if_active())
