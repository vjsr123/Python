for i in range(1,11,1):
    print(i,end=' ')
#_____________________________________________________________________________________________________
print(range(1,11,1))
'''#______________________________________________
count=int(input("Enter the no.of elements"))
lst=[]
for i in range(count):
    ele=int(input("Enter the elememts"))
    lst.append(ele)
print(lst)
even_lst=[]
for i in lst:
    if i%2==0:
        even_lst.append(i)
print(even_lst)
'''    
#____________________________________________________________________________________________
lst2=[10,20,30,40,50,67,89]
even_lst=[i for i in lst2 if i%2==0]
print(even_lst)
#_____________________________________________________________________________________________________________
#list compression:
names=['raja','jaga','madhu','mahesh','ranjith']
print([i for i in names if i[0]=='r'])

#break statement:
for i in range(1,11):
    if i==5:
        break
    print(i,end=' ')
    
#continue statement:
for i in range(1,11):
    if i==7:
        continue
    print(i,end=' ')
