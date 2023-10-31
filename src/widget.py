from masks import card_number_mask, invoice_number_mask


def type_of_cards(type_and_number: str | list[str], account_and_number) -> str:
    """Принимает на вход строку информацией тип карты/счета и номер карты/счета.
       Возвращает эту строку с замаскированным номером карты/счета"""
    split_list = type_and_number.split()
    split_account = account_and_number.split()
    only_account = invoice_number_mask(split_account[-1])
    only_number_account = split_account[:-1]
    join_oneline = ''.join(only_number_account)
    if len(split_list) == 3:
        only_number = card_number_mask(split_list[-1])
        only_type = split_list[:2]
        join_only_type = ' '.join(only_type)
        return f'{join_only_type} {only_number} \n{join_oneline} {only_account}'
    elif len(split_list) == 2:
        only_number = card_number_mask(split_list[-1])
        only_type = split_list[:1]
        join_only_type = ' '.join(only_type)
        return f'{join_only_type} {only_number} \n{join_oneline} {only_account}'
    else:
        return "Не знаю такой номер карты, счета"


print(type_of_cards(type_and_number='Maestro 1596837868705199', account_and_number='Счет 64686473678894779589'))

