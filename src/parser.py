def sort_vacancy(salary_range: list[str], filter_words: str | None, vacancy_list: list):
    # Функция для получения вакансий по критериям пользователя
    # сортировка по зарплате
    sort_vacancies = sorted(vacancy_list, key=lambda x: x['salary_from'], reverse=True)

    # Фильтрация по критериям пользователя
    top_vacancies = []
    for vacancy in sort_vacancies:

        list_salary_range = salary_range
        if filter_words not in vacancy['name'] and filter_words is not None:
            continue
        else:
            if vacancy['salary_from'] < int(list_salary_range[0]):
                continue
            if vacancy['salary_to'] > int(list_salary_range[-1]):
                continue
        top_vacancies.append(vacancy)
    return top_vacancies


# Функция для получения вакансий по ключам
def get_vacancy(sort_vacancy: list, element: int):
    name = sort_vacancy[element]['name']
    url = sort_vacancy[element]['url']
    salary_from = sort_vacancy[element]['salary_from']
    salary_to = sort_vacancy[element]['salary_to']
    description = sort_vacancy[element]['description']

    return f'{name}\n{url}\n{salary_from}\n{salary_to}\n{description}'
