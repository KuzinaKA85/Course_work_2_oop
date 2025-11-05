import json
import os
from abc import ABC, abstractmethod
from typing import Any
from src.headhunter_api import HeadHunterAPI


class JSONWorker(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(JSONWorker):
    """Класс для работы с json-файлом"""

    def __init__(self, filename: str = "..data/vacancies.json"):
        self.file_worker = HeadHunterAPI()

    def read(self) -> Any:
        """Чтение данных из JSON файла"""
        try:
            with open(self.file_worker, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            raise ValueError(f"Файл {self.file_worker} содержит некорректный JSON")

    def add_vacancy(self, data: Any) -> None:
        """Запись данных в JSON файл"""
        # Создаем папки если нужно
        # os.makedirs(os.path.dirname(self.file_worker) or '.', exist_ok=True)

        with open(self.file_worker, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    # def exists(self) -> bool:
    #     """Проверка существования файла"""
    #     return os.path.exists(self.file_worker)

    def delete_vacancy(self) -> bool:
        """Удаление файла"""
        try:
            os.remove(self.file_worker)
            return True
        except FileNotFoundError:
            return False
