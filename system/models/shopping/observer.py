from abc import ABC, abstractmethod


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


class IObserver(ABC):
    @abstractmethod
    def update(self, subject):
        pass
