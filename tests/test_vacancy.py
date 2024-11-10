import pytest

from src.vacancy import Vacancy


@pytest.fixture()
def vacancy():
    """Фикстура, создающая объект Vacancy для тестирования.

        Returns:
            Vacancy: Экземпляр класса Vacancy, инициализированный с примерными данными.
        """
    return Vacancy("Frontend developer",
                   "https://hh.ru/vacancy/101939534", {
                       "from": 5000000,
                       "to": 15000000,
                       "currency": "UZS",
                       "gross": True
                   },
                   "Design, develop, and maintain user interfaces for Odoo applications using JavaScript,"
                   " OWL (Odoo Web Library), and Vue.js. Ensure the technical...")


def test_cast_to_object_list(vacancy):
    """Тест метода cast_to_object_list класса Vacancy.

        В этом тесте проверяется, может ли объект вакансии быть правильно преобразован
        в словарный формат, содержащий необходимые данные о вакансии.

        Args:
            vacancy (Vacancy): Объект Vacancy.

        Asserts:
            Dict: Ожидаемое словарное представление объекта вакансии.
        """
    assert Vacancy.cast_to_object_list(vacancy) == {
        "name": "Frontend developer",
        "url": "https://hh.ru/vacancy/101939534",
        "salary_from": 5000000,
        "salary_to": 15000000,
        "description": "Design, develop, and maintain user interfaces for Odoo applications using JavaScript, OWL"
        " (Odoo Web Library), and Vue.js. Ensure the technical..."
    }


def test_str(vacancy):
    """Тест строкового представления класса Vacancy.

        В этом тесте проверяется, правильно ли отформатировано строковое представление
        объекта вакансии согласно ожидаемому выводу.

        Args:
            vacancy (Vacancy): Объект Vacancy.

        Asserts:
            str: Ожидаемый строковый формат объекта вакансии.
        """
    assert Vacancy.__str__(vacancy) == (
        f"Вакансия: Frontend developer\n"
        f"ссылка на вакансию: https://hh.ru/vacancy/101939534\n"
        f"описание вакансии: Design, develop, and maintain user interfaces for Odoo"
        f" applications using JavaScript, OWL (Odoo Web Library), and Vue.js. Ensure"
        f" the technical...\n"
        f"зарплата от: 5000000\n"
        f"зарплата до: 15000000")
