class Employee:
    def __init__(self):
        self.working_hours = 0
    def WorkingHrs(self):
        self.working_hours = 50
    def printHrs(self):
        print("Working Hours:", self.working_hours)
class Trainee(Employee):
    def WorkingHrs(self):
        self.working_hours = 60
    def resetHrs(self):
        super().WorkingHrs()
employee = Employee()
employee.WorkingHrs()
print("Employee")
employee.printHrs()
trainee = Trainee()
trainee.WorkingHrs()
print("Trainee")
trainee.printHrs()
trainee.resetHrs()
print("Trainee(after reset):")
trainee.printHrs()