# Создайте словарь library, где ключами будут названия книг,
# а значениями — словари с информацией о книге (автор, год издания, наличие).
# После этого реализуйте первую функцию 'book_list_view(library)',
# которая выводит в консоль названия всех книг в библиотеке.
# Если в библиотеке нет книг, функция выводит сообщение об этом.

# Реализуйте функцию `add_book(title, author, year)`, которая добавляет книгу
# в словарь `library`. Поле `наличие` при добавлении новой книги должно быть `None`
# (означает, что книга в библиотеке, но не определен ее статус).
# Если книга с таким названием уже существует,
# программа должна предложить обновить информацию о ней.
# Функция должна вывести сообщение об успешном добавлении/обновлении
# информации о книге с ее названием

# Реализуйте функцию `remove_book(title)`, которая удаляет книгу из словаря.
# Если книга не найдена, программа должна вывести сообщение об этом.
# После удаления функция должна вывести сообщение об удалении книги
# с ее названием.

# Реализуйте функцию `issue_book(title)`, которая отмечает книгу
# как выданную(`наличие` становится `False`).
# Реализуйте функцию `return_book(title)`, которая отмечает книгу
# как вернувшуюся в библиотеку(`наличие` становится `True`).

library = {
    "Отцы и дети": {
        "author": "И. С. Тургенев",
        "year": 1862,
        "is_availability": True
    },
    "Мастер и Маргарита": {
        "author": "М. А. Булгаков",
        "year": 1966,
        "is_availability": True
    },
    "Евгений Онегин": {
        "author": "А. С. Пушкин",
        "year": 1833,
        "is_availability": True
    },
    "Преступление и наказание": {
        "author": "Ф. М. Достоевский",
        "year": 1866,
        "is_availability": True
    },
    "Мёртвые души": {
        "author": "Н. В. Гоголь",
        "year": 1842,
        "is_availability": True
    }
}


def book_list_view(library):
    if not library:
        print("В библиотеке нет книг.")
    else:
        for title in library.keys():
            print(title)


def add_book(library):
    def add_author_and_year(added_or_updated):
        author = input("Введите автора произведения:\n")
        year = int(input("Введите год издания книги:\n"))
        library[title] = {
            "author": author,
            "year": year,
            "is_availability": None
        }
        print(f"\nКнига с названием \"{title}\" {added_or_updated}.\n"
              f"Автор: {author}.\n"
              f"Год: {year}.\n")

    title = input("Введите название книги:\n")
    if title in library:
        print(f"\nКнига с названием \"{title}\" существует.\n"
              f"Обновите информацию о ней!\n")

        add_author_and_year("обновлена")
    else:
        add_author_and_year("добавлена")


def remove_book(library):
    title = input("Введите название книги для удаления:\n")
    if title not in library:
        print(f"\nКнига \"{title}\" не найдена.\n")
    else:
        del library[title]
        print(f"\nКнига \"{title}\" удалена.\n")


def issue_return_book(library, is_availability, issue_return):
    title = input("Введите название книги:\n")
    if title in library:
        library[title] = {
            "author": library[title].get("author"),
            "year": library[title].get("year"),
            "is_availability": is_availability
        }
        print(f"\nКнига \"{title}\" {issue_return}.\n")
    else:
        print("\nНет такой книги.\n")


def run():
    while True:
        try:
            info = int(input("Введите число соответствующее действию:\n"
                             "1 - Показать список книг\n"
                             "2 - Добавить книгу\n"
                             "3 - Удалить книгу\n"
                             "4 - Выдать книгу\n"
                             "5 - Вернуть книгу\n"
                             "0 - Завершить программу\n"))
            if info == 1:
                book_list_view(library)
            elif info == 2:
                add_book(library)
            elif info == 3:
                remove_book(library)
            elif info == 4:
                issue_return_book(library, False, "выдана")
            elif info == 5:
                issue_return_book(library, True, "возвращена")
            elif info == 0:
                break
            else:
                print("Соответствие не найдено!")

        except ValueError:
            print("Ввод некорректного значения")


run()
