import peewee
from model import Author
from model import Book


if __name__ == '__main__':
    try:
        Author.create_table()
    except peewee.OperationalError:
        print('Author table already exists')

    try:
        Book.create_table()
    except peewee.OperationalError:
        print('Book table already exists')

    author01 = Author.create(name='H. G. Wells')
    book01 = {'title': 'A Máquina do tempo', 'author': author01}
    book02 = {'title': 'Guerra dos Mundos', 'author': author01}

    author02 = Author.create(name='Julio Verne')
    book03 = {'title': 'Volta ao mundo em 80 dias', 'author': author02}
    book04 = {'title': 'Vinte Mil Leguas Submarinas', 'author': author01}

    books = [book01, book02, book03, book04]

    Book.insert_many(books).execute()

    book = Book.get(Book.title == 'Volta ao mundo em 80 dias')
    print(book.title)

    books = Book.select().join(Author).where(Author.name == 'H. G. Wells')

    print(books.count())

    for book in books:
        print(book.title)

    author = Author.get(Author.name == 'Julio Verne')
    book = Book.get(Book.title == 'Vinte Mil Leguas Submarinas')

    book.author = author
    book.save()

    book = Book.get(Book.title == 'Guerra dos Mundos')
    book.delete_instance()