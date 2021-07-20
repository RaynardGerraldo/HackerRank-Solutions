if __name__ == '__main__':
    name_score = []
    vals = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        name_score.append([])
        name_score[_].append(name),name_score[_].append(score)
        
    name_score.sort(),name_score.sort(key = lambda x: x[1])
    
    vals = [name_score[i][1] for i in range(len(name_score))]
    
    the_count = vals.count(vals[0])
    
    for i in range(len(name_score)):
        if len(name_score) > 3 and len(vals) > 3:
            if name_score[i][1] == name_score[0][1]:
                pass

            elif name_score[i][1] == name_score[i-1][1]:
                if name_score[i][1] < name_score[-1][1]:
                    print(name_score[i][0])
                
            elif name_score[i][1] >= name_score[i-1][1]:
                if name_score[i][1] > name_score[i-1][1]:
                    if name_score[i-1][1] == name_score[0][1]:
                        print(name_score[i][0])
                    else:
                        pass
                    
                elif name_score[i][1] >= name_score[-1][1]:
                    if the_count >= 2:
                        pass
                    else:
                        print(name_score[i][0])
                        
                else:
                    print(name_score[i][0])
            else:
                print(name_score[i][0])        


        else:
            if name_score[i][1] > min(vals) and name_score[i][1] == max(vals):
                print(name_score[i][0])
