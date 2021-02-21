# 1105. Filling Bookcase Shelves
# https://leetcode.com/problems/filling-bookcase-shelves/

# 68 ms, faster than 16.67%
# 18.6 MB, less than 13.64%

class Solution(object):
    def minHeightShelvesRec(self, books, shelf_width, space_left, current_height, total_height, cache):
        cached = cache.get((len(books), space_left), None)
        if cached != None:
            return cached[0] - cached[1] + total_height
        if space_left < 0:
            return float('inf')
        
        if not books:
            return total_height
        
        book_width,book_height = books[0]
        new_current_height = max(current_height, book_height)
        onThisShelf = self.minHeightShelvesRec(books[1:], shelf_width, space_left - book_width, new_current_height, total_height - current_height + new_current_height, cache)
        onNextShelf = self.minHeightShelvesRec(books[1:], shelf_width, shelf_width - book_width, book_height, total_height + book_height, cache)
        result = min(onThisShelf,onNextShelf)
        cache[(len(books), space_left)] = (result,total_height)
        return result
        
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        '''
        for every book, I can put it on the same shelf (if it fits) or on the next shelf
        
        height = min of
        put it on this shelf, call recursively with rest of books
        put it on next shelf, call recursively with rest of books
        * pass room left on this shelf
        '''
        
        return self.minHeightShelvesRec(books, shelf_width, shelf_width, 0, 0, {})
