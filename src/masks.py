def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты, заменяя цифры на '*'"""
    card_number_mask = card_number[:-12] + " " + card_number[-12:-10] + "** **** " + card_number[-4:]
    return card_number_mask


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер счета, заменяя цифры на '*'"""
    account_number_mask = "**" + account_number[-4:]
    return account_number_mask
