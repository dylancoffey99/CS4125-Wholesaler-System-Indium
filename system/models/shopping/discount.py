import datetime
from system.models.shopping import calendar
from system.models.shopping.observer import IObserver


class DiscountCategory:
    def __init__(self, name, desc, discount_percentage):
        self._name = name
        self._desc = desc
        self._discount_percentage = discount_percentage

    def get_name(self):
        return self._name

    def get_description(self):
        return self._desc

    def get_discount(self):
        return self._discount_percentage

# testing some categories
education_discount_category = DiscountCategory("Education",
                                               "Purchasing on behalf of educational institution",
                                               10)

business_discount_category = DiscountCategory("Business",
                                              "Purchasing on behalf of a medium to large business",
                                              15)

startup_discount_category = DiscountCategory("Startup",
                                             "Purchasing on behalf of a small business or startup",
                                             20)

print("Discount for category " + startup_discount_category.get_name() + " is " + \
      str(startup_discount_category.get_discount()) + "%")


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
