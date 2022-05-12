class Salary:
    def __init__(self, pay):
        self._pay = pay

    def get_total(self):
        return (self._pay * 12) / 4.95


class Employee:
    def __init__(self, pay, bonus):
        self._pay = pay
        self._bonus = bonus

    def annual_salary(self):
        second_bonus = 1000
        return "Total salaries " + str(self._pay.get_total() + self._bonus + second_bonus)


x = Salary(8988989898)
y = Salary(8567875478)
z = Salary(898232)
e = Employee(z, 10000)
print(e.annual_salary())
