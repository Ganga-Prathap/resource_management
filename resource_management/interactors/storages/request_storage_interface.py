from abc import abstractmethod
from typing import List
from .dtos import RequestDto


class RequestStorageInterface:

    @abstractmethod
    def get_admin_requests(self, offset: int, limit: int) -> List[RequestDto]:
        pass

    @abstractmethod
    def get_total_requests_count(self) -> int:
        pass
