class demo:
    def  work(self):
        print("One - parameter")
    def work(self,name):
        self.name="Jaga"
        print('two parameter constructor')
    def work(self,name,age):
        print('three parameter constructor')
        print(name)
d=demo()
d.work('raja',26)

 #Method overloading is not possible in python.
 #While performing method overloading in python ,the last defined method can be invoked and the previous methods becomes useless as we cannot invoke them.
