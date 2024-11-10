class Vacancy:
    """
    Класс для создания вакансии
    """
    def __init__(self, name_vacancies: str, link: str, salary: dict, description: str):
        self.__name_vacancies = name_vacancies
        self.__link = link
        self.__description = self.__validate_description(description)
        self.__salary_from = self.__salary_from(salary)
        self.__salary_to = self.__salary_to(salary)

    @staticmethod
    def __validate_description(description):
        return description if bool(description) is True else 'Описания нет'

    @staticmethod
    def __salary_from(salary) -> int:
        try:
            salary_from = salary.get('from')
        except Exception:
            return 0
        else:
            return salary_from or 0

    @staticmethod
    def __salary_to(salary) -> int:
        try:
            salary_to = salary.get('to')
        except Exception:
            return 0
        else:
            return salary_to or 0

    def __lt__(self, other):
        return self.__salary_from < other.__salary_from

    def __str__(self):
        return (f"Вакансия: {self.__name_vacancies}\n"
                f"ссылка на вакансию: {self.__link}\n"
                f"описание вакансии: {self.__description}\n"
                f"зарплата от: {self.__salary_from}\n"
                f"зарплата до: {self.__salary_to}")

    # Функция сохранения вакансии в словарь
    def cast_to_object_list(self):
        dict_vacancy = {"name": self.__name_vacancies,
                        "url": self.__link,
                        "salary_from": self.__salary_from,
                        "salary_to": self.__salary_to,
                        "description": self.__description}

        return dict_vacancy
