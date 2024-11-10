import json
from typing import Any, List
from abc import ABC, abstractmethod
from src.hh_api import Vacancy
import os


class AbstractJson(ABC):
    @abstractmethod
    def add_vacancy(self, vacancies: List[Vacancy]) -> None:
        pass

    @abstractmethod
    def reed_vacancy(self) -> List[dict]:
        pass

    @abstractmethod
    def del_vacancy(self) -> None:
        pass


class JSONSaver(AbstractJson):
    """
     Класс для сохранения вакансий в JSON-файл и получения вакансий из JSON-файл
    """

    def __init__(self, file_name='data/vacancies.json') -> None:
        """Инициализация пути к файлу.

                Args:
                    file_name (str): Путь к JSON-файлу.
                """
        self.__path = os.path.abspath(file_name)


    def add_vacancy(self, vacancies: list[Vacancy]) -> None:
        """
         Функция для сохранения, вакансий в JSON-файл
        """
        with open(self.__path, 'r', encoding='utf-8') as file:
            try:
                data: list[dict[str, Any]] = json.load(file)
            except json.JSONDecodeError:
                data = []

                # добавление вакансии в список
                for vacancy in vacancies:
                    data.append(vacancy.cast_to_object_list())

        # добавление список вакансий в JSON-файл
        with open(self.__path, 'w', encoding='utf-8') as file:
            return json.dump(data, file, indent=4, ensure_ascii=False)


    def reed_vacancy(self) -> List[dict]:
        """ Функция для получения вакансий по критериям пользователя, из JSON файла"""
        with open(self.__path, 'r', encoding='utf-8') as file:
            vacancy_list = json.load(file)
        return vacancy_list


    def del_vacancy(self) -> None:
        """Функция для удаления вакансии"""
        with open(self.__path, 'w', encoding='utf-8') as file:
            pass
