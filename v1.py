def shift_letters(text):
    result = []
    change = int(input('Введите число на которое будут смещаться буквы:'))
    for char in text:
        if char == '\n':  # Если символ — это переход на новую строку
            result += char
        elif 'а' <= char <= 'я':  # Для маленьких букв
            # Смещаем букву на 1, если она последняя (я), возвращаем на 'а'
            new_char = chr(((ord(char) - ord('а') + change) % 32) + ord('а'))
            result.append(new_char)
        elif 'А' <= char <= 'Я':  # Для заглавных букв
            # Смещаем букву на 1, если она последняя (Я), возвращаем на 'А'
            new_char = chr(((ord(char) - ord('А') + change) % 32) + ord('А'))
            result.append(new_char)
        else:
            result.append(char)  # Если символ не буква, оставляем его без изменений

    return ''.join(result)


# Пример использования:
input_text = input("Введите текст: ")
output_text = shift_letters(input_text)
print("Изменённый текст:", output_text)