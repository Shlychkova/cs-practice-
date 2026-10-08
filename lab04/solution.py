def winner(names,scores):
    maxr=0
    max=-100000
    for i in range(len(scores)):
        if scores[i]>max:
            maxr=i
            max=scores[i]
    return names[maxr]
def average(scores):
    psp=0.0
    sr=0
    count=0
    for k in range(len(scores)):
        sr=scores[k]+sr
    return round(sr/len(scores),2)
def ranking(names,scores):
    lt=[]
    sortsc=sorted(scores,reverse=True)
    for i in range(len(sortsc)):
        for j in range(len(sortsc)):
            if (sortsc[i]==scores[j])and (names[j] not in lt):
                lt.append(names[j])
    return lt
names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]
print(winner(names,scores))
print(average(scores))
print(ranking(names,scores))
