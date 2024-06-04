
from data_create import name_data, surname_data, phone_data


"""Добавление контакта"""
def add_contact():
    name = name_data() # Имя
    surname = surname_data() # Фамилия
    phone = phone_data() # Телефон

    with open('phonebook.csv', 'a', encoding='utf-8') as f:
        f.write(f"{name} {surname} {phone}\n")


"""Чтение файла"""
def read_file_to_dict():
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Имя', 'Фамилия', 'Телефон']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list


def read_file_to_list():
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list


"""Параметры поиска"""
def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = input('1 - по имени\n2 - по фамилии\n3 - по телефону\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите телефон для поиска: ')
        print()
    return search_field, search_value


"""Поиск номера"""
def find_number(contact_list):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Имя', '2': 'Фамилия', '3': 'Телефон'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()


def get_new_number():
    last_name = input('Введите имя: ')
    first_name = input('Введите фамилию: ')
    phone_number = input('Введите телефон: ')
    return last_name, first_name, phone_number


"""Поиск для изменения"""
def search_to_change(contact_list: list):
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден')
    print()


"""Изменение контакта"""
def change_contact():
    contact_list = read_file_to_list()
    number_to_change = search_to_change(contact_list)
    contact_list.remove(number_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Имя\n2 - Фамилия\n3 - Телефон\n')
    if field == '1':
        number_to_change[0] = input('Введите имя: ')
    elif field == '2':
        number_to_change[1] = input('Введите фамилию: ')
    elif field == '3':
        number_to_change[2] = input('Введите телефон: ')
    contact_list.append(number_to_change)
    with open('phonebook.csv', 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


"""Удаление контакта"""
def delete_contact():
    contact_list = read_file_to_list()
    number_to_change = search_to_change(contact_list)
    contact_list.remove(number_to_change)
    with open('phonebook.csv', 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


"""Просмотр контактов"""
def view_contact():
    list_of_contacts = sorted(read_file_to_dict(), key=lambda x: x['Имя'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts


def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print() 