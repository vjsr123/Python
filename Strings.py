'''s1=input("Enter the String")
ch=input("Enter the character")
for i in s1:
    if ch!=char(i):
        print(ch)'''
'''
lst=list(eval(input("Enter the elements in the list")))
print(min(lst))
print(max(lst)) '''

'''
for i in range(3):
    for j in range(6):
        print('*',end=' ')
    print() '''
'''
n=int(input("Enter no.of rows"))
for i in range(n):
    for j in range (i+1):
        print('*',end=' ')
    print()
    '''
n=int(input("Enter no.of rows"))
for i in range (n):
    for j in range (n-i):
         print('*',end=' ')
    print()
 
