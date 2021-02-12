'''  
Name:        ArithmeticCombinationToTarget
Description: Given a String and an int as Input and a target, using standard integer arithmetic 
             operators +, -, how many different solutions can you find by inserting the operators
             between some digits?
Example:     INPUT = "123456789". TARGET = 100
             OUTPUT: All combinations with '+' and '-' that sums up to 100:
             -1+2-3+4+5+6+78+9
             1+2+3-4+5+6+78+9
             1+2+34-5+67-8+9
             1+23-4+5+6+78-9
             1+23-4+56+7+8+9
             12+3+4+5-6-7+89
             12+3-4+5+67+8+9
             12-3-4+5-6+7+89
             123+4-5+67-89
             123+45-67+8-9
             123-4-5-6-7+8-9
             123-45-67+89

'''
def count_combinations(nums, target, operation):
    if not nums:
        if target == 0:
            print(''.join(operation))
        return target == 0
    result = 0
    
    # add this number
    operation.append('+{}'.format(nums[0]))
    result += count_combinations(nums[1:], target - nums[0], operation)
    operation.pop()
    
    # subtract this number
    operation.append('-{}'.format(nums[0]))
    result += count_combinations(nums[1:], target + nums[0], operation)
    operation.pop()
    
    # combine this number
    if len(nums) > 1:
        new_number = nums[0] * 10 + nums[1]
        result += count_combinations([new_number] + nums[2:], target, operation)
    return result

def combinations(nums_str, target):
    return count_combinations(map(int,nums_str), target, [])

result = combinations('123456789', 100)
print('Total {}'.format(result))
'''
Output:
+1+2+3-4+5+6+78+9
+1+2+34-5+67-8+9
+1+23-4+5+6+78-9
+1+23-4+56+7+8+9
-1+2-3+4+5+6+78+9
+12+3+4+5-6-7+89
+12+3-4+5+67+8+9
+12-3-4+5-6+7+89
+123+4-5+67-89
+123-4-5-6-7+8-9
+123+45-67+8-9
+123-45-67+89
Total 12
'''