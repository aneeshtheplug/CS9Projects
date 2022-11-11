from employee import Employee
class Teacher(Employee):
    def __init__(self, title, yearsWorked, subject):
        super().__init__(title, yearsWorked)
        self.subject = subject
    
    def getSubject(self):
        return self.subject 

    def setSubject(self,subject):
        self.subject = subject
    
    def getInfo(self):
        return "Title: {}, Years Worked: {}, Subject: {}" \
               .format(self.title, self.yearsWorked, self.subject)

    def __ge__(self, teacher):
        return self.yearsWorked >=  teacher.yearsWorked

t1 = Teacher("Teacher", 4, "Biology")
t2 = Teacher("Teacher", 3, "Chemistry")
t3 = Teacher("Teacher", 3, "Math")

assert t1.getInfo() == \
       "Title: Teacher, Years Worked: 4, Subject: Biology"
assert t2.getInfo() == \
       "Title: Teacher, Years Worked: 3, Subject: Chemistry"
assert t3.getInfo() == \
       "Title: Teacher, Years Worked: 3, Subject: Math"

assert (t1 >= t2) == True
assert (t1 >= t3) == True
assert (t2 >= t1) == False
assert (t2 >= t3) == True
assert (t3 >= t1) == False
assert (t3 >= t2) == True
