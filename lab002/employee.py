class Employee:

    def __init__(self, title, yearsWorked):
        self.title = title
        self.yearsWorked = yearsWorked

    def setTitle(self, title):
        self.title = title

    def setYearsWorked(self, yearsWorked):
        self.yearsWorked = yearsWorked

    def getTitle(self):
        return self.title

    def getYearsWorked(self):
        return self.yearsWorked

    def getInfo(self):
        return "Title: {}, Years Worked: {}" \
               .format(self.title, self.yearsWorked)