#  module_7_2.py Позиционирование в файле.
# =============================================
def custom_write(file_name, strings): # file_name - название файла для записи,
                                         # strings - список строк для записи.
    strings_positions  ={}          # возвращаемый словарь
    file = open(file_name, 'w', encoding='utf-8')  # открываем для записи
    current_str = 1                                # текущая строка
    for i in strings:
        current_tell = file.tell()
        file.write(f'{i}\n')
        strings_positions.update({(current_str,current_tell) : i})
        current_str += 1
    file.close()
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)