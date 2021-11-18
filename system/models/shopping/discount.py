"""
This module contains the classes DiscountCategory and SeasonalDiscount. The module
imports the datetime class from the datetime module, the Calendar class from the
calendar module, and the AbstractObserver class from the observer module, both in
the systems shopping package.
"""
from datetime import datetime
from system.models.shopping.calendar import Calendar
from system.models.shopping.observer import AbstractObserver


class DiscountCategory:
    """
    This class represents a model of a discount category, containing a constructor,
    and the getter methods for its parameters.
    """
    def __init__(self, discount_id: int, discount_name: str, discount_percentage: float):
        """
        This constructor instantiates a discount category object.

        :param discount_id: ID of the discount category.
        :param discount_name: Name of the discount category.
        :param discount_percentage: Discount percentage of the discount category.
        """
        self.discount_id = discount_id
        self.discount_name = discount_name
        self.discount_percentage = discount_percentage

    def get_discount_id(self) -> int:
        """
        This method gets the discount ID.

        :returns: ID of the discount category.
        """
        return self.discount_id

    def get_discount_name(self) -> str:
        """
        This method gets the discount name.

        :returns: Name of the discount category.
        """
        return self.discount_name

    def get_discount_percentage(self) -> float:
        """
        This method gets the discount percentage.

        :returns: Discount percentage of the discount category.
        """
        return self.discount_percentage


class SeasonalDiscount(AbstractObserver):
    """
    This class represents a model of a seasonal discount and implements AbstractObserver.
    The class contains a constructor, a method to check if the seasonal discount is active,
    and the implemented abstract method.
    """
    def __init__(self, discount_name: str, start_date: datetime, end_date: datetime):
        """
        This constructor instantiates a seasonal discount object.

        :param discount_name: Name of the discount.
        :param start_date: Starting date/time of the discount.
        :param end_date: Ending date/time of the discount.
        """
        self.discount_name = discount_name
        self.start_date = start_date
        self.end_date = end_date
        self.current_date = None  # will be updated immediately when calendar subject attaches

    def check_if_active(self):
        """This method checks if the seasonal discount is active."""
        bool(self.start_date <= self.current_date <= self.end_date)

    def update(self, subject):
        # can only perform this update if the subject is a calendar as defined in calendar.py
        if isinstance(subject, Calendar):
            self.current_date = subject.get_date()


# brief test to see if this works
discount_start = datetime(2021, 1, 1)
discount_end = datetime(2021, 1, 31)
jan_discount = SeasonalDiscount("January", discount_start, discount_end)

cal = Calendar()
cal.attach(jan_discount)
print(cal.get_date())
print(jan_discount.check_if_active())
