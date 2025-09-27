class Encryptor:
    def __init__(self, shift):
        self.alphabet: str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        self.alphabet_dict: dict = {letter: index for index, letter in enumerate(self.alphabet)}
        self.shift = shift

    def shift_text(self, input_text: str) -> str:
        result: list = []
        letters_quantity: int = len(self.alphabet)
        for char in input_text:
            low_char = char.lower()
            if low_char in self.alphabet_dict:  # ✅ проверка по ключу
                new_index: int = (self.alphabet_dict[low_char] + self.shift) % letters_quantity
                new_char = self.alphabet[new_index].upper() if char.isupper() else self.alphabet[new_index]
                result.append(new_char)
            else:
                result.append(char)
        return ''.join(result)
input_text = """

"""

if __name__ == '__main__':
    shift = int(input('Введите число на которое будут смещаться буквы: '))
    input_type = int(input('Ввести текст или взять из текстового документа (1,2): '))
    shifter = Encryptor(shift)
    if input_type == 1:
        input_text = str(input('Введите текст: '))
        print(shifter.shift_text(input_text))
    else:
        file=open('user_input.txt', 'r', encoding='utf-8')
        input_text = file.read()
        print(shifter.shift_text(input_text))