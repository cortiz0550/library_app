from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """

def menu():
	user_input = input(USER_CHOICE)
	while user_input != 'q':
		user_actions[user_input]()

		user_input = input(USER_CHOICE)


def prompt_add_book():  # Ask for book name and author
	title = input('Enter the title: ').title()
	author = input('Enter the author: ').title()

	database.add_book(title, author)


def list_books():  # Print out all books in a nice format
	library = database.get_all_books()

	print(f'You have {len(library)} book(s) in your library.')
	for book in library:
		book_title = book['title']
		book_author = book['author']
		book_read = "Yes" if book['read'] == "1" else "No"

		print(f'{book_title}, by {book_author}, read: {book_read}')


def prompt_read_book():  # Ask for name and change the read boolean
	title = input('Enter the title: ').title()
	database.mark_book_as_read(title)


def prompt_delete_book():  # Ask for name and delete a book from the master list
	title = input('Enter the title: ').title()
	author = input('Enter the author: ').title()

	database.delete_book(title, author)


user_actions = {
	'a' : prompt_add_book,
	'l' : list_books,
	'r' : prompt_read_book,
	'd' : prompt_delete_book
}

menu()