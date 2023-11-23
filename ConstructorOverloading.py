class employee:
    def __init__(self):
        print("Inside  1 constuctor")
    def __init__(self,name):
        print("Inside 2 constructor")
    def __init__(self,name,salary):
        print("inside 3 constructor")
        print(name)
#e=employee()
e=employee('Jaga',55000)

#Constructor chaining also not possible in python.
