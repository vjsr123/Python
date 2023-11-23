names=['raja','jaga','madhu','mahesh','ranjith']
print([i for i in names if i[0]=='r'])

for i in range(1,11):
    if i==5:
        break
    print(i,end=' ')

for i in range(1,11):
    if i==7:
        continue
    print(i)
