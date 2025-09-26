class Encryptor:
    def __init__(self, shift):
        self.shift = shift
        self.alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        self.alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    def shift_text(self, text):
        result = ""
        for char in text:
            if char == '\n':  # Переход на новую строку
                result += char
            elif char in self.alphabet_lower:  # Строчные буквы
                index = self.alphabet_lower.index(char)
                result += self.alphabet_lower[(index + self.shift) % len(self.alphabet_lower)]
            elif char in self.alphabet_upper:  # Заглавные буквы
                index = self.alphabet_upper.index(char)
                result += self.alphabet_upper[(index + self.shift) % len(self.alphabet_upper)]
            else:  # Остальные символы
                result += char
        return result
# Пример использования
input_text = """
 Ётёд, худхмет циеи лд цйупяи хптёд, очыч бртъмн м цдоти лдутрмсдвэиихг утлзфдёписми!

 \nМфд, умхарт лдьмшфтёдст ьмшфтр Ъилдфг сд рмсчх ыицяфи.
 """
change = int(input('Введите число на которое будут смещаться буквы:'))
shifter = Encryptor(change)  # сдвиг на указанное количество букв
print(shifter.shift_text(input_text))