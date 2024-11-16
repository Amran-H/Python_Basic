""""
Project: Library Management System
Student: Amran Hossain 

This project is a simple Library Management System. 
It allows users to manage a collection of books through the following features:
1. Display Books: View all available books in the library.
2. Borrow a Book: Borrow a book, updating its availability.
3. Return a Book: Return a borrowed book to the collection.
4. Add a New Book: Add new books to the library.
5. Remove a Book: Remove books to the library.
6. Save and Load Data: Data is saved to a file ('books.txt') for persistence across sessions.
"""

# Initial list of books
books = ["Accounting", "Physics", "Marketing", "Chemistry", "The Alchemist"]

# Display available books
def display_books():
    print("\nAvailable Books:")
    for book in books:
        print(f"- {book}")

# Borrow a book
def borrow_book():
    book = input("\nEnter the name of the book you want to borrow: ")
    if book in books:
        books.remove(book)
        print(f"You have borrowed '{book}'.")
    else:
        print("Sorry, the book is not available.")

# Return a book
def return_book():
    book = input("\nEnter the name of the book you want to return: ")
    books.append(book)
    print(f"Thank you for returning '{book}'.")

# Add a new book
def add_book():
    book = input("\nEnter the name of the book to add: ")
    books.append(book)
    print(f"'{book}' has been added to the library.")
    
# Remove a book
def remove_book():
    book = input("\nEnter the name of the book you want to remove: ")
    if book in books:
        books.remove(book)
        print(f"You have removed '{book}'.")
    else:
        print("Sorry, the book is not available.")

# Save books to a file
def save_books_to_file():
    with open("books.txt", "w") as file:
        for book in books:
            file.write(book + "\n")
    print("\nBooks have been saved to 'books.txt'.")

# Function to load books from a file
def load_books_from_file():
    try:
        with open("books.txt", "r") as file:
            global books
            books = [line.strip() for line in file]
        print("\nBooks have been loaded from 'books.txt'.")
    except FileNotFoundError:
        print("\nNo saved file found. Starting with the default list.")

# Main program
def main():
    load_books_from_file()
    while True:
        print("\nLibrary Menu:")
        print("1. Display Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Add a New Book")
        print("5. Remove a Book")
        print("6. Save and Exit")

        choice = input("\nEnter your choice: ")
        if choice == "1":
            display_books()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            add_book()
        elif choice == "5":
            remove_book()
        elif choice == "6":
            save_books_to_file()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
