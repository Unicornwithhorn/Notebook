import file_work


# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок.
def menu(text_menu: str, variants: dict):
    while True:
        answer = input(text_menu)
        if answer in variants.keys():
            break
        else:
            print('Вы ввели некорректное значение. Повторите ввод\n')
    load_menu(variants.get(answer))


def load_menu(point_id: int):
    match point_id:
        case 1:
            show_note()
        case 2:
            create_new_note(),
        case 3:
            end_work()


def show_note():
    variants = file_work.load_data()
    titles = '\n'.join(variants.keys())
    print(titles)
    main_menu()





def create_new_note():
    variants = file_work.load_data()
    flag = True
    while flag:
        title = input("Введите заголовок заметки\n")
        if title in variants.keys():
            answer = input('Заметка с таким названием уже существует. Заменить? (да\нет)\n')
            if answer.lower() == "да":
                del variants[title]
                flag = False
            else:
                print('Введите незанятое название заметки\n')
        else:
            flag = False
    note = input("Введите тест заметки\n")
    variants[title] = note
    file_work.save_data(variants)
    print(f'Заметка "{title.upper()} была сохранена"')
    main_menu()


def end_work():
    pass


def main_menu():
    menu('1) Показать список заметок\n'
         '2) Создать новую заметку \n'
         '3) Выход \n',
         {'1': 1,
          '2': 2,
          '3': 3})
