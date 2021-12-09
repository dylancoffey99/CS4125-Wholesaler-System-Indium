from abc import ABC, abstractmethod


class AbstractController(ABC):
    @abstractmethod
    def logout_user(self):
        pass


class AbstractControllerObserver(ABC):
    @abstractmethod
    def attach_observers(self):
        pass
