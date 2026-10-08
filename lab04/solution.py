def winner(names,scores):
    maxr=0
    max=-100000
    for i in range(len(scores)):
        if scores[i]>max:
            maxr=i
            max=scores[i]
    return names[maxr]

names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]
print(winner(names,scores))
