class World:
    def __int__(self, country):
        self._country = country

    def salary(self, budget):
        if budget > 150000:
            print(f"Your work country is {self._country} (salar/month) CHF")
        elif budget < 80000:
            print(f"Not work for them")
        else:
            print(f"No way")


x = World('Switzerland')
x.salary(25)
x.salary(150880)
x.salary(750090)
