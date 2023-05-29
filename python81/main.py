# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать
# функционал для изменения и удаления данных

# import os

# phonebook = 'text.txt'
# fields = ["Фамилия", "Имя", "Телефон", "Описание"]


# def saveData(phonebook, data):  # Функция сохранения данных в файл
#     with open(phonebook, 'w', encoding='utf-8') as fout:

#         for i in range(len(data)):
#             s = ''
#             for v in data[i].values():
#                 s += v + ','
#             fout.write(f'{s[:-1]}\n')
#     print('данные обновлены')


# def readData(phonebook: str):  # Функция выгрузки данных из файл
#     data = []
#     with open(phonebook, 'r', encoding='utf-8') as fin:
#         for line in fin:
#             record = dict(zip(fields, line.strip().split(',')))
#             data.append(record)
#     return data


# def getNewPerson():  # Функция добавления человека в базу
#     phoneDirectory = readData(phonebook)
#     newRecord = dict()
#     for i in range(len(fields)):
#         newRecord[fields[i]] = (
#             input(f'введите данные по полю "{fields[i]}": '))
#     phoneDirectory.append(newRecord)
#     saveData(phonebook, phoneDirectory)


# def searchData(searchedData, fieldNum):  # Функция поиска по определенному полю
#     phoneDirectory = readData(phonebook)
#     tick = 0
#     find = False
#     printIndent()
#     print('Результаты поиска: ')
#     for line in phoneDirectory:
#         tick += 1
#         if searchedData.lower() in line[fields[fieldNum]].lower():
#             find = True
#             print(f'{tick}', end=" ")
#             print(*line.values())

#     if find == False:
#         print(
#             f'{searchedData} не найдена среди данных поля {fields[fieldNum]}')
#     os.system('pause')


# def askSearch():  # Меню поиска данных
#     while True:
#         printIndent()
#         print('Меню поиска')
#         for i in range(len(fields)):
#             print(f'{i} - поиск по полю {fields[i]}')
#         print(f'{len(fields)} - выход в главное меню')
#         answer = int(input('Введите номер меню: '))
#         if answer == len(fields):
#             break
#         if 0 <= answer < len(fields):
#             searched = input('введите искомое значение:')
#             searchData(searched, answer)


# def printAllData():  # Функция вывода всех данных
#     phoneDirectory = readData(phonebook)
#     tick = 0
#     printIndent()
#     print('Данные справочника:')
#     for line in phoneDirectory:
#         tick += 1
#         print(f'{tick}', end=" ")
#         print(*line.values())
#     os.system('pause')


# def printIndent():  # Функция вывода отступа для лучшей читаемости данных с консоли
#     print()
#     for i in range(20):
#         print('_', end='')
#     print()


# def remRecord():  # Функция удаления записи по введенному индексу
#     printAllData()
#     RecIndex = int(input('введите номер записи которую следует удалить: '))-1
#     phoneDirectory = readData(phonebook)
#     phoneDirectory.pop(RecIndex)
#     saveData(phonebook, phoneDirectory)
#     os.system('pause')


# def changeRecord():  # меню изменения записи
#     printAllData()
#     recIndex = int(
#         input('введите номер записи которую следует редактировать: '))-1
#     print(*enumerate(fields))
#     fieldsIndex = int(input('введите номер поля для редактирования: '))
#     phoneDirectory = readData(phonebook)
#     phoneDirectory[recIndex][fields[fieldsIndex]
#                              ] = input('введите новые данные: ')
#     saveData(phonebook, phoneDirectory)
#     os.system('pause')


# def AskAction():  # Функция вывода главного меню
#     while True:
#         printIndent()
#         print('Главное меню. \n'
#               '0 - ввести новую запись \n'
#               '1 - войти в меню поиска \n'
#               '2 - вывести все данные \n'
#               '3 - удалить запись из справочника \n'
#               '4 - редактировать запись из справочника \n'
#               '5 - выйти из программы \n'
#               'Что вы хотите сделать?:', end=' ')
#         answer = int(input())

#         if answer == 5:
#             return
#         elif answer == 0:
#             getNewPerson()
#         elif answer == 2:
#             printAllData()
#         elif answer == 1:
#             askSearch()
#         elif answer == 3:
#             remRecord()
#         elif answer == 4:
#             changeRecord()


# AskAction()
# @2@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# import csv
# import os

# phonebook = ("C:/Users/gkopeykin/Desktop/PythonTasks/python81/phonebook.csv")

# fields = ["Фамилия", "Имя", "Телефон", "Описание"]


# def load_contacts(phonebook):
#     contacts = []
#     with open(phonebook, 'r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             contacts.append(row)
#     return contacts


# def save_contacts(phonebook_csv, contacts):
#     with open(phonebook, 'w', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=fields)
#         writer.writeheader()
#         writer.writerows(contacts)


# def main():
#     print("Телефонный справочник")
#     print("--------------------")
#     phonebook = "python81/phonebook.csv"

#     while True:
#         print("\nМеню:")
#         print("1. Вывести все контакты")
#         print("2. Добавить контакт")
#         print("3. Изменить контакт")
#         print("4. Удалить контакт")
#         print("5. Сохранить и выйти")

#         choice = input("Выберите пункт меню: ")

#         if choice == "1":
#             contacts = load_contacts(phonebook)
#             print("Контакты:")
#             for contact in contacts:
#                 print(contact)
#         elif choice == "2":
#             new_contact = {}
#             for field in fields:
#                 value = input(f"Введите {field}: ")
#                 new_contact[field] = value
#             contacts = load_contacts("phonebook.csv")
#             contacts.append(new_contact)
#             save_contacts(phonebook, contacts)
#             print("Контакт добавлен.")
#         elif choice == "3":
#             contacts = load_contacts(phonebook)
#             index = int(
#                 input("Введите индекс контакта, который хотите изменить: "))
#             if 0 <= index < len(contacts):
#                 contact = contacts[index]
#                 for field in fields:
#                     value = input(f"Введите новое значение для {field}: ")
#                     contact[field] = value
#                 save_contacts(phonebook, contacts)
#                 print("Контакт изменен.")
#             else:
#                 print("Недопустимый индекс контакта.")
#         elif choice == "4":
#             contacts = load_contacts(phonebook)
#             index = int(
#                 input("Введите индекс контакта, который хотите удалить: "))
#             if 0 <= index < len(contacts):
#                 contacts.pop(index)
#                 save_contacts(phonebook, contacts)
#                 print("Контакт удален.")
#             else:
#                 print("Недопустимый индекс контакта.")
#         elif choice == "5":
#             contacts = load_contacts(phonebook)
#             save_contacts(phonebook, contacts)
#             print("Данные сохранены.")
#             break
#         else:
#             print("Некорректный выбор. Попробуйте еще раз.")


# if __name__ == "__main__":
#     main()
import csv


class Phonebook(object):
    def __init__(self, filename):
        self.filename = filename
        self.fields = ["Фамилия", "Имя", "Телефон", "Описание"]
        self.contacts = self.load_contacts()

    def load_contacts(self):
        contacts = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    contacts.append(row)
        except FileNotFoundError:
            print("Файл не найден. Создан новый справочник.")
        return contacts

    def save_contacts(self):
        with open(self.filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(self.contacts)
        print("Справочник сохранен.")

    def print_all_contacts(self):
        if not self.contacts:
            print("Справочник пуст.")
            return
        for contact in self.contacts:
            print(contact)

    def add_contact(self):
        new_contact = {}
        for field in self.fields:
            value = input(f"Введите {field}: ")
            new_contact[field] = value
        self.contacts.append(new_contact)
        print("Контакт добавлен.")

    def edit_contact(self):
        index = int(input("Введите индекс контакта, который хотите изменить: "))
        if 0 <= index < len(self.contacts):
            contact = self.contacts[index]
            for field in self.fields:
                value = input(f"Введите новое значение для {field}: ")
                contact[field] = value
            print("Контакт изменен.")
        else:
            print("Недопустимый индекс контакта.")

    def delete_contact(self):
        index = int(input("Введите индекс контакта, который хотите удалить: "))
        if 0 <= index < len(self.contacts):
            self.contacts.pop(index)
            print("Контакт удален.")
        else:
            print("Недопустимый индекс контакта.")

    def menu(self):
        while True:
            print("\nМеню:")
            print("1. Вывести все контакты")
            print("2. Добавить контакт")
            print("3. Изменить контакт")
            print("4. Удалить контакт")
            print("5. Сохранить и выйти")

            choice = input("Выберите пункт меню: ")

            if choice == "1":
                self.print_all_contacts()
            elif choice == "2":
                self.add_contact()
            elif choice == "3":
                self.edit_contact()
            elif choice == "4":
                self.delete_contact()
            elif choice == "5":
                self.save_contacts()
                break
            else:
                print("Некорректный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    phonebook = Phonebook("phonebook.csv")
    phonebook.menu()
