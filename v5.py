class Encryptor:
    def __init__(self, shift):
        self.alphabet: str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        self.alphabet_dict: dict = {letter: index for index, letter in enumerate(self.alphabet)}
        self.shift = shift

    def shift_text(self, text: str) -> str:
        result: list = []
        letters_quantity: int = len(self.alphabet)
        for char in text:
            low_char = char.lower()
            if low_char in self.alphabet_dict:  # ✅ проверка по ключу
                new_index: int = (self.alphabet_dict[low_char] + self.shift) % letters_quantity
                new_char = self.alphabet[new_index].upper() if char.isupper() else self.alphabet[new_index]
                result.append(new_char)
            else:
                result.append(char)
        return ''.join(result)


if __name__ == '__main__':
    change = int(input('Введите число на которое будут смещаться буквы: '))
    text = str(input('Введите текст: '))
    shifter = Encryptor(change)
    print(shifter.shift_text(text))