from multiprocessing.sharedctypes import Value
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        testBook1 = BookLover("Bobby Bo", "bob@aol.com", "fantasy")
        testBook1.add_book("Bob and the Bobilicious Berry", 5)
        self.assertTrue("Bob and the Bobilicious Berry" in testBook1.book_list['book_name'].values, "(Test 1) Book not in booklover!")

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        testBook2Actual = BookLover("Bobby Bo", "bob@aol.com", "fantasy")
        testBook2Actual.add_book("Bob and the Bobilicious Berry", 5)
        testBook2Actual.add_book("Bob and the Bobilicious Berry", 5)

        testBook2Expected = BookLover("Bobby Bo", "bob@aol.com", "fantasy")
        testBook2Expected.add_book("Bob and the Bobilicious Berry", 5)
        self.assertEqual(testBook2Actual.book_list['book_name'].values, testBook2Expected.book_list['book_name'].values, "(Test 2) Book has multiple occurences of the same book!")

    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        testBook3 = BookLover("Bobby Bo", "bob@aol.com", "fantasy")
        testBook3.add_book("Bob and the Bobilicious Berry", 5)

        self.assertTrue(testBook3.has_read("Bob and the Bobilicious Berry"), "(Test 3) Book has not been read! (Expected True)")
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        testBook4 = BookLover("Bobby Bo", "bob@aol.com", "fantasy")
        testBook4.add_book("Bob and the Bobilicious Berry", 5)

        self.assertFalse(testBook4.has_read("Joe and the Joe's Mom"), "(Test 4) Book has been read! (Expected False)")
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        testBook5 = BookLover("Bobby Bo", "bob@aol.com", "fantasy")
        testBook5.add_book("Carl and the Colored Crayon", 2)
        testBook5.add_book("John's Pants", 5)
        testBook5.add_book("A Book Which Booklovers Love <3", 4)
        testBook5.add_book("July Fourth's Fourth Edition of a Fourth Book", 1)
        testBook5.add_book("Another Overpriced Tech Book, College Edition", 3)

        self.assertEqual(testBook5.num_books_read(), 5, "(Test 5) Book is incorrectly adding in new books!")
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        testBook6 = BookLover("Bobby Bo", "bob@aol.com", "fantasy")
        testBook6.add_book("Carl and the Colored Crayon", 2)
        testBook6.add_book("John's Pants", 5)
        testBook6.add_book("A Book Which Booklovers Love <3", 4)
        testBook6.add_book("July Fourth's Fourth Edition of a Fourth Book", 1)
        testBook6.add_book("Another Overpriced Tech Book, College Edition", 3)

        self.assertTrue(all(i > 3 for i in testBook6.fav_books().book_rating), "(Test 6) Book is incorrectly rating favorite books!")
if __name__ == '__main__':
    unittest.main(verbosity=3)