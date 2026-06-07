"https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true"
'''
Ques:
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    unique_score = set(arr)
    
    sorted_scores = sorted(list(unique_score))
    
    print(sorted_scores[-2])

'''
-map(int, input().split()): Takes the string input "2 3 6 6 5", splits it by spaces into ['2', '3', '6', '6', '5'], and converts each string into an integer.
-set(arr): A Python set cannot contain duplicate items. Passing our scores into a set automatically collapses the duplicates
-sorted(...): This sorts the unique numbers in ascending (increasing) order:[2, 3, 5, 6]
[-2]: Python supports negative indexing, where -1 is the last element (the winner) and -2 is the second-to-last element (the runner-up). In our sorted list [2, 3, 5, 6], index -2 points directly to 5.
'''
