'''
Concerned with storing and retrieving books from a text file
'''
books_file = 'library.txt'

def add_book(title, author):
	with open(books_file, 'w') as f:
		f.write(f'{title},{author},0')


def get_all_books():
	with open(books_file, 'r') as f:
		lines = [line.strip().split(',') for line in f.readlines()]

	return [
		{'title' : line[0], 'author' : line[1], 'read' : line[2]}
		for line in lines
	]

def mark_book_as_read(title):
	books = get_all_books()
	for book in books:
		if book['title'] == title:
			book['read'] = '1'

	_save_all_books(books)

def delete_book(title, author):
	books = get_all_books()
	for book in books:
		if book['title'] == title and book['author'] == author:
			books.remove(book)
			break

	_save_all_books(books)


def _save_all_books(books):
	with open(books_file, 'w') as f:
		for book in books:
			f.write(f"{book['title']},{book['author']},{book['read']}\n")