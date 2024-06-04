
from logger import add_contact, read_file_to_dict, find_number, change_contact, delete_contact, view_contact

def interface():
    print('Что необходимо сделать?')
    command = input('1 - Добавить контакт\n2 - Найти контакт\n3 - Изменить контакт\n\
4 - Удалить контакт\n5 - Просмотреть все контакты\n6 - Выйти из справочника\n')
    print()
    if command == '1':
        add_contact()
    elif command == '2':
        contact_list = read_file_to_dict()
        find_number(contact_list)
    elif command == '3':
        change_contact()
    elif command == '4':
        delete_contact()
    elif command == '5':
        view_contact()
    elif command == '6':
        return
    else:
        print('Нет такого варианта')
        
