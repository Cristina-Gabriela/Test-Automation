class Salary:
    def __init__(self, pay):
        self._pay = pay

    def get_total(self):
        return (self._pay * 12) / 4.95


class Employee:
    def __init__(self, pay, bonus):
        self._bonus = bonus
        self.object_salary = Salary(pay)

    def annual_salary(self):
        second_bonus = 1000
        return "Total salaries: " + str(self.object_salary.get_total() + self._bonus + second_bonus)

object_salary = Salary(565656558)
print(object_salary.get_total())

employee = Employee(999999999, 88888888)
print(employee.annual_salary())
print(employee.annual_salary())


