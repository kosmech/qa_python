from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector_with_book):
        # создаем экземпляр (объект) класса BooksCollector
        # добавляем две книги
        collector_with_book.add_new_book('Что делать, если ваш кот хочет вас убить')
        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector_with_book.get_books_rating()) == 2
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_rating_set_rating_10(self, collector_with_book):
        collector_with_book.set_book_rating('Книга', 10)
        assert collector_with_book.get_book_rating('Книга') == 10
    def test_get_book_rating_new_book_rating_1(self, collector_with_book):
        assert collector_with_book.get_book_rating('Книга') == 1
    def test_get_books_with_specific_rating_9(self, collector_with_book):
        collector_with_book.set_book_rating('Книга', 10)
        collector_with_book.add_new_book('Доширак - лучший выбор!')
        collector_with_book.set_book_rating('Доширак - лучший выбор!', 9)
        collector_with_book.add_new_book('Мисс говядина')
        collector_with_book.set_book_rating('Мисс говядина', 9)
        assert collector_with_book.get_books_with_specific_rating(9) == ['Доширак - лучший выбор!', 'Мисс говядина']
    def test_get_books_rating_show_dict(self, collector_with_book):
        collector_with_book.set_book_rating('Книга', 10)
        collector_with_book.add_new_book('Доширак - лучший выбор!')
        collector_with_book.set_book_rating('Доширак - лучший выбор!', 9)
        collector_with_book.add_new_book('Мисс говядина')
        collector_with_book.set_book_rating('Мисс говядина', 9)
        assert collector_with_book.get_books_rating() == {'Книга': 10, 'Доширак - лучший выбор!': 9, 'Мисс говядина': 9}
    def test_add_book_in_favorites_add_book(self, collector_with_book):
        collector_with_book.add_new_book('Терминатор Кроль: Восстание морковок')
        collector_with_book.add_book_in_favorites('Терминатор Кроль: Восстание морковок')
        assert 'Терминатор Кроль: Восстание морковок' in collector_with_book.get_list_of_favorites_books()
    def test_delete_book_from_favorites_delete_success(self, collector_with_book):
        collector_with_book.add_new_book('Терминатор Кроль: Восстание морковок')
        collector_with_book.add_book_in_favorites('Терминатор Кроль: Восстание морковок')
        collector_with_book.delete_book_from_favorites('Терминатор Кроль: Восстание морковок')
        assert 'Терминатор Кроль: Восстание морковок' not in collector_with_book.get_list_of_favorites_books()


