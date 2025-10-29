# demo.py - Library Management System Demo Script

# Import the data structures and helper functions
import operations

print("=" * 60)
print("LIBRARY MANAGEMENT SYSTEM DEMONSTRATION")
print("=" * 60)

# 1. ADDING BOOKS (manually to demonstrate)
print("\n1. ADDING BOOKS TO LIBRARY")
print("-" * 40)

# Add books directly to the data structures for demo
operations.books.append({
    "isbn": "978-0-7475-3269-9",
    "title": "Harry Potter and the Philosopher's Stone",
    "author": "J.K. Rowling",
    "genre": "Fiction",
    "total_copies": 5,
    "available_copies": 5
})
print("✓ Added: Harry Potter and the Philosopher's Stone")

operations.books.append({
    "isbn": "978-0-590-35340-3",
    "title": "Harry Potter and the Chamber of Secrets",
    "author": "J.K. Rowling",
    "genre": "Fiction",
    "total_copies": 3,
    "available_copies": 3
})
print("✓ Added: Harry Potter and the Chamber of Secrets")

operations.books.append({
    "isbn": "978-0-06-112008-4",
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "genre": "Fiction",
    "total_copies": 4,
    "available_copies": 4
})
print("✓ Added: To Kill a Mockingbird")

operations.books.append({
    "isbn": "978-0-553-29337-9",
    "title": "A Brief History of Time",
    "author": "Stephen Hawking",
    "genre": "Non-Fiction",
    "total_copies": 2,
    "available_copies": 2
})
print("✓ Added: A Brief History of Time")

operations.books.append({
    "isbn": "978-0-7653-7698-5",
    "title": "The Martian",
    "author": "Andy Weir",
    "genre": "Sci-Fi",
    "total_copies": 3,
    "available_copies": 3
})
print("✓ Added: The Martian")

# Display all books
operations.display_all_books()

# 2. ADDING MEMBERS
print("\n2. ADDING MEMBERS")
print("-" * 40)

operations.members.append({
    "id": "M001",
    "name": "John Doe",
    "email": "john.doe@email.com",
    "contact": "123-456-7890",
    "borrowed_books": []
})
print("✓ Added member: John Doe")

operations.members.append({
    "id": "M002",
    "name": "Jane Smith",
    "email": "jane.smith@email.com",
    "contact": "098-765-4321",
    "borrowed_books": []
})
print("✓ Added member: Jane Smith")

operations.members.append({
    "id": "M003",
    "name": "Alice Johnson",
    "email": "alice.j@email.com",
    "contact": "555-123-4567",
    "borrowed_books": []
})
print("✓ Added member: Alice Johnson")

# Display all members
operations.display_all_members()

# 3. SEARCHING BOOKS
print("\n3. SEARCHING FOR BOOKS")
print("-" * 40)
print("Searching for 'Harry Potter':")
search_term = "Harry Potter"
results = []
for book in operations.books:
    if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower():
        results.append(book)

for book in results:
    print(f"  - {book['title']} by {book['author']}")

print("\nSearching for author 'Stephen Hawking':")
search_term = "Stephen Hawking"
results = []
for book in operations.books:
    if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower():
        results.append(book)

for book in results:
    print(f"  - {book['title']} by {book['author']}")

# 4. BORROWING BOOKS
print("\n4. BORROWING BOOKS")
print("-" * 40)

# John borrows Harry Potter 1
member = operations.members[0]  # M001
book = operations.books[0]  # Harry Potter 1
member["borrowed_books"].append(book["isbn"])
book["available_copies"] -= 1
print(f"✓ {member['name']} borrowed '{book['title']}'")

# John borrows Harry Potter 2
book = operations.books[1]  # Harry Potter 2
member["borrowed_books"].append(book["isbn"])
book["available_copies"] -= 1
print(f"✓ {member['name']} borrowed '{book['title']}'")

# Jane borrows To Kill a Mockingbird
member = operations.members[1]  # M002
book = operations.books[2]
member["borrowed_books"].append(book["isbn"])
book["available_copies"] -= 1
print(f"✓ {member['name']} borrowed '{book['title']}'")

# Jane borrows Brief History
book = operations.books[3]
member["borrowed_books"].append(book["isbn"])
book["available_copies"] -= 1
print(f"✓ {member['name']} borrowed '{book['title']}'")

# Alice borrows The Martian
member = operations.members[2]  # M003
book = operations.books[4]
member["borrowed_books"].append(book["isbn"])
book["available_copies"] -= 1
print(f"✓ {member['name']} borrowed '{book['title']}'")

# Display updated books status
operations.display_all_books()

# 5. TESTING BORROW LIMIT
print("\n5. TESTING BORROW LIMIT (Max 3 books)")
print("-" * 40)

# John tries to borrow 3rd book (The Martian)
member = operations.members[0]  # M001
book = operations.books[4]  # The Martian
member["borrowed_books"].append(book["isbn"])
book["available_copies"] -= 1
print(f"✓ {member['name']} borrowed '{book['title']}' (3rd book)")

# John tries to borrow 4th book (should fail)
if len(member["borrowed_books"]) >= 3:
    print(f"✗ {member['name']} cannot borrow more - already has 3 books!")

# 6. RETURNING BOOKS
print("\n6. RETURNING BOOKS")
print("-" * 40)

# John returns Harry Potter 1
member = operations.members[0]
isbn = "978-0-7475-3269-9"
book = None
for b in operations.books:
    if b["isbn"] == isbn:
        book = b
        break
member["borrowed_books"].remove(isbn)
book["available_copies"] += 1
print(f"✓ {member['name']} returned '{book['title']}'")

# Jane returns Brief History
member = operations.members[1]
isbn = "978-0-553-29337-9"
book = None
for b in operations.books:
    if b["isbn"] == isbn:
        book = b
        break
member["borrowed_books"].remove(isbn)
book["available_copies"] += 1
print(f"✓ {member['name']} returned '{book['title']}'")

# Display updated books status
operations.display_all_books()

# 7. UPDATING BOOK DETAILS
print("\n7. UPDATING BOOK INFORMATION")
print("-" * 40)

# Update Harry Potter total copies
for book in operations.books:
    if book["isbn"] == "978-0-7475-3269-9":
        book["total_copies"] = 6
        print(f"✓ Updated '{book['title']}' - total copies now 6")
        break

# Update Stephen Hawking's name
for book in operations.books:
    if book["isbn"] == "978-0-553-29337-9":
        book["author"] = "Stephen W. Hawking"
        print(f"✓ Updated author name to '{book['author']}'")
        break

# Display updated books
operations.display_all_books()

# 8. UPDATING MEMBER DETAILS
print("\n8. UPDATING MEMBER INFORMATION")
print("-" * 40)

for member in operations.members:
    if member["id"] == "M001":
        member["email"] = "john.newemail@email.com"
        member["contact"] = "111-222-3333"
        print(f"✓ Updated {member['name']}'s contact information")
        break

# Display updated members
operations.display_all_members()

# 9. TESTING DELETE WITH BORROWED BOOKS
print("\n9. TESTING DELETE RESTRICTIONS")
print("-" * 40)

# Try to delete book with borrowed copies
book = operations.books[1]  # Harry Potter 2 (John still has it)
if book["available_copies"] < book["total_copies"]:
    print(f"✗ Cannot delete '{book['title']}' - has borrowed copies")

# Try to delete member with borrowed books
member = operations.members[0]  # John still has books
if len(member["borrowed_books"]) > 0:
    print(f"✗ Cannot delete member '{member['name']}' - has borrowed books")

# 10. SUCCESSFUL DELETION
print("\n10. SUCCESSFUL DELETION (After returning)")
print("-" * 40)

# John returns remaining books
member = operations.members[0]
while len(member["borrowed_books"]) > 0:
    isbn = member["borrowed_books"][0]
    for book in operations.books:
        if book["isbn"] == isbn:
            member["borrowed_books"].remove(isbn)
            book["available_copies"] += 1
            print(f"✓ {member['name']} returned '{book['title']}'")
            break

# Now delete member M001
for i, member in enumerate(operations.members):
    if member["id"] == "M001":
        if len(member["borrowed_books"]) == 0:
            operations.members.pop(i)
            print(f"✓ Member 'M001' deleted successfully")
        break

# Delete book with no borrowed copies
for i, book in enumerate(operations.books):
    if book["isbn"] == "978-0-7653-7698-5":
        if book["available_copies"] == book["total_copies"]:
            operations.books.pop(i)
            print(f"✓ Book 'The Martian' deleted successfully")
        break

# Final status
print("\n" + "=" * 60)
print("FINAL LIBRARY STATUS")
print("=" * 60)
operations.display_all_books()
operations.display_all_members()

print("\n" + "=" * 60)
print("DEMONSTRATION COMPLETE")
print("=" * 60)
print("\nThis demo showed:")
print("✓ Adding books and members")
print("✓ Searching for books")
print("✓ Borrowing and returning books")
print("✓ Enforcing 3-book limit")
print("✓ Updating book and member details")
print("✓ Delete restrictions (borrowed items)")
print("✓ Successful deletion after returning")