"https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true"
'''
Ques:
Given: 3 integers x,y,z representing the dimensions of an cuboid along with an integer n, find all the possible combinations
given by (i, j, k) where i + j + k != n 
Here we have to use list comprehensions instead of multipal loops
'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # The list comprehension magic:
    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
    print(coordinates)

'''
here:
- i,j,k is the output expression
- [for i in range (x+1)]: represents that the value should stop iterating at x
- [for j in range (y+1)]: middle loop running entirely for every iteration of 'i'
- [for k in range (z+1)]:innermost loop running entirely on every interation of 'j'
- if (i + j + k) != n, code throws the combination away if all the integers are equal to n.
'''
