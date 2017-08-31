# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(lists):
    best_ele = None
    best_len = 0
    cur_ele = None
    cur_len = 0
    for e in lists:
        if cur_ele != e:
            cur_ele = e
            cur_len = 1
        else:
            cur_len += 1
        if cur_len > best_len:
            best_ele = cur_ele
            best_len = cur_len
    return best_ele



#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None


