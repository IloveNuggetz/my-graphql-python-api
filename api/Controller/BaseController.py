from abc import abstractmethod, ABC


class BaseController(ABC):
    bp = None

    @property
    @abstractmethod
    def get_bp():
        pass
