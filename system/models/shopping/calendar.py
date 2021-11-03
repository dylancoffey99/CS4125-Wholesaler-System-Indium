import datetime
from system.models.shopping.observer import ISubject


class Calendar(ISubject):
    def __init__(self):
        # datetime object, always 1/1/2021 initially
        self.current_date = datetime.datetime(2021, 1, 1)
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)
        self.notify()  # update new observers with the date, as they may not have it

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def advance_time(self):
        # adding a timedelta object to a datetime object will increment the datetime values
        # in this case, 1 day is being added on to the datetime created in the init function
        self.current_date += datetime.timedelta(days=1)
        self.notify()
        print("Time advanced by 1 day. The current date is "
              + self.current_date.strftime("%d/%m/%Y"))

    # once the date is retrieved, further actions such as extracting
    # the exact month and day may be performed on the object
    def get_date(self):
        return self.current_date

    # set any date desired, this may be useful for testing purposes
    def set_date(self, new_date):
        if isinstance(new_date, datetime.date):
            self.current_date = new_date
            self.notify()
        else:
            raise Exception("This function will only accept datetime.date objects.")
