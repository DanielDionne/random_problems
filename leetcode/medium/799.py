# 799. Champagne Tower
# https://leetcode.com/problems/champagne-tower/

#  116 ms, faster than 54.35%
# 13.9 MB, less than 13.04%

class Solution(object):
    def champagneTowerRec(self, poured, query_row, query_glass,cache):
        cached = cache.get((query_row,query_glass), None)
        if cached != None:
            return cached
        if query_glass < 0 or query_glass > query_row:
            return 0.0
        if query_row == 0:
            return float(poured)
        left_parent  = max(0.0,(self.champagneTowerRec(poured, query_row-1, query_glass  , cache)-1)/2.0)
        right_parent = max(0.0,(self.champagneTowerRec(poured, query_row-1, query_glass-1, cache)-1)/2.0)
        result = left_parent + right_parent
        cache[(query_row,query_glass)] = result
        return result
        
        
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        
        '''
        I can calculate how much each cup has this way:
            (cup above - 1) / 2 + (other cup above - 1) / 2
        '''
        return min(self.champagneTowerRec(poured, query_row, query_glass, {}),1.0)