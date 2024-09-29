books:list = []
users:list = []

books.append({"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "status": "Available"})
books.append({"id": 2, "title": "1984", "author": "George Orwell", "genre": "Dystopian", "status": "Checked Out"})
books.append({"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic", "status": "Available"})

users.append({"id": 1, "name": "Alice", "borrowed_books": []})
users.append({"id": 2, "name": "Bob", "borrowed_books": []})
def add_books(id:int, title:str, author:str, genre:str,status:str) -> dict:
    book: dict = {"id":id, "title":title, "author":author, "genre":genre, "status": status}
    return  book

def view_all_books():
    print("\nAll Books:")
    for book in books:
        print(f"{book['id']} {book['title']} by {book['author']} ({book['status']})")

def search_books():
    search_type = input("Search by (1) Title, (2) Author, (3) Genre: ")
    query = input("Enter search term: ").lower()

    print("\nSearch Results:")
    for book in books:
        if (search_type == "1" and query in book["title"].lower()) or \
           (search_type == "2" and query in book["author"].lower()) or \
           (search_type == "3" and query in book["genre"].lower()):
            print(f"{book['id']}. \"{book['title']}\" by {book['author']} ({book['status']})")

def add_user(id:int, user_name:str, borrowed_books:list) -> dict:
    user: dict = {"id":id,"user_name":user_name, "borrowed_books":borrowed_books}
    return user

def view_users():
    print("\nAll Users:")
    for user in users:
        print(f"User ID: {user['id']}, Name: {user['name']}, Borrowed Books: {', '.join(user['borrowed_books']) or 'None'}")

def view_checked_out_books() -> None:
    print("\nChecked Out Books:")
    for book in books:
        if book["status"] == "Checked Out":
            print(f"{book['id']}. \"{book['title']}\" by {book['author']}")

def borrow_book():
    user_id = int(input("Enter your User ID: "))
    book_id = int(input("Enter the Book ID to borrow: "))

    user = next((user for user in users if user["id"] == user_id), None)
    book = next((book for book in books if book["id"] == book_id), None)

    if user and book:
        if book["status"] == "Available":
            book["status"] = "Checked Out"
            user["borrowed_books"].append(book["title"])
            print(f"You have borrowed \"{book['title']}\".")
        else:
            print(f"Sorry, the book \"{book['title']}\" is currently checked out.")
    else:
        print("Invalid User ID or Book ID.")

def return_book():
    user_id = int(input("Enter your User ID: "))
    book_id = int(input("Enter the Book ID to return: "))

    user = next((user for user in users if user["id"] == user_id), None)
    book = next((book for book in books if book["id"] == book_id), None)

    if user and book:
        if book["title"] in user["borrowed_books"]:
            book["status"] = "Available"
            user["borrowed_books"].remove(book["title"])
            print(f"You have returned \"{book['title']}\".")
        else:
            print("You haven't borrowed this book.")
    else:
        print("Invalid User ID or Book ID.")


def main_menu():
    while True:
        print("\nWelcome to the Community Library System!")
        print("----------------------------------------")
        print("1. View all books")
        print("2. View available books")
        print("3. View checked-out books")
        print("4. Search for a book")
        print("5. Borrow a book")
        print("6. Return a book")
        print("7. View all users")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            view_all_books()
        elif choice == "2":
            search_books()
        elif choice == "3":
            borrow_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            view_users()
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

main_menu()

