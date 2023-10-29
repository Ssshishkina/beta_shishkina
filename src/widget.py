from masks import card_number_mask, invoice_number_mask


def type_of_cards(type_and_number): str | list[str], account_and_number) -> str:
    """Принимает на вход строку информацией тип карты/счета и номер карты/счета.
    Возвращает эту строку с замаскированным номером карты/счета"""
    split_list = type_and_number.split()
    split_account = account_and_number.split()

