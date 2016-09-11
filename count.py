def count(sequence, item):
    found = 0
    for i in sequence:
        if i == item:
            found += 1
        print item
    return found
count([6, 2, 3, 4, 5, 6],6)