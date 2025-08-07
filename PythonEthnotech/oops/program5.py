class Mark:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def avg_score(self):
        sum =0
        for val in self.marks:
            sum+=val
        print("Hello",self.name,"and your score is :",sum/3)

s1= Mark("Tower",[98,90,95])
s1.avg_score()

s1.name="Ravi Tower" # even we can modify the object attributes
s1.avg_score()

s1.marks=[35,45,56]
s1.avg_score()