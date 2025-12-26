import abc
import random


class Encryptor(abc.ABC):
    alphabet_dict: dict[str, str]

    def encrypt(self, text: str) -> str:
        result: list[str] = []
        for c in text:
            char = c.lower()
            if char in self.alphabet_dict:
                res = self.alphabet_dict[char]
                if c.isupper():
                    res = res.upper()
                result.append(res)
            else:
                result.append(char)
        return "".join(result)


class ShiftEncryptor(Encryptor):
    def __init__(self, shift: int):
        self.alphabet_dict: dict = {}

        alphabet: str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

        for i, char in enumerate(alphabet):
            self.alphabet_dict[char] = alphabet[(i + shift) % len(alphabet)]


class RandomMappingEncryptor(Encryptor):
    def __init__(self):
        self.alphabet_dict: dict[str, str] = {}

        alphabet: str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        alphabet_set: set[str] = set(alphabet)

        for char in alphabet:
            c = random.choice(list(alphabet_set))
            alphabet_set.discard(c)
            self.alphabet_dict[char] = c


def encrypt_file(encryptor: Encryptor, path: str):
    with open(path, "r") as f:
        with open(f"{path}_encrypted", "w") as d:
            d.write(encryptor.encrypt(f.read()))


if __name__ == "__main__":
    print("Выберите тип энкриптора:")
    print("1. Shift")
    print("2. RandomMapping")
    raw_input = input("Номер энкриптора > ")
    try:
        encrypt_type = int(raw_input)
        if encrypt_type not in (1, 2):
            raise ValueError
    except ValueError:
        print(f"Иди нахуй, ну единичка или двоечка, какой ещё {raw_input}")
        exit(1)

    if encrypt_type == 1:
        shift = int(input("Введите число на которое будут смещаться буквы: "))
        e = ShiftEncryptor(shift)
    else:
        e = RandomMappingEncryptor()

    print("Выберите тип ввода-вывода:")
    print("1. STDIO")
    print("2. Из файла")
    input_type = int(input("Тип ввода-вывода > "))
    if input_type == 1:
        input_text = str(input("Введите текст: "))
        print(e.encrypt(input_text))
    else:
        encrypt_file(e, "user_input.txt")
