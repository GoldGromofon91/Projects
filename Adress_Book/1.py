import json, os


def save_file(obj):
    with open('contact.json', 'w', encoding='utf-8') as f:
        json.dump(obj, f)
        # print('Контакт записан в файл')


def load_file():
    with open('contact.json', 'r', encoding='utf-8') as f:
        contact = json.load(f)
    return contact


def info():
    print('"-h" - для вызова справки о помощи')
    print('"-a" - для добавления в адрессную книгу введите в формате: Имя_Фамилия_Номер тел.')
    print('"-l" - для просмотра списка контактов')
    print('"-s" - для поиска контакта введите:"Имя"')
    print('"-c" - для изменения объекта')
    print('"-d" - для удаления контакта введите')


def get_info():
    contact = load_file()
    print('-' * 20 + 'Список контактов' + '-' * 20)
    for i, el in enumerate(contact, 1):
        print(f' {i}.{el}')


def search_contact(param_contact):
    item_s = []
    p_contact = load_file()
    for el in p_contact:
        for key, val in el.items():
            if param_contact == val:
                item_s.append(el)
    print(f'Контакты с именем {param_contact}')
    for i, el in enumerate(item_s, 1):
        print(f'{i}.{el}')


def del_contact(param_contact):
    contact = load_file()
    del contact[param_contact - 1]
    print('Контакт удален!')
    save_file(contact)


def change_contact(num, change_param):
    ch_con = load_file()
    for i in range(len(ch_con)):
        if i == num - 1:
            ch_con[i] = {'Имя': change_param[0], 'Фамилия': change_param[1], 'Телефон': change_param[2]}
            print('Контакт изменен!')
    save_file(ch_con)


item = []
running = True
us_data = input('Программа адрессная книга.\nДля начала работы введите "start", для выхода введите "q": ')
while running:
    try:
        if us_data.isdigit() or (us_data != 'start' and us_data != 'q'):
            raise ValueError
        else:
            break
    except ValueError:
        us_data = input('Для начала работы введите "start", для выхода введите "q": ')

if us_data == 'start':
    print('Для просмотра всех функций введите "-h": ')
    while running:
        usr = input('Введите команду --> ')
        if usr == 'q':
            running = False
        if usr == '-h':
            info()
        elif usr == '-a':
            if os.path.exists('/Users/mac/Desktop/GeekBrains/Tasks/Adress_Book/contact.json'):
                usr_add = input().split()
                con = load_file()
                contact_dir = {'Имя': usr_add[0], 'Фамилия': usr_add[1], 'Телефон': usr_add[2]}
                con.append(contact_dir)
                save_file(con)
                print('Контакт записан в файл')
            else:
                usr_add = input().split()
                contact_dir = {'Имя': usr_add[0], 'Фамилия': usr_add[1], 'Телефон': usr_add[2]}
                item.append(contact_dir)
                save_file(item)
                print('Контакт записан в файл')
        elif usr == '-l':
            try:
                get_info()
            except FileNotFoundError:
                print('В вашей книге пока нет контактов, введите "-a" чтобы добавить контакт')
        elif usr == '-s':
            usr_search = input()
            search_contact(usr_search)
        elif usr == '-d':
            print('Для удаления контакта введите его порядковый номер')
            try:
                usr_del = int(input())
                del_contact(usr_del)
            except ValueError:
                print('Введите порядковый номер контакта')
        elif usr == '-c':
            usr_num = int(input('Введите порядковый номер контакта, который нужно ихменить: '))
            usr_data = input('Введите новые данные контакта в формате: "Имя_Фамилия_Телефон"').split()
            change_contact(usr_num, usr_data)
    else:
        print('До свидания!')
elif us_data == 'q':
    print('До свидания!')
