
import random
import  os, time
# sample book list
books: list = [
    {"book-ID": "1", "title": "Think Big", "author": "Benjamin", "genre": "biography", "status": "available"},
    {"book-ID": "2", "title": "Forty Rules of Love", "author": "Elif Shafak", "genre": "Novel", "status": "available"},
    ]
# empty user list
users_list: list = []
# admin portal for add and remove books
def admin():
    """FOR ADMIN TASK"""
    adminName = "default"
    password = "default321"
    loginName = input("Enter Admin login name:  ").strip()
    loginPass = input("Enter Admin password: ").strip()
    if  loginName == adminName and loginPass == password:
        print("Admininstrator Mode ")
        print("1. add book")
        print("2. remove book")
        ask = input("Choose (1 or 2): ")
        if ask == "1" :
            # for generating unique book id
            while True:
                is_unique = True
                bookid = str(random.randint(1,9999)) + random.choice(['a','b','c','d','e']) + random.choice(['a','b','c','d','e'])
                is_unique = True  
                for book in books:
                    if bookid == book['book-ID']:  
                        is_unique = False  
                        print(f"rechecking as {bookid}")
                        time.sleep(2)
                        break  
                if is_unique:
                    break
            # adding new book info
            author = input("Enter author name: ").strip().title()
            book_title = input("Enter book title: ").strip().title()
            genre = input("Enter its genre: ").strip().title()
            status = input("press enter if available") or "available"
            if status != "available":
                status = "not available"
            new_book = {"book-ID": bookid , "title": book_title, "author": author, "genre": genre, "status": status}
            books.append(new_book)
            print(f"Book '{new_book} added succesfully.")
        # for removing books
        else: 
            view()
            bookinfo = input("Enter Your Book to remove:  ").strip()
            for book in books:
                if bookinfo == book['book-ID'] or bookinfo == book['title']:
                    books.remove(book)
                    print(f"{book['title']} has been removed successfully")
                    input()

# for viewing books info in library
def view():
    print(f"\033[35mBook ID        :   Information \033[0m")
    for book in books:
        for j in book.values():
            if j != book['title']:
                print(f"{'None' if j is None else j:^15}|" , end= " ")
            else: 
                print(f"{'None' if j is None else j:^20}|" , end= " ")
        
        print("\n\033[32m",'--'*19,'\033[91m','--'*8, '\033[96m','--'*19, sep="", end='\033[0m\n')

# for searching book with relative info this part is made by help of chatgpt
def search():
    print("🔍📕📗📘📙🔍")
    ask = input("Enter Book info: ").lower().strip()  
    book_found = False  
    
    for book in books:
        for info in book.values():
            # Only search if info is a string (skip None or non-string types)
            if isinstance(info, str) and ask in info.lower():  # Convert info to lowercase for comparison
                book_found = True
                # Print the book details if a match is found
                for value in book.values():
                    print(f"{'None' if value is None else value}", end="   ")
                print("\n",'--'*32)  # Print new line after showing book details
                break  # Stop searching once the book is found
    
    if not book_found:
        print("No book found with the given information.")

# for borrowing available books    
def borrow():
    print("🏪 Borrow books, Gain Knowledge 🏪")
    user_view()
    user_id = input("Enter your User ID: ")
    view()
    book_id = input("Enter the Book ID you want to borrow: ")
    
    
    user = next((u for u in users_list if str(u['user-ID']) == user_id), None)
    if user:
        book = next((b for b in books if b['book-ID'] == book_id and b['status'] == 'available'), None)
        if book:
            book['status'] = 'borrowed'
            user['books'].append(book['title'])
            print(f"You have successfully borrowed {book['title']}.")
        else:
            print("Sorry, the book is not available.")
    else:
        print("User not found. Please register first.")

# for returning the borrowed book
def book_return():
    print("🔙 Return Books in safe hands 🌐")
    user_view()
    user_id = input("Enter your User ID: ").strip()
    book_title = input("Enter the Book Title you want to return: ").strip().lower()
    
    user = next((u for u in users_list if str(u['user-ID']) == user_id), None)
    if user:
        borrowed_books_lower = [title.lower() for title in user['books']]
        
        if book_title in borrowed_books_lower:
            original_title = next(title for title in user['books'] if title.lower() == book_title)
            book = next((b for b in books if b['title'].strip().lower() == book_title), None)
            
            if book:
                book['status'] = 'available'
                user['books'].remove(original_title)  # Remove by original case-sensitive title
                print(f"You have successfully returned {original_title}.")
            else:
                print("Book not found in the system.")
        else:
            print("You did not borrow this book or the title is incorrect.")
    else:
        print("User not found. Please register first.")
        
# for viewing and adding users   
def users():
    print("1. add a user")
    print("2. user list")
    ask = input("Enter Your choice 1-2 :").strip()
    if ask == "1":
        add_users()
    else:
        user_view()

def user_view():
    for user in users_list:
            print(f"User-ID: {user['user-ID']}, Name: {user['name']}, Borrowed Books: {user['books']}")
    
def menu():
    add_users()
    while True:
        input(":--enter--:")
        os.system("cls")
        for again in range(1):
            print("\t\033[34m 📚 LIBRARY MANAGEMENT SYSTEM 📑 \033[0m")
            a = '-'
            print(f"\t   {a*27}")
            print("1. Book Gallery")
            print("2. Search Book")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. Users")
            print("6. Exit ")
            ask = input("Enter your Choice (1-6) or 'admin': ").strip().lower()
            if ask == "1":
                view()
            elif ask == 'admin':
                admin()
            elif ask == "2":
                search()
            elif ask == "3":
                borrow()
            elif ask == "4":
                book_return()
            elif ask == "5":
                users()
            else:
                again = input("Do you want to exit? ").strip().lower()
                if again in ["yes", 'y', "okay", "exit"]:
                    exit()
                else:
                    continue



def add_users():
    print("Library Registration")
    username :str = input("What is your Name?")
    userID: str= random.randint(111,999)
    row = {"user-ID": userID,"name": username, "books": []}
    users_list.append(row)
    print(f"User {username} registered with User ID: {userID}")

menu()



