from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_rating_set_10(self):
        collector = BooksCollector() # создаем экземпляр (объект) класса BooksCollector
        collector.add_new_book('Зомби попугай') # добавляем книгу "Зомби попугай"
        collector.set_book_rating('Зомби попугай', 10)
        assert collector.get_book_rating('Зомби попугай') == 10
    def test_get_book_rating_1(self):
        collector = BooksCollector()
        collector.add_new_book('Собака-барабака')
        assert collector.get_book_rating('Собака-барабака') == 1

    def test_get_books_with_specific_rating_9(self):
        collector = BooksCollector()
        collector.add_new_book('Восстание микроволновок')
        collector.set_book_rating('Восстание микроволновок', 10)
        collector.add_new_book('Доширак - лучший выбор!')
        collector.set_book_rating('Доширак - лучший выбор!', 9)
        collector.add_new_book('Мисс говядина')
        collector.set_book_rating('Мисс говядина', 9)
        assert collector.get_books_with_specific_rating(9) == ['Доширак - лучший выбор!', 'Мисс говядина']
    def test_get_books_rating_show_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Восстание микроволновок')
        collector.set_book_rating('Восстание микроволновок', 10)
        collector.add_new_book('Доширак - лучший выбор!')
        collector.set_book_rating('Доширак - лучший выбор!', 9)
        collector.add_new_book('Мисс говядина')
        collector.set_book_rating('Мисс говядина', 9)
        assert collector.get_books_rating() == {'Восстание микроволновок': 10, 'Доширак - лучший выбор!': 9, 'Мисс говядина': 9}
    def test_add_book_in_favorites_add_book(self):
        collector = BooksCollector()
        collector.add_new_book('Терминатор Кроль: Восстание морковок')
        collector.add_book_in_favorites('Терминатор Кроль: Восстание морковок')
        assert 'Терминатор Кроль: Восстание морковок' in collector.get_list_of_favorites_books()
    def test_delete_book_from_favorites_delete_sucsess(self):
        collector = BooksCollector()
        collector.add_new_book('Терминатор Кроль: Восстание морковок')
        collector.add_book_in_favorites('Терминатор Кроль: Восстание морковок')
        collector.delete_book_from_favorites('Терминатор Кроль: Восстание морковок')
        assert 'Терминатор Кроль: Восстание морковок' not in collector.get_list_of_favorites_books()


