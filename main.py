# Напишите проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список заметок,
# редактировать заметку, удалять заметку.

import interface
import file_work
import pandas as pd

interface.main_menu()

# from FilesWork import save_load_delete
# notes = ['Селёдка', 'Сельдерей', 'Водка']
# titles = ['Список селёдок', 'Список селдереев', 'Список водков']
# save_load_delete.create_dict(notes,titles)
# save_load_delete.save_dict(notes,titles)
#
# my_dict = dict()
# text_menu = """1) Показать список заметок\n
#             2) Создать новую заметку \n
#             3) Выход"""
#
#
# def hoho():
#     print("хохо")
#
#
# variants = [interface.choice_note(),
#           hoho(),
#           interface.end_work()]
# flag = True
# while flag:
#     answer = input(text_menu)
#     if int(answer) in variants.keys():
#         flag = False
#         variants.get(answer-1)
#     else:
#         print('Вы ввели некорректное значение. Повторите ввод')


# interface.main_menu()

# df = pd.DataFrame(notes, index= titles)
# test = Series.
# df.to_excel('./notebook.xlsx')

# top_players = pd.read_excel('./notebook.xlsx')
# print(df)
# print()
# print(df[2])

# cols = [0, 2, 3]

# top_players = pd.read_excel('./notebook.xlsx', usecols=cols)
# print(top_players.head())
# top_players.head()