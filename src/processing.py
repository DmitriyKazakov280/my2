def filter_by_state(list_of_dicts: list, state_for_key: str = "EXECUTED") -> list:
    """Функция которая, принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только
     те словари, у которых ключ state соответствует указанному значению."""
    new_list = []
    for state in list_of_dicts:
        if state.get("state") == state_for_key:
            new_list.append(state)
    return new_list


def sort_by_date(list_of_dicts: list, ascending: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр,
     задающий порядок сортировки (по умолчанию — убыванию).
     Функция должна возвращать новый список, отсортированный по дате (date)."""
    new_list = sorted(list_of_dicts, key=lambda date: date.get("date", ''), reverse=ascending)
    return new_list
