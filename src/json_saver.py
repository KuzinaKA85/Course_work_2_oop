import json
import os
from typing import Any, Dict, List, Optional

from src.abstract_json_saver import AbstractJSONSaver


class JSONWorker(AbstractJSONSaver):
    """Класс для работы с json-файлом"""

    def __init__(self, filename: str = "..data/vacancies.json") -> None:
        self.__filename = filename

    def __load(self) -> List[Dict]:
        """Загружаем данные из JSON-файла"""
        if os.path.exists(self.__filename):
            with open(self.__filename, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def __save(self, data: List[Dict]) -> None:
        with open(self.__filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy: Dict) -> None:
        data = self.__load()
        if not any(v["id"] == vacancy["id"] for v in data):  # Нет дубликатов по ID
            data.append(vacancy)
        self.__save(data)

    def get_vacancies(self, criteria: Optional[Dict[str, Any]] = None) -> List[Dict]:
        data = self.__load()
        if criteria:
            return [v for v in data if all(v.get(k) == criteria[k] for k in criteria)]
        return data

    def delete_vacancy(self, vacancy: Dict) -> None:
        data = self.__load()
        data = [v for v in data if v["id"] != vacancy["id"]]
        self.__save(data)

    #     # Заглушки для других
    # def add_to_csv(self, vacancy: Dict) -> None:
    #     raise NotImplementedError("CSV not implemented")
