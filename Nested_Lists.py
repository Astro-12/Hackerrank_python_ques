if __name__ == '__main__':
    students = []
    
    # Read input and store as [name, score] pairs
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    scores = sorted(list(set(score for name, score in students)))
    second_lowest = scores[1]
    
    names = sorted(name for name, score in students if score == second_lowest)
    
    # Print each matching name on a new line
    for name in names:
        print(name)
