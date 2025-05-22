from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Функция маскирует номер карты и счета, заменяя цифры на '*'"""

    name_card = []
    number_card = []
    for i in card_number.split():
        if i.isalpha() == True:
            name_card.append(i)
        else:
            number_card.append(i)

    name_s_card = "".join(name_card)
    number_s_card = "".join(number_card)

    if len(number_s_card) == 16 and len(name_s_card) >= 3:
        card_details_new = get_mask_card_number(number_s_card)
        return f"{name_s_card} {card_details_new}"
    elif len(number_s_card) == 20 and len(name_s_card) >= 3:
        new_number = get_mask_account(number_s_card)
        return f"{name_s_card} {new_number}"
    else:
        return "Не верный номер!"


def get_date(date_operation: str) -> str:
    """ Функция которая, принимает на вход строку с датой в
    формате "2024-03-11T02:26:18.671407" и
    возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    new_data = date_operation[:10]

    new_data_s = []

    for i in new_data.split("-"):
        if i.isdigit() == True and len(new_data) == 10:
            new_data_s.append(i)
        else:
            return "Неверный формат"

    if len(new_data_s) == 3:
        return ".".join(reversed(new_data_s))
    else:
        return "Неверный формат"
