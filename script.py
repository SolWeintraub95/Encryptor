# This is a sample Python script.
#
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def shift_letters(text):
#     result = []
#     change = int(input('Введите число на которое будут смещаться буквы:'))
#     for char in text:
#         if char == '\n':  # Если символ — это переход на новую строку
#             result += char
#         elif 'а' <= char <= 'я':  # Для маленьких букв
#             # Смещаем букву на 1, если она последняя (я), возвращаем на 'а'
#             new_char = chr(((ord(char) - ord('а') + change) % 32) + ord('а'))
#             result.append(new_char)
#         elif 'А' <= char <= 'Я':  # Для заглавных букв
#             # Смещаем букву на 1, если она последняя (Я), возвращаем на 'А'
#             new_char = chr(((ord(char) - ord('А') + change) % 32) + ord('А'))
#             result.append(new_char)
#         else:
#             result.append(char)  # Если символ не буква, оставляем его без изменений
#
#     return ''.join(result)
#
#
# # Пример использования:
# input_text = input("Введите текст: ")
# output_text = shift_letters(input_text)
# print("Изменённый текст:", output_text)


# my_file = open("cypher1.txt", "w+")
# my_file.write() = user_input
# my_file.close()
# print (my_file.write("cypher1.txt"))


# def shift_text_russian(text, shift):
#     result = ""
#     for char in text:
#         if char == '\n':  # Если символ — это переход на новую строку
#             result += char  # Просто добавляем его в результат
#         elif 'А' <= char <= 'Я' or 'а' <= char <= 'я':  # Если символ русская буква
#             if char.isupper():  # Для заглавных букв
#                 base = ord('А')
#                 result += chr((ord(char) - base + shift) % 33 + base)
#             else:  # Для строчных букв
#                 base = ord('а')
#                 result += chr((ord(char) - base + shift) % 33 + base)
#         else:  # Остальные символы оставляем без изменений
#             result += char
#     return result
#
# # Пример использования
# input_text = """Привет. Вы замечали, что поздравление - это часто просто тёплые слова, которые ценятся тем больше, чем меньше их говорят между поздравлениями?
# \nНа самом деле мне кажется я не умею поздравлять, потому что поздравление - это что-то ёмкое и содержательное, и притом немногословное. А у меня это обычно просто тёплые слова, которые я стараюсь извлечь из себя так же, как писатель обычно пишет книгу.
# \nВ любом случае пора уже к ним переходить. У меня кончились идеи как растянуть этот момент, когда к ним пеереходить не надо.
# \nТак вот к чему я это всё.
# \nС вами у нас получилось создать тёплую ячейку (общества, хыхыхы), в которой тёплые слова - это не редкость. И я действительно рад этому и удивляюсь тому, как так вышло. Возможно я прилагаю к этому усилия, которых не замечаю сам. Возможно у вас так же.
# \nЯ вас обеих очень сердечно люблю и желаю вам в новом году испытаний по силам, побед, заслуженного отдыха и любящих, а также понимающих людей рядом.
# \nОчень рад, что мы в итоге сблизились и рад называть себя вашим другом.
# \nС наступающим или наступившим (не знаю когда вы это расшифруете) новым годом.
# \nЛюблю вас очень очень сильно."""
# shift_value = 4
# print(shift_text_russian(input_text, shift_value))