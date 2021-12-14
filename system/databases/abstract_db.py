from abc import ABC, abstractmethod


class AbstractDB(ABC):
    @abstractmethod
    def check_db(self):
        pass

    @abstractmethod
    def create_db(self):
        pass
