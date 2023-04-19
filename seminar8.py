# Задание 1. 
# Задание на закрепление знаний по модулю CSV. Написать скрипт,
# осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
# info_3.txt и формирующий новый «отчетный» файл в формате CSV.

# Для этого:

# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
# с данными, их открытие и считывание данных. В этой функции из считанных данных
# необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения каждого параметра поместить в соответствующий список. Должно
# получиться четыре списка — например, os_prod_list, os_name_list,
# os_code_list, os_type_list. В этой же функции создать главный список
# для хранения данных отчета — например, main_data — и поместить в него
# названия столбцов отчета в виде списка: «Изготовитель системы»,
# «Название ОС», «Код продукта», «Тип системы». Значения для этих
# столбцов также оформить в виде списка и поместить в файл main_data
# (также для каждого файла);

# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
# В этой функции реализовать получение данных через вызов функции get_data(),
# а также сохранение подготовленных данных в соответствующий CSV-файл;

# Пример того, что должно получиться:

# Изготовитель системы,Название ОС,Код продукта,Тип системы

# 1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

# 2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

# 3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based


# import re

# os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
# os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])

# import re
# import csv


# def write_to_csv(file, data):
#     with open(file, 'w') as f_n:
#         f_n_writer = csv.writer(f_n)
#         for nrow in data:
#             f_n_writer.writerow(nrow)


# def get_data(lst):
#     os_prod_list = []
#     os_name_list = []
#     os_code_list = []
#     os_type_list = []
#     main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
#     for file in lst:
#         datafile = open(file)
#         for row in datafile:
#             row = row.rstrip()
#             if re.match('Изготовитель системы', row):
#                 os_prod_list.append(re.search(r'(Изготовитель системы).\s*(.*)', row).group(2))
#             elif re.match('Название ОС', row):
#                 os_name_list.append(re.search(r'(Название ОС).\s*(.*)', row).group(2))
#             elif re.match('Код продукта', row):
#                 os_code_list.append(re.search(r'(Код продукта).\s*(.*)', row).group(2))
#             elif re.match('Тип системы', row):
#                 os_type_list.append(re.search(r'(Тип системы).\s*(.*)', row).group(2))

#     for k in range(len(lst)):
#         main_data.append([
#             os_prod_list[k],
#             os_name_list[k],
#             os_code_list[k],
#             os_type_list[k]
#          ])
#     return main_data


# if __name__ == "__main__":
#     res = get_data(['info_1.txt', 'info_2.txt', 'info_3.txt'])
#     write_to_csv('new_file.csv', res)

#     with open('new_file.csv') as f_n:
#         print(f_n.read())


# Задача 2. 
# Задание на закрепление знаний по модулю json. Есть файл orders
# в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
# его заполнение данными.

# Для этого:
# Создать функцию write_order_to_json(), в которую передается
# 5 параметров — товар (item), количество (quantity), цена (price),
# покупатель (buyer), дата (date). Функция должна предусматривать запись
# данных в виде словаря в файл orders.json. При записи данных указать
# величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json()
# с передачей в нее значений каждого параметра.

# ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

# {
#     "orders": []
# }

# вам нужно подгрузить JSON-объект
# и достучаться до списка, который и нужно пополнять
# а потом сохранять все в файл

# import json


# def write_order_to_json(item, quantity, price, buyer, date):
#     with open('orders.json') as f_n:
#         dict_to_json = json.load(f_n)
#         print(dict_to_json)
#         dict_to_json['orders'].append({
#             'item': item,
#             'quantity': quantity,
#             'price': price,
#             'buyer': buyer,
#             'date': date,
#         })
#     with open('orders.json', 'w') as f_w:
#         json.dump(dict_to_json, f_w, indent=4)


# if __name__ == "__main__":
#     write_order_to_json('Жигули', 3, 100, 'Бухаев', '08.04.2023')
#     write_order_to_json('Клинское', 2, 200, 'Бухаев', '08.04.2023')
#     write_order_to_json('Хамовники', 3, 500, 'Бухаев', '08.04.2023')
#     write_order_to_json('Хольстен', 4, 700, 'Бухаев', '08.04.2023')


# Задача 3. 
# Задание на закрепление знаний по модулю yaml.
#  Написать скрипт, автоматизирующий сохранение данных
#  в файле YAML-формата.
# Для этого:

# Подготовить данные для записи в виде словаря, в котором
# первому ключу соответствует список, второму — целое число,
# третьему — вложенный словарь, где значение каждого ключа —
# это целое число с юникод-символом, отсутствующим в кодировке
# ASCII(например, €);

# Реализовать сохранение данных в файл формата YAML — например,
# в файл file.yaml. При этом обеспечить стилизацию файла с помощью
# параметра default_flow_style, а также установить возможность работы
# с юникодом: allow_unicode = True;

# Реализовать считывание данных из созданного файла и проверить,
# совпадают ли они с исходными.
# import yaml

# def write_dict_to_yaml(dict, file):
#     with open(file, 'w') as f_n:
#         yaml.dump(dict, f_n, default_flow_style=False, allow_unicode = True)

#     with open(file) as f_n:
#         f_n_content = yaml.load(f_n)

#     print(f_n_content == dict)

# if __name__ == "__main__":
#     my_dict = {
#         '100€': [1, 2, 3, 4],
#         '200€': 8000,
#         '300€': {
#             'first': [1,2,3,4],
#             'second': 800,
#         }
#     }

#     write_dict_to_yaml(my_dict, 'file.yaml')