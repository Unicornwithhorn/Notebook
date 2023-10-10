# Напишите проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список заметок,
# редактировать заметку, удалять заметку.

import pandas as pd
from FilesWork import save_load_delete
notes = ['Селёдка', 'Сельдерей', 'Водка']
titles = ['Список селёдок', 'Список селдереев', 'Список водков']
save_load_delete.create_dict(notes,titles)
save_load_delete.save_dict(notes,titles)




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