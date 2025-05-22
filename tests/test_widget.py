import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("number_tests, card_number_masks",
                        [("МИР 7000792289606361", "МИР 7000 79** **** 6361"),
                         ("Счет 70007922896063610000", "Счет **0000"),
                         ("", "Не верный номер!"),
                         ("7000792289606361", "Не верный номер!"),
                         ("a7000792289606361", "Не верный номер!"),
                         ("Счет 73654108430135874305", "Счет **4305"),
                         ("Счет", "Не верный номер!"),
                          ])
def test_mask_account_card(number_tests: str, card_number_masks: str) -> str:
    assert mask_account_card(number_tests) == card_number_masks


@pytest.mark.parametrize("date_operation_tests, answer_data",
                         [("2024-03-11T02:26:18.671407", "11.03.2024"),
                          ("", "Неверный формат"),
                          ("2024-03-1", "Неверный формат"),
                          ("2024-03 11T02:26:18.671407", "Неверный формат"),
                        ])
def test_get_date(date_operation_tests: str, answer_data: str) -> str:
    assert get_date(date_operation_tests) == answer_data