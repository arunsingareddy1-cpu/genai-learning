#find all duplicate elements in list
from enum import unique


lst = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8, 9, 10]
def find_duplicates(lst):
    duplicate = []
    for i in lst:
        if lst.count(i) > 1 and i not in duplicate:
            duplicate.append(i)
    return duplicate    
print(find_duplicates(lst))
#findall unique elements in list
def find_unique(lst):
    unique = []
    for i in lst:
        if lst.count(i) == 1:
            unique.append(i)
    return unique

print(find_unique(lst))

# count the no of duplicate values in list
def count_duplicates(lst):
    count={}
    for i in lst:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return {k:v for k,v in count.items() if v>1}

print(count_duplicates(lst))

#creae a list of all unique elements in list
def unique_elements(lst):
    unique = []
    for i in lst:
        if lst.count(i)==1:
            unique.append(i)

    return unique

print(unique_elements(lst))
