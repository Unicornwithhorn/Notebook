import operations
# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок.
def menu(text_menu: str, variants: dict):
    flag = True
    while flag:
        answer = input(text_menu)
        if answer in variants.keys():
            flag = False
            variants.get(answer)
        else:
            print('Вы ввели некорректное значение. Повторите ввод')


def choice_note():
    pass


def create_new_note(variants: dict):
    flag = True
    while flag:
        title = input("Введите заголовок заметки")
        if title in variants.keys():
            print('Заметка с таким названием уже существует. Заменить?')

        else:
            flag = False
    note = input("Введите тест заметки")
    variants[title] = note



def end_work():
    pass


def main_menu():
    menu('1) Показать список заметок\n2) Создать новую заметку \n 3) Выход', {'1': choice_note(),
                                                                              '2': create_new_note(),
                                                                              '3': end_work()})

