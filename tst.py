lst1 = [1,2,3]
lst2 = [1,1,3]

print(sum([i != j for i,j in zip(lst1, lst2)]))
