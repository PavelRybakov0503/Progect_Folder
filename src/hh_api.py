from abc import ABC, abstractmethod
import requests
from src.vacancy import Vacancy


class AbstractParser(ABC):
    @abstractmethod
    def get_vacancies(self, *args):
        pass


class HeadHunterAPI(AbstractParser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}

    # Функция для requests запроса
    def get_vacancies(self, keyword: str, page: int) -> list[dict]:
        self.params['text'] = keyword
        self.params['page'] = page
        response = requests.get(self.url, headers=self.headers, params=self.params)
        vacancies = response.json()['items']
        return vacancies

    # функция для создания списка объектов вакансий
    @staticmethod
    def from_vacancy(vacancies: list):
        list_vacancy = []
        for vacancy in vacancies:
            list_vacancy.append(Vacancy(name_vacancies=vacancy.get('name'), link=vacancy.get('alternate_url'),
                                        salary=vacancy.get('salary'),
                                        description=vacancy.get('snippet').get("responsibility")))
        return list_vacancy
