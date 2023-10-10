import pandas as pd

def data_input():
    flag = True
    titles = pd.read_excel('./notebook.xlsx', usecols=0)
    while flag:
        tittle = input("Введите заголовок")
        if tittle in titles:
            print("Заметка с таким заголовком уже существует")
        else:
            flag = False
    note = input("Введите текст заметки")
    save_dict(tittle, note)


def edit(number: int):
    answer = input('1) Изменить заголовок \n 2) Изменить текст заметки \n 3) Выход в главное меню')
    match answer:
        case:

def edit_note(number: int):
    notes = pd.read_excel('./notebook.xlsx', usecols=1)
    print(notes[number])
    notes[number] = input("введите новый текст заметки: \n")

def edit_tittle(number: int):
    titles = pd.read_excel('./notebook.xlsx', usecols=0)
    print(titles[number])
    for_save = pd.DataFrame({'Titles': titles, 'Notes': notes})
    for_save.to_excel('./notebook.xlsx')










def create_note(note: str, title: str) :

    my_dict = dict(zip(titles, notes))
    return dict(sorted(my_dict.items()))


# def save_dict(notes: list(), titles: list()) :
#     s = pd.Series(notes, index=titles)
#     s.to_excel('./notebook.xlsx')
def save_dict(new_title:str, new_note:str) :
    # my_dict = pd.read_excel('./notebook.xlsx')
    notes = pd.read_excel('./notebook.xlsx', usecols=1)
    titles = pd.read_excel('./notebook.xlsx', usecols=0)
    for i in range(len(titles)):
        if (i == len(titles)):
            titles.add(new_title)
            notes.add(new_note)
        elif (titles[i] < new_title < titles[i+1]):
            titles = titles[:i] + [new_title] + titles[i:]
            notes = notes[:i] + [new_note] + notes[i:]
        elif (titles[i] == new_title):
            titles = titles[:i-1]+ [new_title] + titles[i:]
            notes = notes[:i-1]+ [new_note] + notes[i:]
        for_save = pd.DataFrame({'Titles': titles, 'Notes': notes})
        for_save.to_excel('./notebook.xlsx')










