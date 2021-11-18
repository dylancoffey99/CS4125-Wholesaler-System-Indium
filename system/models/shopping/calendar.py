"""
This module contains the Calendar class. The module imports the datetime, timedelta,
and date classes from the datetime module, and the AbstractSubject class from the
observer module, in the systems shopping package.
"""
from datetime import datetime, timedelta, date
from system.models.shopping.observer import AbstractSubject


class Calendar(AbstractSubject):
    """
    This class represents a model of a calendar and implements AbstractSubject.
    The class contains a constructor, an advance_time method, the getters/setter
    methods for its variables, and the implemented abstract methods.
    """
    def __init__(self):
        """This constructor instantiates a calendar object."""
        # datetime object, always 1/1/2021 initially
        self.current_date = datetime(2021, 1, 1)
        self.observers = []

    def advance_time(self):
        """
        This method advances the calendars current date by one day, and notifies
        the observers.
        """
        # adding a timedelta object to a datetime object will increment the datetime values
        # in this case, 1 day is being added on to the datetime created in the init function
        self.current_date += timedelta(days=1)
        self.notify()
        print("Time advanced by 1 day. The current date is "
              + self.current_date.strftime("%d/%m/%Y"))

    # once the date is retrieved, further actions such as extracting
    # the exact month and day may be performed on the object
    def get_date(self):
        """
        This method gets the current date of the calendar.

        :returns: Current date/time of the calendar.
        """
        return self.current_date

    # set any date desired, this may be useful for testing purposes
    def set_date(self, new_date: date):
        """
        This method sets the current date of the calendar, and notifies the observers.

        :param new_date: New date to be set to the current date of the calendar.
        """
        self.current_date = new_date
        self.notify()

    def attach(self, observer):
        self.observers.append(observer)
        self.notify()  # update new observers with the date, as they may not have it

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)
