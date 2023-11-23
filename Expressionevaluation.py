1.len(str(10<20))
2.4*len("problem1")/(len("python")%3)+2.0 #division by zero error
3.len('twenty four')/len('twenty')+2*(-1)**3)#-0.16666666666666674
4.3<10 or 5 #true
5.3<(10 or 2)#true
6.3<(10 and 2)#false
7.(5<100/0) and (10<100)#division by zero error
8.len("hello")==25/5 or 20/10#true
9.str((5<10)and(10<5)or(3<18) and  not 8<18)#false
10."str(2**4**2)" #str(2**4**2)
11.bool(4-len("four')#false
12.bool(1**10) #true
13.2/int(1.5)+200#202.0
14.10.0**350#(34, 'Result too large')
15.Write a Program that asks for your height in cm and then converts your height to feet and inches.(1 foot=12 inches,1 inch=2.54cm).
              
height=float(input("Enter the height in cm"))
inches=height/2.54
foot=inches/12
print("inches :",inches,"foot :",foot)
