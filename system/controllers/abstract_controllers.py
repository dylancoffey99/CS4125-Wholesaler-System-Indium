from abc import ABC, abstractmethod


class AbstractController(ABC):
    @abstractmethod
    def logout_user(self):
        pass

    @abstractmethod
    def attach_observers(self):
        pass
