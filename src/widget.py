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

    name_s_card = " ".join(name_card)
    number_s_card = "".join(number_card)

    if len(number_s_card) == 16:
        # number_card_mask = number_s_card[:-12] + " " + number_s_card[-12:-10] + "** ****" + number_s_card[-4:]
        card_details_new = get_mask_card_number(number_s_card)
        result = f"{name_s_card} {card_details_new}"
        # return name_numder
    else:
        # number_score_mask = "**" + number_s_card[-4:]
        new_number = get_mask_account(number_s_card)
        result = f"{name_s_card} {new_number}"
    return result


def get_date(date_operation: str) -> str:
    """ Функция которая принимает на вход строку с датой в
    формате "2024-03-11T02:26:18.671407" и
    возвращает строку с датой в формате "ДД.ММ.ГГГГ" """

    date_new = date_operation[8:10] + "." + date_operation[5:7] + "." + date_operation[:4]
    return date_new
