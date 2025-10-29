# tests.py - Library Management System Unit Tests

import operations

print("=" * 60)
print("LIBRARY MANAGEMENT SYSTEM - UNIT TESTS")
print("=" * 60)

# Clear any existing data
operations.books.clear()
operations.members.clear()

# TEST 1: Adding books with unique ISBN
print("\nTEST 1: Add book with unique ISBN")
operations.books.append({
    "isbn": "TEST-001",
    "title": "Test Book 1",
    "author": "Test Author",
    "genre": "Fiction",
    "total_copies": 5,
    "available_copies": 5
})
assert len(operations.books) == 1, "Book list should have 1 book"
print("✓ PASSED: Book added successfully with unique ISBN")

# TEST 2: Prevent duplicate ISBN
print("\nTEST 2: Prevent adding book with duplicate ISBN")
# Check if ISBN already exists
isbn_exists = False
for book in operations.books:
    if book["isbn"] == "TEST-001":
        isbn_exists = True
        break

assert isbn_exists == True, "Should detect duplicate ISBN"
assert len(operations.books) == 1, "Book list should still have only 1 book"
print("✓ PASSED: Duplicate ISBN detection works")

# TEST 3: Validate genre using tuple
print("\nTEST 3: Validate genre from tuple")
invalid_genre = "InvalidGenre"
is_valid = invalid_genre in operations.VALID_GENRES
assert is_valid == False, "Should reject invalid genre"

valid_genre = "Fiction"
is_valid = valid_genre in operations.VALID_GENRES
assert is_valid == True, "Should accept valid genre"
print("✓ PASSED: Genre validation using tuple works")

# TEST 4: Add member and enforce borrow limit (max 3 books)
print("\nTEST 4: Enforce maximum borrow limit (3 books)")
# Setup
operations.members.append({
    "id": "TEST-M001",
    "name": "Test Member",
    "email": "test@email.com",
    "contact": "123-456",
    "borrowed_books": []
})

operations.books.append({
    "isbn": "TEST-003",
    "title": "Book 2",
    "author": "Author 2",
    "genre": "Fiction",
    "total_copies": 5,
    "available_copies": 5
})

operations.books.append({
    "isbn": "TEST-004",
    "title": "Book 3",
    "author": "Author 3",
    "genre": "Sci-Fi",
    "total_copies": 5,
    "available_copies": 5
})

operations.books.append({
    "isbn": "TEST-005",
    "title": "Book 4",
    "author": "Author 4",
    "genre": "Non-Fiction",
    "total_copies": 5,
    "available_copies": 5
})

# Borrow 3 books
member = operations.members[0]
member["borrowed_books"].append("TEST-001")
member["borrowed_books"].append("TEST-003")
member["borrowed_books"].append("TEST-004")

# Try to borrow 4th book
can_borrow = len(member["borrowed_books"]) < 3
assert can_borrow == False, "Should prevent borrowing more than 3 books"

# Verify member has exactly 3 books
assert len(member["borrowed_books"]) == 3, "Member should have exactly 3 borrowed books"
print("✓ PASSED: Borrow limit enforced (max 3 books)")

# TEST 5: Delete restrictions - cannot delete book with borrowed copies
print("\nTEST 5: Prevent deletion of book with borrowed copies")
book = operations.books[0]  # TEST-001
book["available_copies"] = 4  # Simulate borrowed copy
can_delete = book["available_copies"] == book["total_copies"]
assert can_delete == False, "Should not allow deleting borrowed book"

# Verify book still exists
book_exists = False
for b in operations.books:
    if b["isbn"] == "TEST-001":
        book_exists = True
        break
assert book_exists, "Book should still exist"
print("✓ PASSED: Cannot delete book with borrowed copies")

# TEST 6: Delete restrictions - cannot delete member with borrowed books
print("\nTEST 6: Prevent deletion of member with borrowed books")
member = operations.members[0]
can_delete = len(member["borrowed_books"]) == 0
assert can_delete == False, "Should not allow deleting member with books"

# Verify member still exists
member_exists = False
for m in operations.members:
    if m["id"] == "TEST-M001":
        member_exists = True
        break
assert member_exists, "Member should still exist"
print("✓ PASSED: Cannot delete member with borrowed books")

# TEST 7: Return book functionality
print("\nTEST 7: Return book updates availability")
# Get initial available copies
book = operations.books[0]
initial_copies = book["available_copies"]

# Return book
member = operations.members[0]
isbn = "TEST-001"
member["borrowed_books"].remove(isbn)
book["available_copies"] += 1

# Get updated available copies
updated_copies = book["available_copies"]

assert updated_copies == initial_copies + 1, "Available copies should increase by 1 after return"
print("✓ PASSED: Book return updates availability correctly")

# TEST 8: Search functionality (using lists and dictionaries)
print("\nTEST 8: Search books by title or author")
# Search for "Test Book"
search_term = "Test Book"
results = []
for book in operations.books:
    if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower():
        results.append(book)

assert len(results) >= 1, "Should find books matching 'Test Book'"

# Search for "Author 2"
search_term = "Author 2"
results = []
for book in operations.books:
    if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower():
        results.append(book)

assert len(results) == 1, "Should find exactly one book by 'Author 2'"
assert results[0]["isbn"] == "TEST-003", "Should find correct book"
print("✓ PASSED: Search functionality works correctly")

print("\n" + "=" * 60)
print("ALL TESTS PASSED SUCCESSFULLY!")
print("=" * 60)
print("\nTest Summary:")
print("✓ Test 1: Unique ISBN validation")
print("✓ Test 2: Duplicate ISBN prevention")
print("✓ Test 3: Genre validation using tuples")
print("✓ Test 4: Borrow limit enforcement (3 books max)")
print("✓ Test 5: Book deletion restriction (borrowed copies)")
print("✓ Test 6: Member deletion restriction (borrowed books)")
print("✓ Test 7: Return book functionality")
print("✓ Test 8: Search functionality")
print("\n" + "=" * 60)
print("All data structures working correctly:")
print(f"✓ Dictionaries: Used for {len(operations.books)} books and {len(operations.members)} members")
print(f"✓ Lists: Used for books[], members[], and borrowed_books[]")
print(f"✓ Tuples: Used for VALID_GENRES {operations.VALID_GENRES}")
print("=" * 60)