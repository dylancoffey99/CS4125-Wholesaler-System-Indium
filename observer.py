# observer.py
# defines observer and subject interfaces
# Author: Nikita Basovs 18233244

# abstract classes in python
from abc import ABC, abstractmethod


# subject interface
class ISubject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


# observer interface
class IObserver(ABC):
    @abstractmethod
    def update(self, subject):
        pass
