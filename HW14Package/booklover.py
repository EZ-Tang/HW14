# Eric Tang
# 7/4/2022
# DS 5100

import numpy as np
import pandas as pd


"""BookLover class which records a user's name, email, favorite genre, number of books, and book_list. 
The methods are add_book(), has_read(), and num_books_read(), and fav_books()."""
class BookLover:
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    def add_book(self, book_name, rating):
        if book_name not in self.book_list['book_name'].values.tolist():
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            print(book_name + " is already in the list!")

    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]