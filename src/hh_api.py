from abc import ABC, abstractmethod
import requests
from src.vacancy import Vacancy
from typing import List, Dict, Union


class AbstractParser(ABC):
    @abstractmethod
    def get_vacancies(self, *args: Union[str, int]) -> List[Dict]:
        pass


class HeadHunterAPI(AbstractParser):
    """Класс для работы с API HeadHunter"""

    def init(self) -> None:
        """Инициализация параметров API."""
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}

    def get_vacancies(self, keyword: str, page: int) -> List[Dict]:
        """Функция для requests запроса.

        Args:
            keyword (str): Ключевое слово для поиска вакансий.
            page (int): Номер страницы для запроса.

        Returns:
            List[Dict]: Список вакансий, полученный от API.

        Raises:
            RequestException: Исключение при ошибке запроса.
            KeyError: Исключение, если ожидаемые ключи отсутствуют в ответе.
        """
        self.params['text'] = keyword
        self.params['page'] = page

        try:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            response.raise_for_status()  # Проверка на статус ошибки
            vacancies = response.json()['items']
            return vacancies
        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса: {e}")
            return []
        except KeyError as e:
            print(f"Отсутствует ожидаемый ключ в ответе: {e}")
            return []

    @staticmethod
    def from_vacancy(vacancies: List[Dict]) -> List[Vacancy]:
        """Функция для создания списка объектов вакансий.

        Args:
            vacancies (List[Dict]): Список словарей с данными вакансий.

        Returns:
            List[Vacancy]: Список объектов вакансий.
        """
        list_vacancy = []
        for vacancy in vacancies:
            name = vacancy['name']
            link = vacancy['alternate_url']
            salary = vacancy.get('salary')
            description = vacancy['snippet']['responsibility'] if 'snippet' in vacancy and 'responsibility' in vacancy[
                'snippet'] else None

            list_vacancy.append(Vacancy(name_vacancies=name, link=link, salary=salary, description=description))

        return list_vacancy
