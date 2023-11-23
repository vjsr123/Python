s1={10,20,30,40,50}
#Set is not an ordered collection of data
#Set do not allow duplicates
#Set does not allow indexing of numbers
s1.add(500)
print(s1)
s1.remove(500)
print(s1)

#s1.remove(600) #error
s1.discard(600)
del s1

s1={1,2,3}
s2={3,4,5}
union_set=s1.union(s2)
print(s1.intersection(s2))
print(len(s1))
