from catalog.models import Genre, Book, BookInstance, Author
from faker import Faker
from datetime import timedelta
import textwrap

fake = Faker()

# Create Genres
genres = [
    Genre(name='Science Fiction'),
    Genre(name='Satire'),
    Genre(name='Drama'),
    Genre(name='Adventure'),
    Genre(name='Romance'),
    Genre(name='Mystery')
]

# Save the genres to the database
for genre in genres:
    genre.save()

# Create Authors
authors = []
for i in range(1, 10):
    a_fname = fake.first_name()
    a_lname = fake.last_name()
    a_dob = fake.date_of_birth()
    a_dod = a_dob + timedelta(days=365*fake.random_int(65,100))
    author = Author(first_name=a_fname,
                    last_name=a_lname,
                    date_of_birth=a_dob,
                    date_of_death=a_dod)
    author.save()
    authors.append(author)


# Create Books
books = []
for i in range(1, 10):
    a_title = fake.text(50)
    a_author = authors[fake.random_int(0, len(authors)) - 1]
    a_summary = fake.text(1000)
    a_isbn = fake.isbn13()
    book = Book(title=a_title,
                author=a_author,
                summary=a_summary,
                isbn=a_isbn)
    book.save()
    book.genre.add(genres[fake.random_int(0, len(genres)) - 1])
    book.save()
    books.append(book)


# Create fake events
events = []
for i in range(1, 10):
    a_title = fake.text(50)
    a_time_date = fake.date_of_birth()
    a_location = fake.text(50)
    
    event = Event()




instances = []
for i in range(1, 400):
    a_book = books[fake.random_int(0, len(books)) - 1]
    a_imprint = fake.text(200)
    a_status = 'a'
    instance = BookInstance(book=a_book,
                            imprint=a_imprint,
                            status=a_status)
    instance.save()
    instances.append(instance)

print('Genre:')
for g in Genre.objects.all():
    print(g)

print('\nAuthor:')
for a in Author.objects.all():
    print(a)

print('\nBook:')
for b in Book.objects.all():
    print(b)

print('\nBookInstance:')
for i in BookInstance.objects.all():
    print(i)

# Retrieve a random book from model and print it.
books_count = Book.objects.count()
book = Book.objects.all()[fake.random_int(0, books_count - 1)]

print('\nExample Book:')
print(f'Title: {book.title}')
print(f'Author: {book.author}')
print(f'ISBN: {book.isbn}')
print(f'Summary:\n{textwrap.fill(book.summary, 77)}')

