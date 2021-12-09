from abc import ABC, abstractmethod


class AbstractView(ABC):
    @abstractmethod
    def setup_view(self):
        pass

    @abstractmethod
    def load_labels(self):
        pass

    @abstractmethod
    def load_interactions(self):
        pass

    @abstractmethod
    def clear_frame(self):
        pass


class AbstractViewSubject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def notify(self, command: int):
        pass
