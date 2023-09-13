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
books = [Book(*row) for row in reader if Book.year => int(2009) or Book.year <= int(2014) ] #same way instead of using for loop like above. Its a list comprehension 




    