from abc import ABC, abstractmethod


class AbstractController(ABC):
    @abstractmethod
    def logout_user(self):
        pass


class AbstractObserverController(ABC):
    @abstractmethod
    def attach_observers(self):
        pass
