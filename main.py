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


def add_book(title, author, year):
    new_book = {
        title: {
            "author": author,
            "year": year,
            "is_availability": None
        }
    }
    return library.update(new_book)


def run():
    while True:
        try:
            info = int(input("Введите число соответствующее действию:\n"
                             "1 - Показать список книг\n"
                             "2 - Добавить книгу\n"
                             "0 - Завершить программу\n"))
            if info == 1:
                book_list_view(library)
            elif info == 2:
                title = input("Введите название книги:\n")

                for book_name in library.keys():
                    if book_name == title:
                        print(f"\nКнига с названием \"{title}\" существует.\n"
                              f"Обновите информацию о ней!\n")

                author = input("Введите автора произведения:\n")
                year = int(input("Введите год издания книги:\n"))
                add_book(title, author, year)
                print(f"Добавлена/обновлена книга \"{title}\".\n"
                      f"Автор: {author}.\nГод издания: {year}.\n")
            elif info == 0:
                break
            else:
                print("Соответствие не найдено!")

        except ValueError:
            print("Ввод некорректного значения")


run()
