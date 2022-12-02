import pytest
from main import BooksCollector
@pytest.fixture()
def collector_with_book():
    collector = BooksCollector()
    collector.add_new_book('Книга')
    return collector

