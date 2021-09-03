if __name__ == '__main__':
    scores = []
    namescore = {}
    for i in range(int(input())):
        name = input()
        score = float(input())
        
        scores.append(score)    
        namescore[name] = score   
           
    second_lowest = list(sorted(set(scores)))
    
    sortedname = sorted(namescore.keys() ,key = lambda x:x)
    
    for i in sortedname:
        if namescore.get(i) == second_lowest[1]:
            print(i)
