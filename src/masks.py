def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты, заменяя цифры на '*'"""
    if card_number.isdigit() == True and len(card_number) == 16:
        return card_number[:-12] + " " + card_number[-12:-10] + "** **** " + card_number[-4:]
    else:
        return "Не верный номер!"


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер счета, заменяя цифры на '*'"""
    if account_number.isdigit() == True and len(account_number) == 20:
        return "**" + account_number[-4:]
    else:
        return "Не верный номер!"
