
class TestBooksCollector:
    # тест на добавление двух книг
    def test_add_new_book_two_books_added_books(self, collector_with_book):
        collector_with_book.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector_with_book.get_books_rating()) == 2

    # тест на добавление уже добавленной ранее книги
    def test_add_new_book_existing_book_not_added(self, collector_with_book):
        collector_with_book.add_new_book('Книга')
        assert len(collector_with_book.get_books_rating()) == 1

    # тест на установку рейтинга добавленной книги
    def test_set_book_rating_new_value_in_range_1_to_10_set_new_rating(self, collector_with_book):
        collector_with_book.set_book_rating('Книга', 10)
        assert collector_with_book.get_book_rating('Книга') == 10

    # тест на установку рейтинга выше 10
    def test_set_book_rating_new_value_not_in_range_1_to_10_not_set_new_rating(self, collector_with_book):
        collector_with_book.set_book_rating('Книга', 11)
        assert collector_with_book.get_book_rating('Книга') == 1

    # тест на проверку стандартного рейтинга добавленной книги
    def test_get_book_rating_name_book_shows_rating_1(self, collector_with_book):
        assert collector_with_book.get_book_rating('Книга') == 1

    # тест на вывод списка с определённым рейтингом
    def test_get_books_with_specific_rating_value_in_range_1_to_10_show_list(self, collector_with_book):
        collector_with_book.add_new_book('Доширак - лучший выбор!')
        collector_with_book.set_book_rating('Доширак - лучший выбор!', 9)
        collector_with_book.add_new_book('Мисс говядина')
        collector_with_book.set_book_rating('Мисс говядина', 9)
        assert collector_with_book.get_books_with_specific_rating(9) == ['Доширак - лучший выбор!', 'Мисс говядина']

    # тест на вывод пуcтого списка при запросе рейтинга 11
    def test_get_books_with_specific_rating_value_not_in_range_1_to_10_show_empty_list(self, collector_with_book):
        collector_with_book.add_new_book('Доширак - лучший выбор!')
        collector_with_book.set_book_rating('Доширак - лучший выбор!', 9)
        collector_with_book.add_new_book('Мисс говядина')
        collector_with_book.set_book_rating('Мисс говядина', 9)
        assert collector_with_book.get_books_with_specific_rating(11) == []

    # тест на получение всего словаря с книгами и рейтингом
    def test_get_books_rating_show_dict(self, collector_with_book):
        collector_with_book.add_new_book('Доширак - лучший выбор!')
        collector_with_book.set_book_rating('Доширак - лучший выбор!', 9)
        collector_with_book.add_new_book('Мисс говядина')
        collector_with_book.set_book_rating('Мисс говядина', 9)
        assert collector_with_book.get_books_rating() == {'Книга': 1, 'Доширак - лучший выбор!': 9, 'Мисс говядина': 9}

    # тест добавление книги в избранное из добавленных раньше
    def test_add_book_in_favorites_book_from_books_rating_add_book_in_favorites(self, collector_with_book):
        collector_with_book.add_new_book('Терминатор Кроль: Восстание морковок')
        collector_with_book.add_book_in_favorites('Терминатор Кроль: Восстание морковок')
        assert collector_with_book.get_list_of_favorites_books() == ['Терминатор Кроль: Восстание морковок']

    # тест добавление новой книги сразу в избранное
    def test_add_book_in_favorites_book_not_from_books_rating_not_add_book_in_favorites(self, collector_with_book):
        collector_with_book.add_book_in_favorites('Терминатор Кроль: Восстание морковок')
        assert collector_with_book.get_list_of_favorites_books() == []

    # тест на удаление книги из избранного
    def test_delete_book_from_favorites_book_from_favorites_book_not_in_favorites(self, collector_with_book):
        collector_with_book.add_new_book('Терминатор Кроль: Восстание морковок')
        collector_with_book.add_book_in_favorites('Терминатор Кроль: Восстание морковок')
        collector_with_book.delete_book_from_favorites('Терминатор Кроль: Восстание морковок')
        assert collector_with_book.get_list_of_favorites_books() == []

    # тест на получение списка избранных книг
    def test_get_list_of_favorites_books_show_list(self, collector_with_book):
        collector_with_book.add_book_in_favorites('Книга')
        assert collector_with_book.get_list_of_favorites_books() == ['Книга']


