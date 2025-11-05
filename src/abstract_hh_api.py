from abc import ABC, abstractmethod
from typing import Any, List


class AbstractHHApi(ABC):

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Any] | None:
        pass
