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
