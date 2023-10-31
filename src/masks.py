# программа запрашивает у пользователя номер карты
# программа разбивает номер на 4 блока по 4 цифры, разделенные пробелом
# программа маскирует номер карты - видны первые 6 и последние 4 цифры
# программа выдает номер карты в замаскированном виде



def card_number_mask(card_number: str) -> str:
    """Программа маскирует номер карты - видны первые 6 и последние 4 цифры"""
    mask_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
    chang = 4
    return " ".join([mask_number[num: num + chang] for num in range(0, len(mask_number), chang)])


def invoice_number_mask(invoice_number: str) -> str:
    """Функция принимает на вход номер счёта и возвращает его маску. Номер счёта замаскирован и отображается в формате

    **XXXX. т. е. видны только последние 4 цифры."""
    mask_account = (len(invoice_number[:-4]) * "*") + invoice_number[-4:]
    chang = mask_account[-6:]
    return chang


print(card_number_mask("1456123654788912"))
print(invoice_number_mask("123145647894123651256"))
