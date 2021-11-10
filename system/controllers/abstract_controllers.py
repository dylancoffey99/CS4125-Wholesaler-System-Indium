from abc import ABC, abstractmethod


class AbstractAccessController(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def login_view(self, root, frame):
        pass

    @abstractmethod
    def register_view(self, root, frame):
        pass

    @abstractmethod
    def login_user(self, root, frame):
        pass

    @abstractmethod
    def register_user(self, root, frame):
        pass

    @abstractmethod
    def destroy_frame(self, frame):
        pass

    @abstractmethod
    def hash_password(self, password: str) -> str:
        pass
