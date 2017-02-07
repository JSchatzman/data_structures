"""Implementation of Decision Tree."""

import csv
from math import log


with open('../flowers_data.csv') as f:
    data = [tuple(line) for line in csv.reader(f)]



class Node:
    """Representation of decision tree node."""

    def __init__(self,
                 column=-1,
                 value=None,
                 results=None,
                 next_true=None,
                 next_false=None):
        self.column = column
        self.value = value
        self.results = results
        self.next_true = next_true
        self.next_false = next_false


def dividedata(rows, column, value):
    """Return True if row is in first group else False."""
    def split_fun(row):
        if row[column] == value:
            return True
        return False
    split_setosa = [row for row in rows if split_fun(row)]
    split_versicolor = [row for row in rows if not split_fun(row)]
    return (split_setosa, split_versicolor)

split_setosa, split_versicolor = dividedata(data[1:], 5, 'setosa')

def uniquecount(rows):
    """Return the count of each flower type in a data set."""
    results = {'setosa': 0, 'versicolor': 0}
    for row in rows:
        if row[5] == 'setosa':
            results[row[5]] += 1
        else:
            results[row[5]] += 1
    return results

def calc_entropy(rows):
    """Return the entropy of a dataset."""
    def log2(x):
        return log(x) / log(2)
    results = uniquecount(rows)
    entropy = float(0)
    for flower_type in results.keys():
        p = float(results[flower_type]) / len(rows)
        import pdb; pdb.set_trace()
        entropy = entropy - p * log2(p)
    return entropy



# print(uniquecount(split_setosa))

#print(calc_entropy(data[1:]))
print(calc_entropy(split_setosa))
#print(calc_entropy(split_versicolor))



# print(data[2])
# print(uniquecount(data[1:]))


#