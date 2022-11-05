if __name__ == '__main__':
    
    nested = []
    scores = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        nested.append([name, score])
        scores.append(score)
        
    minScore = min(scores)
    
    newSortedScores = [x for x in scores if x!= minScore]
    
    final = [i for i,j in nested if j== min(newSortedScores)]
    
    sortedFinal = final.sort()
    
    for i in range(len(final)):
        print(final[i])
        
