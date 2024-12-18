S = {1, 2, 3, 4, 66, 6, 6,}   
# let print S
print(S)  # it count 6 one time only beacuse set contain unique value means non-repetive value .

# len()
length = len(S)  # it will give length of set 'S'
print(length)

# remove() 
S.remove(4)  
print(S)

# pop()
S.pop()
print(S) 

# clear()
new_set = {3,5,6,7,'name'}
print(new_set)
new_set.clear()
print("After applying cl, 2, 3, 4, 66, 6, 6,} clear(): ", new_set)

# union() -it will take union (adding all value one time)
S2 = {44, 5}
unionSet = S.union(S2)  #   {1, 2, 3, 4, 66, 6, 6,}  union {44,5}  - it will combine both you can think like it add value os S2 in S
print(unionSet)

# intersetion()  - it is opposite to union (it take only common value)
print(S.intersection(S2))  #it will give an empty set beascue there is no common value. 