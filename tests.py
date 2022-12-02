from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector_with_book): # тест на добавление двух книг
        collector_with_book.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector_with_book.get_books_rating()) == 2

    def test_add_new_book_try_added_book(self, collector_with_book): # тест на добавление уже добавленной ранее книги
        collector_with_book.add_new_book('Книга')
        assert len(collector_with_book.get_books_rating()) == 1

    def test_set_book_rating_set_rating_10(self, collector_with_book): # тест на установку рейтинга добавленной книги
        collector_with_book.set_book_rating('Книга', 10)
        assert collector_with_book.get_book_rating('Книга') == 10

    def test_set_book_rating_try_set_rating_11_past_value_1(self, collector_with_book): # тест на установку рейтинга выше 10
        collector_with_book.set_book_rating('Книга', 11)
        assert collector_with_book.get_book_rating('Книга') == 1

    def test_get_book_rating_new_book_rating_1(self, collector_with_book): # тест на проверку стандартного рейтинга добавленной книги
        assert collector_with_book.get_book_rating('Книга') == 1

    def test_get_books_with_specific_rating_show_list_with_rating_9(self, collector_with_book): # тест на вывод списка с определённым рейтингом
        collector_with_book.set_book_rating('Книга', 10)
        collector_with_book.add_new_book('Доширак - лучший выбор!')
        collector_with_book.set_book_rating('Доширак - лучший выбор!', 9)
        collector_with_book.add_new_book('Мисс говядина')
        collector_with_book.set_book_rating('Мисс говядина', 9)
        assert collector_with_book.get_books_with_specific_rating(9) == ['Доширак - лучший выбор!', 'Мисс говядина']

    def test_get_books_rating_show_dict(self, collector_with_book): # тест на получение всего словаря с книгами и рейтингом
        collector_with_book.set_book_rating('Книга', 10)
        collector_with_book.add_new_book('Доширак - лучший выбор!')
        collector_with_book.set_book_rating('Доширак - лучший выбор!', 9)
        collector_with_book.add_new_book('Мисс говядина')
        collector_with_book.set_book_rating('Мисс говядина', 9)
        assert collector_with_book.get_books_rating() == {'Книга': 10, 'Доширак - лучший выбор!': 9, 'Мисс говядина': 9}

    def test_add_book_in_favorites_add_book(self, collector_with_book): # тест добавление книги в избранное
        collector_with_book.add_new_book('Терминатор Кроль: Восстание морковок')
        collector_with_book.add_book_in_favorites('Терминатор Кроль: Восстание морковок')
        assert 'Терминатор Кроль: Восстание морковок' in collector_with_book.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_success(self, collector_with_book): # тест на удаление книги из избранного
        collector_with_book.add_new_book('Терминатор Кроль: Восстание морковок')
        collector_with_book.add_book_in_favorites('Терминатор Кроль: Восстание морковок')
        collector_with_book.delete_book_from_favorites('Терминатор Кроль: Восстание морковок')
        assert 'Терминатор Кроль: Восстание морковок' not in collector_with_book.get_list_of_favorites_books()


