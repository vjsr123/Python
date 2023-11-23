class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def work(self):
        print(self.name,"is Working")
    def play(self):
        print(self.name,"is Playing")
emp1=employee("Jaga",23,46000)
emp1.work()
emp1.play()
emp2 = employee("Raja",27,47000)
emp2.work()
emp2.play()
