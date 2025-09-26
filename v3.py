def shift_text_russian(text, shift):
    result = ""
    alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"  # Все строчные буквы
    alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"  # Все заглавные буквы

    for char in text:
        if char == '\n':  # Переход на новую строку
            result += char
        elif char in alphabet_lower:  # Для строчных букв
            index = alphabet_lower.index(char)
            result += alphabet_lower[(index + shift) % len(alphabet_lower)]
        elif char in alphabet_upper:  # Для заглавных букв
            index = alphabet_upper.index(char)
            result += alphabet_upper[(index + shift) % len(alphabet_upper)]
        else:  # Остальные символы оставляем без изменений
            result += char
    return result

# Пример использования
input_text = """
#Ётёд, худхмет циеи лд цйупяи хптёд, очыч бртъмн м цдоти лдутрмсдвэиихг утлзфдёписми!

#\nМфд, умхарт лдьмшфтёдст ьмшфтр Ъилдфг сд рмсчх ыицяфи.

"""

change = int(input('Введите число на которое будут смещаться буквы:'))
shift_value = change
print(shift_text_russian(input_text, shift_value))
