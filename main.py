# Создайте словарь library, где ключами будут названия книг,
# а значениями — словари с информацией о книге (автор, год издания, наличие).
# После этого реализуйте первую функцию 'book_list_view(library)',
# которая выводит в консоль названия всех книг в библиотеке.
# Если в библиотеке нет книг, функция выводит сообщение об этом.

library = {
    # "Отцы и дети": {
    #     "autor": "И. С. Тургенев",
    #     "year": 1862,
    #     "is_availability": True
    # },
    # "Мастер и Маргарита": {
    #     "autor": "М. А. Булгаков",
    #     "year": 1966,
    #     "is_availability": True
    # },
    # "Евгений Онегин": {
    #     "autor": "А. С. Пушкин",
    #     "year": 1833,
    #     "is_availability": True
    # },
    # "Преступление и наказание": {
    #     "autor": "Ф. М. Достоевский",
    #     "year": 1866,
    #     "is_availability": True
    # },
    # "Мёртвые души": {
    #     "autor": "Н. В. Гоголь",
    #     "year": 1842,
    #     "is_availability": True
    # }
}


def book_list_view(dict_library):
    list_availability = []
    for availability in dict_library.values():
        list_availability.append(availability.get("is_availability"))

    if dict_library == {} or set(list_availability) == {False}:
        print("В библиотеке нет книг")
    else:
        for book_name in dict_library.keys():
            print(book_name)


book_list_view(library)
