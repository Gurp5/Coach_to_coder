import csv 
from collections import namedtuple

# books = [] 

Book = namedtuple("Book", "name author user_rating reviews price year genre")

with open("bestsellers_with_categories.csv", "r") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader)
    # for row in reader:
        #new_book = {}
        # new_book["name"] = row[0]
        # new_book["author"] = row[1]
        # new_book["user_rating"] = row[2]
        # new_book["reviews"] = row[3]
        # new_book["price"] = row[4] 
        # new_book["year"] = row[5]
        # new_book["genre"] = row[6]
        # new_book = Book(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) Can be done like in row 21 below much easier!
        # new_book = Book(*row)
        # books.append(new_book)
    books = [Book(*row) for row in reader]

# Let's practice looping through and processing the data.

# 1 Create a list with all of the bestsellers from 2009 to 2012!

# filtered_bestsellers = []
# for book in books:
#     if int(book.year) >= int(2009) and int(book.year) <= int(2012):
#         filtered_bestsellers.append(book)

# for filtered in filtered_bestsellers:
#     print(filtered.name + " " + filtered.year)

# print(len(filtered_bestsellers))

# list comprehnsion way of above

filtered_bestsellers = [book for book in books if int(book.year) >= int(2009) and int(book.year) <= int(2012)]

# print(filtered_bestsellers)


# 2 How expensive is the most expensive book?

most_expensive_book = books[0]
for book in  books:
    if(int(book.price) > int(most_expensive_book.price)):
        most_expensive_book = book 

# print(most_expensive_book.price)



# 3 Create a list with all books whose author has the first name George!

# george_books = []

# for book in books:
#     if("George" in book.author):
#         george_books.append(book)

# print(george_books)
# print(len(george_books))

george_books = [book for book in books if "George" in book.author]

# print(george_books)
# print(len(george_books))


#same way instead of using for loop like above. Its a list comprehension 

modified_books = []

for book in books:
    british_book_price = Book(
        book.name, 
        book.author, 
        book.user_rating, 
        book.reviews, 
        float(book.price)*0.79, 
        book.year, 
        book.genre
        )
    modified_books.append(british_book_price)

print(modified_books)
print(len(modified_books))

with open("bestsellers_british_book_price.csv", "w") as british_csvfile:
    writer =  csv.writer(british_csvfile, quoting=csv.QUOTE_ALL)
    writer.writerow(Book("Name", "Author", "User Rating", "Reviews", "Price", "Year", "Genre"))
    for book in modified_books:
        writer.writerow(book)



    