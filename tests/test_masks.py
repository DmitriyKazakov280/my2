import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("number_test, card_number_mask",
                         [("7000792289606361", "7000 79** **** 6361"),
                          ("87000792289606361", "Не верный номер!"),
                          ("87000289606361", "Не верный номер!"),
                          ("870007 2289606361", "Не верный номер!"),
                          ("", "Не верный номер!")
                         ])
def test_get_mask_card_number(number_test: str, card_number_mask: str) -> str:
    assert get_mask_card_number(number_test) == card_number_mask


def test_get_mask_account(account_number_masks):
    assert get_mask_account('73654108430135874305') == account_number_masks
    assert get_mask_account('3654108430135874305') != account_number_masks
    assert get_mask_account('a654108430135874305') != account_number_masks
    assert get_mask_account('9993654108430135874305') != account_number_masks
    assert get_mask_account('36541084 30135874305') != account_number_masks
