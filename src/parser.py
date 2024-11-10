from typing import List, Dict, Any, Optional

def sort_vacancy(salary_range: List[str], filter_words: Optional[str], vacancy_list: List[Dict[str, Any]])\
        -> List[Dict[str, Any]]:
    """Функция для получения вакансий по критериям пользователя с сортировкой по зарплате.

    Args:
        salary_range (List[str]): Диапазон зарплат, заданный пользователем.
        filter_words (Optional[str]): Слова для фильтрации вакансий по названию. Если None, то фильтрация не
         применяется.
        vacancy_list (List[Dict[str, Any]]): Список вакансий для сортировки и фильтрации.

    Returns:
        List[Dict[str, Any]]: Отфильтрованный и отсортированный список вакансий.
    """
    sort_vacancies = sorted(vacancy_list, key=lambda x: x['salary_from'], reverse=True)
    """ Фильтрация по критериям пользователя"""
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


def get_vacancy(sort_vacancy: List[Dict[str, Any]], element: int) -> str:
    """ Функция для получения вакансий по ключам"""
    name = sort_vacancy[element]['name']
    url = sort_vacancy[element]['url']
    salary_from = sort_vacancy[element]['salary_from']
    salary_to = sort_vacancy[element]['salary_to']
    description = sort_vacancy[element]['description']

    return f'{name}\n{url}\n{salary_from}\n{salary_to}\n{description}'
