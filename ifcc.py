#1.WAPP to check whether the number is present between 1-10
num=int(input('Enter the number'))
if num>=1 and  num<=10:
    print("yes it is in the range 1-10")
else:
    print("No,It is not in the range of 1-10")
#2.WAPP to check ehether a number is divisible by 5 or not.
num=int(input("Enter the number"))
if num%5==0:
    print(num,"is divisible by 5")
else:
    print(num,"is not divisible by 5")
#3.WAPP to check whether a number is even or odd.
num=int(input("Enter the input"))
if num%2==0:
    print("Even Number")
else:
    print("Odd Number")

#
string = str(input("Enter a String"))
for ch in string:
    if ch in 'aeiouAEIOU':
        print(ch,end='',"are the vowels present in the string given by the user")
            
 


