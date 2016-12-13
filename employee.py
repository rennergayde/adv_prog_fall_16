

class Employee:
# Common base class for all employees
    empCount = 0
    ishCount = 0
    mattCount = 0
    payroll = 0

    def __init__(self, name, salary, title):
        self.name = name
        self.salary = salary
        self.title = title
        Employee.empCount += 1
        Employee.payroll += self.salary
        if title == "Ishmael":
            Employee.ishCount += 1
            return
        elif title == "Matthew":
            Employee.mattCount += 1
            return
        else:
            print "Please enter an accepted title"
            return


    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name,  ", Salary: ", self.salary, "Title: ", self.title

#This would create first object of Employee class
emp1 = Employee("Jane", 2000, "Ishmael")
#This would create second object of Employee class
emp2 = Employee("Nick", 5000, "Matthew")
emp3 = Employee("Kim", 500, "Ishmael")
emp4 = Employee("Simon", 10, "Matthew")
emp5 = Employee("Max", -2000, "Ishmael")

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()
emp5.displayEmployee()

print "Total Employees: %d" % Employee.empCount
print "Total Ishmaels: %d" % Employee.ishCount
print "Total Matthews: %d" % Employee.mattCount
print "Payroll: %d" % Employee.payroll
