import sqlite3

# Connect to database (it will create one if it doesn’t exist)
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create table if it doesn’t exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    isbn TEXT
)
""")
conn.commit()

def add_book():
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    year = input("Enter Published Year: ")
    isbn = input("Enter ISBN: ")

    cursor.execute("INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)", 
                   (title, author, year, isbn))
    conn.commit()
    print("✅ Book added successfully!\n")

def view_books():
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    if rows:
        print("\n📚 All Books:")
        for row in rows:
            print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Year: {row[3]}, ISBN: {row[4]}")
    else:
        print("No books found.\n")

def search_book():
    keyword = input("Enter title or author to search: ")
    cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", 
                   ('%' + keyword + '%', '%' + keyword + '%'))
    rows = cursor.fetchall()
    if rows:
        print("\n🔍 Search Results:")
        for row in rows:
            print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Year: {row[3]}, ISBN: {row[4]}")
    else:
        print("No matching books found.\n")

def delete_book():
    view_books()
    book_id = input("\nEnter the Book ID to delete: ")
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    print("❌ Book deleted successfully!\n")

def main():
    while True:
        print("\n====== 📚 Library Management System ======")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            print("👋 Exiting... Have a nice day!")
            break
        else:
            print("Invalid choice! Try again.\n")

    conn.close()

if __name__ == "__main__":
    main()
