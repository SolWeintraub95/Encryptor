class EncryptorBase:
    def __init__(self, shift: int):
        self.shift: int = shift


class Encryptor(EncryptorBase):
    def __init__(self):
        self.alphabet: str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        self.alphabet_dict: dict = {letter: index for index, letter in enumerate(self.alphabet)}

    def shift_text(self, text: str) -> str:
        result: list = []
        letters_quantity: int = len(self.alphabet)
        for char in text:
            low_char = char.lower()
            if self.alphabet_dict.get(low_char):
                new_index: int = (self.alphabet_dict[low_char] + self.shift) % letters_quantity
                new_char = self.alphabet[new_index].upper() if char.isupper() else self.alphabet[new_index]
                result.append(new_char)
            else:
                result.append(char)
        return ''.join(result)


if __name__ == '__main__':
    change = int(input('Введите число на которое будут смещаться буквы: '))
    shifter = Encryptor(change)  # сдвиг на указанное количество букв
    print(shifter.shift_text('К сожалению, Вы не прошли техническое интервью.\nУвидимся через полгода.'))
