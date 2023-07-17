def read_file():
    with open('phones.txt', 'r', encoding='utf-8') as f:
        my_list = [i.strip() for i in f]
        for i in range(len(my_list)):
            my_list[i] = my_list[i].split(";")
    return my_list

def write_file(data):
    string = ''
    for elem in data:
        for i in range(len(elem)):
            if i == len(elem) - 1:
                string += elem[i] + "\n"
            else:
                string += elem[i] + ";"
    with open('phones.txt', 'w', encoding='utf-8') as file:
        file.write(string)

def print_info(info):
    print("----------")
    for elem in info:
        print(*elem)

def search(request, x): # На вход принимает строку с данными и переменную (0 - фамилия, 1 - Имя, 2 - отчество, 3 - номер телефона)
    data = read_file()
    answer_data = []
    for elem in data:
        if elem[x].upper() == request.upper():
            answer_data.append(elem)
    return answer_data

def search_fio(request):
    data = read_file()
    request = request.split()
    answer_data = []
    for elem in data:
        if elem[:3] == request:
            answer_data.append(elem)
    return answer_data

def replace_number(fio, new_number):
    data = read_file()
    fio = fio.split()
    for i in range(len(data)):
        if data[i][:3] == fio:
            data[i][3] = new_number
    write_file(data)

def delete_contact(fio):
    data = read_file()
    fio = fio.split()
    for i in range(len(data) - 1, -1, -1):
        if data[i][:3] == fio:
            data.pop(i)  
    write_file(data)

def add_number(fio, new_number):
    data = read_file()
    fio = fio.split()
    fio.append(new_number)
    data.append(fio)
    write_file(data)            


def menu():
    while True:
        print("Выберите пункт меню")
        print("1 - Поиск номера по фамилии")
        print("2 - Поиск контакта по номеру")
        print("3 - Вывод всего справочника")
        print("4 - Поиск по ФИО")
        print("5 - Изменить номер телефона")
        print("6 - Добавить контакт")
        print("7 - Удалить контакт")
        print("0 - Выход из программы")
        menu_number = int(input("Введите число: "))
        print("----------")
        if menu_number == 1:
            print_info(search(input("Введите фамилию: "), 0))
            print("----------")
        elif menu_number == 2:
            print_info(search(input("Введите номер телефона в формате +7ХХХХХХХХХХ: "), 3))
            print("----------")
        elif menu_number == 3:
            print_info(read_file())
            print("----------")
        elif menu_number == 4:
            print_info(search_fio(input("Введите ФИО: ")))
            print("----------")
        elif menu_number == 5:
            fio = input("Введите ФИО, чей номер хотите изменить: ")
            new_number = input("Введите новый номер: ")
            replace_number(fio, new_number)
            print("----------")
        elif menu_number == 6:
            fio = input("Введите ФИО нового контакта: ")
            new_number = input("Введите номер: ")
            add_number(fio, new_number)
            print("----------")
        elif menu_number == 7:
            fio = input("Введите ФИО контакта, который хотите удалить: ")
            delete_contact(fio)
            print("----------")
        elif menu_number == 0:
            break

if __name__ == '__main__':
    menu()