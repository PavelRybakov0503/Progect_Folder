class Vacancy:
    """
    Класс для создания вакансии
    """

    __slots__ = ['name_vacancies', '_link', '_description', '_salary_from', '_salary_to']

    def __init__(self, name_vacancies: str, link: str, salary: dict, description: str) -> None:
        """Инициализация объекта вакансии.

                Args:
                    name_vacancies (str): Название вакансии.
                    link (str): Ссылка на вакансию.
                    salary (dict): Словарь, содержащий информацию о зарплате ('from', 'to').
                    description (str): Описание вакансии.
                """
        self.name_vacancies = name_vacancies
        self._link = link
        self._description = self.__validate_description(description)
        self._salary_from = self.__salary_from(salary)
        self._salary_to = self.__salary_to(salary)

    @staticmethod
    def __validate_description(description) -> str:
        """Валидация описания вакансии.

                Если описание пустое, возвращает 'Описания нет', иначе возвращает
                переданное описание.

                Args:
                    description (str): Описание вакансии.

                Returns:
                    str: Валидационное описание вакансии.
                """
        return description if bool(description) is True else 'Описания нет'

    @staticmethod
    def __salary_from(salary: dict) -> int:
        """Получение минимальной зарплаты из словаря salary.

                Args:
                    salary (dict): Словарь с данными о зарплате.

                Returns:
                    int: Минимальная зарплата или 0, если она не указана.
                """
        try:
            salary_from = salary.get('from')
        except Exception:
            return 0
        else:
            return salary_from or 0

    @staticmethod
    def __salary_to(salary) -> int:
        """Получение максимальной зарплаты из словаря salary.

               Args:
                   salary (dict): Словарь с данными о зарплате.

               Returns:
                   int: Максимальная зарплата или 0, если она не указана.
               """
        try:
            salary_to = salary.get('to')
        except Exception:
            return 0
        else:
            return salary_to or 0

    def __lt__(self, other: 'Vacancy') -> bool:
        """Сравнение объектов вакансий по минимальной зарплате.

                Args:
                    other (Vacancy): Другая вакансия для сравнения.

                Returns:
                    bool: True, если минимальная зарплата текущей вакансии меньше,
                          чем у другой вакансии, иначе False.
                """
        return self.__salary_from < other.__salary_from

    def __str__(self) -> str:
        """Строковое представление объекта вакансии.

                Returns:
                    str: Информация о вакансии в читаемом формате.
                """
        return (f"Вакансия: {self.name_vacancies}\n"
                f"ссылка на вакансию: {self._link}\n"
                f"описание вакансии: {self._description}\n"
                f"зарплата от: {self._salary_from}\n"
                f"зарплата до: {self._salary_to}")


    def cast_to_object_list(self) -> dict:
        """Функция сохранения вакансии в словарь"""
        dict_vacancy = {"name": self.name_vacancies,
                        "url": self._link,
                        "salary_from": self._salary_from,
                        "salary_to": self._salary_to,
                        "description": self._description}

        return dict_vacancy
