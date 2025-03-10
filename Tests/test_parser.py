import pytest
from src.parser import get_vacancy, sort_vacancy


@pytest.fixture
def list_vacancy():
    return [
        {
            "name": "Водитель-экспедитор",
            "url": "https://hh.ru/vacancy/101840292",
            "salary_from": 110000,
            "salary_to": 0,
            "description": "Развоз продукции по Клиентским точкам в Москве и МО. Соблюдение стандартов и правил"
            " компании."
            " Ведение документооборота, заполнение накладных, путевых и..."
        },
        {
            "name": "Водитель На Рено Логан",
            "url": "https://hh.ru/vacancy/102569427",
            "salary_from": 75000,
            "salary_to": 115000,
            "description": "Развоз сотрудников охраны по постам и объектам. Соблюдение правил дорожного движения."
            " Следить за чистотой автомобиля, техническим состоянием."
        }
    ]


def test_sort_vacancy(list_vacancy):
    assert sort_vacancy(['10', '100000'], 'Водитель', list_vacancy) == [
        {
            "name": "Водитель-экспедитор",
            "url": "https://hh.ru/vacancy/101840292",
            "salary_from": 110000,
            "salary_to": 0,
            "description": "Развоз продукции по Клиентским точкам в Москве и МО. Соблюдение стандартов и правил"
            " компании."
            " Ведение документооборота, заполнение накладных, путевых и..."
        }
    ]


def test_reed_vacancy():
    assert get_vacancy([
        {'name': 'Разработчик AI-решений (python + no-code платформы)', 'url': 'https://hh.ru/vacancy/99862545',
         'salary_from': 120000, 'salary_to': 200000,
         'description': 'Кроме того, мы разрабатываем высокоэффективных AI-агентов, которые берут на себя ряд рутинных'
         ' задач, таких как обработка данных, составление отчетов...'},
        {'name': 'Младший python-разработчик', 'url': 'https://hh.ru/vacancy/99725937', 'salary_from': 85000,
         'salary_to': 100000,
         'description': 'Разработка внутренних серверных приложений на <highlighttext>Python</highlighttext> для'
         ' автоматизации бизнес-процессов. Организация взаимообмена данными между собственными и сторонними сервисами'
         ' через API. '},
        {'name': 'Junior python-программист в техподдержку (FastAPI)', 'url': 'https://hh.ru/vacancy/102012417',
         'salary_from': 0, 'salary_to': 0,
         'description': 'Доработка интеграций по документации партнера. Улучшение действующих микросервисов.'
         ' Поддержка действующего функционала. Работа с агрегированными запросами SQL/NoSQL. Работа с настройками...'}]
        , 0) == ('Разработчик AI-решений (python + no-code платформы)\n'
                 'https://hh.ru/vacancy/99862545\n'
                 '120000\n'
                 '200000\n'
                 'Кроме того, мы разрабатываем высокоэффективных AI-агентов, которые берут на себя ряд рутинных задач,'
                 ' таких как обработка данных, составление отчетов...')
