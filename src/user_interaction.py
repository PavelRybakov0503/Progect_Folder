from src.hh_api import HeadHunterAPI
from src.parser import sort_vacancy, get_vacancy
from src.json_worker import JSONSaver


# Функция для взаимодействия с пользователем
def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    try:
        page = int(input("Введите количество страниц, не больше 20: "))
    except ValueError:
        print('количество страниц должно быть числовым значением')
        return ValueError
    try:
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    except ValueError:
        print('количество вакансий должно быть числовым значением')
        return ValueError

    filter_words = input("Введите ключевое слово для фильтрации вакансий: ")
    try:
        salary_range = input("Введите диапазон зарплат, через пробел # Пример: 100000 150000: ").split()
        if len(salary_range) < 2 or len(salary_range) >= 3:
            raise ValueError
    except ValueError:
        print('Ожидается два значения')
        return ValueError

    hh_api = HeadHunterAPI()
    # requests запрос
    vacancies = hh_api.get_vacancies(search_query, page)
    # Преобразование набора данных из JSON в список объектов
    vacancies_list = hh_api.from_vacancy(vacancies)
    # инициализация объекта JSONSaver класса
    json_saver = JSONSaver()
    json_saver.del_vacancy()
    # добавление вакансий в JSON-файл
    json_saver.add_vacancy(vacancies_list)
    # чтение JSON-файл
    reed_vacancy = json_saver.reed_vacancy()
    # Фильтрация по критериям пользователя
    top_vacancy = sort_vacancy(salary_range, filter_words, reed_vacancy)

    if len(top_vacancy) < top_n:
        for element in range(len(top_vacancy)):
            print()
            print(get_vacancy(top_vacancy, element))
        print(f'по донному запросу найдено: {len(top_vacancy)} вакансий')
    else:
        for element in range(top_n):
            print()
            print(get_vacancy(top_vacancy, element))
