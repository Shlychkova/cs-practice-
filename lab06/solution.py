def count_items(values:list)->dict:
    counts={}
    for value in values:
        counts[values]= counts.get(value, 0) + 1
    return counts
