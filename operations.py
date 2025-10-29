# operations.py - Library Management System Core Functions

# Data Structures
books = []  # List to store book dictionaries
members = []  # List to store member dictionaries
VALID_GENRES = ("Fiction", "Non-Fiction", "Sci-Fi")  # Tuple of valid genres


# ===== BOOK OPERATIONS =====

def add_book():
    """Add a new book to the library system"""
    print("\n--- ADD NEW BOOK ---")
    isbn = input("Enter ISBN: ").strip()

    # Check if ISBN is unique
    for book in books:
        if book["isbn"] == isbn:
            print("Error: ISBN already exists")
            return

    title = input("Enter Title: ").strip()
    author = input("Enter Author: ").strip()
    genre = input(f"Enter Genre {VALID_GENRES}: ").strip()

    # Check if genre is valid
    if genre not in VALID_GENRES:
        print(f"Error: Genre must be one of {VALID_GENRES}")
        return

    try:
        total_copies = int(input("Enter Total Copies: ").strip())
    except ValueError:
        print("Error: Total copies must be a number")
        return

    # Create book dictionary
    new_book = {
        "isbn": isbn,
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "available_copies": total_copies
    }

    books.append(new_book)
    print(f"✓ Book '{title}' added successfully")


def search_books():
    """Search books by title or author"""
    print("\n--- SEARCH BOOKS ---")
    search_term = input("Enter title or author to search: ").strip().lower()

    results = []
    for book in books:
        if search_term in book["title"].lower() or search_term in book["author"].lower():
            results.append(book)

    if results:
        print(f"\n✓ Found {len(results)} book(s):")
        for book in results:
            print(f"  ISBN: {book['isbn']}, Title: {book['title']}, Author: {book['author']}, "
                  f"Genre: {book['genre']}, Available: {book['available_copies']}/{book['total_copies']}")
    else:
        print("✗ No books found matching your search")


def update_book():
    """Update book details"""
    print("\n--- UPDATE BOOK ---")
    isbn = input("Enter ISBN of book to update: ").strip()

    book_found = None
    for book in books:
        if book["isbn"] == isbn:
            book_found = book
            break

    if not book_found:
        print("Error: Book not found")
        return

    print("Leave blank to keep current value")
    title = input(f"New Title (current: {book_found['title']}): ").strip()
    author = input(f"New Author (current: {book_found['author']}): ").strip()
    genre = input(f"New Genre (current: {book_found['genre']}): ").strip()
    total_copies = input(f"New Total Copies (current: {book_found['total_copies']}): ").strip()

    if title:
        book_found["title"] = title
    if author:
        book_found["author"] = author
    if genre:
        if genre in VALID_GENRES:
            book_found["genre"] = genre
        else:
            print(f"Error: Genre must be one of {VALID_GENRES}")
            return
    if total_copies:
        try:
            book_found["total_copies"] = int(total_copies)
        except ValueError:
            print("Error: Total copies must be a number")
            return

    print(f"✓ Book with ISBN {isbn} updated successfully")


def delete_book():
    """Delete a book only if no copies are borrowed"""
    print("\n--- DELETE BOOK ---")
    isbn = input("Enter ISBN of book to delete: ").strip()

    for book in books:
        if book["isbn"] == isbn:
            if book["available_copies"] < book["total_copies"]:
                print("Error: Cannot delete book with borrowed copies")
                return

            confirm = input(f"Delete '{book['title']}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                books.remove(book)
                print(f"✓ Book with ISBN {isbn} deleted successfully")
            else:
                print("✗ Deletion cancelled")
            return

    print("Error: Book not found")


# ===== MEMBER OPERATIONS =====

def add_member():
    """Add a new member to the library system"""
    print("\n--- ADD NEW MEMBER ---")
    member_id = input("Enter Member ID: ").strip()

    # Check if member ID is unique
    for member in members:
        if member["id"] == member_id:
            print("Error: Member ID already exists")
            return

    name = input("Enter Name: ").strip()
    email = input("Enter Email: ").strip()
    contact = input("Enter Contact: ").strip()

    # Create member dictionary
    new_member = {
        "id": member_id,
        "name": name,
        "email": email,
        "contact": contact,
        "borrowed_books": []
    }

    members.append(new_member)
    print(f"✓ Member '{name}' added successfully")


def update_member():
    """Update member details"""
    print("\n--- UPDATE MEMBER ---")
    member_id = input("Enter Member ID to update: ").strip()

    member_found = None
    for member in members:
        if member["id"] == member_id:
            member_found = member
            break

    if not member_found:
        print("Error: Member not found")
        return

    print("Leave blank to keep current value")
    name = input(f"New Name (current: {member_found['name']}): ").strip()
    email = input(f"New Email (current: {member_found['email']}): ").strip()
    contact = input(f"New Contact (current: {member_found['contact']}): ").strip()

    if name:
        member_found["name"] = name
    if email:
        member_found["email"] = email
    if contact:
        member_found["contact"] = contact

    print(f"✓ Member with ID {member_id} updated successfully")


def delete_member():
    """Delete a member only if they have no borrowed books"""
    print("\n--- DELETE MEMBER ---")
    member_id = input("Enter Member ID to delete: ").strip()

    for member in members:
        if member["id"] == member_id:
            if len(member["borrowed_books"]) > 0:
                print("Error: Cannot delete member with borrowed books")
                return

            confirm = input(f"Delete member '{member['name']}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                members.remove(member)
                print(f"✓ Member with ID {member_id} deleted successfully")
            else:
                print("✗ Deletion cancelled")
            return

    print("Error: Member not found")


# ===== BORROW/RETURN OPERATIONS =====

def borrow_book():
    """Allow a member to borrow a book"""
    print("\n--- BORROW BOOK ---")
    member_id = input("Enter Member ID: ").strip()

    # Find member
    member = None
    for m in members:
        if m["id"] == member_id:
            member = m
            break

    if not member:
        print("Error: Member not found")
        return

    # Check if member already has 3 books
    if len(member["borrowed_books"]) >= 3:
        print("Error: Member has already borrowed 3 books")
        return

    isbn = input("Enter Book ISBN: ").strip()

    # Find book
    book = None
    for b in books:
        if b["isbn"] == isbn:
            book = b
            break

    if not book:
        print("Error: Book not found")
        return

    # Check if book is available
    if book["available_copies"] <= 0:
        print("Error: No copies available")
        return

    # Borrow the book
    member["borrowed_books"].append(isbn)
    book["available_copies"] -= 1
    print(f"✓ Book '{book['title']}' borrowed successfully by {member['name']}")


def return_book():
    """Allow a member to return a borrowed book"""
    print("\n--- RETURN BOOK ---")
    member_id = input("Enter Member ID: ").strip()

    # Find member
    member = None
    for m in members:
        if m["id"] == member_id:
            member = m
            break

    if not member:
        print("Error: Member not found")
        return

    isbn = input("Enter Book ISBN: ").strip()

    # Check if member has borrowed this book
    if isbn not in member["borrowed_books"]:
        print("Error: Member has not borrowed this book")
        return

    # Find book
    book = None
    for b in books:
        if b["isbn"] == isbn:
            book = b
            break

    if not book:
        print("Error: Book not found")
        return

    # Return the book
    member["borrowed_books"].remove(isbn)
    book["available_copies"] += 1
    print(f"✓ Book '{book['title']}' returned successfully by {member['name']}")


# ===== DISPLAY FUNCTIONS =====

def display_all_books():
    """Display all books in the library"""
    if not books:
        print("\n✗ No books in the library")
        return

    print("\n=== ALL BOOKS ===")
    for book in books:
        print(f"ISBN: {book['isbn']}, Title: {book['title']}, Author: {book['author']}, "
              f"Genre: {book['genre']}, Available: {book['available_copies']}/{book['total_copies']}")


def display_all_members():
    """Display all members"""
    if not members:
        print("\n✗ No members registered")
        return

    print("\n=== ALL MEMBERS ===")
    for member in members:
        print(f"ID: {member['id']}, Name: {member['name']}, Email: {member['email']}, "
              f"Contact: {member['contact']}, Borrowed Books: {len(member['borrowed_books'])}")


# ===== MAIN MENU =====

def show_menu():
    """Display the main menu"""
    print("\n" + "=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("=" * 60)
    print("\n📚 BOOK OPERATIONS:")
    print("  1. Add New Book")
    print("  2. Search Books")
    print("  3. Update Book")
    print("  4. Delete Book")
    print("  5. Display All Books")
    print("\n👥 MEMBER OPERATIONS:")
    print("  6. Add New Member")
    print("  7. Update Member")
    print("  8. Delete Member")
    print("  9. Display All Members")
    print("\n📖 BORROW/RETURN OPERATIONS:")
    print("  10. Borrow Book")
    print("  11. Return Book")
    print("\n  0. Exit System")
    print("=" * 60)


def main():
    """Main interactive program"""
    print("\n🎓 Welcome to Library Management System!")
    print(f"Valid Genres: {', '.join(VALID_GENRES)}")

    while True:
        show_menu()
        choice = input("\nEnter your choice (0-11): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            search_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            display_all_books()
        elif choice == "6":
            add_member()
        elif choice == "7":
            update_member()
        elif choice == "8":
            delete_member()
        elif choice == "9":
            display_all_members()
        elif choice == "10":
            borrow_book()
        elif choice == "11":
            return_book()
        elif choice == "0":
            print("\n" + "=" * 60)
            print("Thank you for using Library Management System!")
            print("Goodbye! 👋")
            print("=" * 60)
            break
        else:
            print("\n✗ Invalid choice! Please enter a number between 0-11.")

        input("\nPress Enter to continue...")


# ===== RUN PROGRAM =====

if __name__ == "__main__":
    main()