class CarDealer:
    def __init__(self, color, engine_capacity, number_of_doors, car_automation):
        self._color = color
        self._engine_capacity = engine_capacity
        self._number_of_doors = number_of_doors
        self._automation = car_automation

    def build_offer(self, budget):
        if budget > 30000:
            print(f"You can buy a Mercedes C Class with color {self._color} ")
        elif 30000 > budget > 10000:
            print(f"You can buy a Dacia Logan {self._color}")
        else:
            print("Your preferences are ignored but you can still buy a Dacia Logan. ")

    def automation_car(self, car_automation):
        self.car_automation = car_automation

        if car_automation >= 0 and car_automation < 1:
            print(f"Vintage car")
        elif car_automation >= 1 and car_automation < 2:
            print(f" The degree of automation of the car is: {car_automation}, small")
        elif car_automation >= 2 and car_automation < 3:
            print(f'The degree of automation of the car is:{car_automation}, medium')
        elif car_automation >= 3 and car_automation < 4:
            print(f'The degree of automation of car is :{car_automation}, medium')
        elif car_automation >= 4 and car_automation < 5:
            print(f'The degree of automation of car is:{car_automation}, high')
        elif car_automation >= 5 and car_automation < 6:
            print(f'The degree of automation of car is:{car_automation}, very good')
        else:
            print(f"No car")


automation = CarDealer("grey", 1.7, 5, 5)

dealer = CarDealer("red", 1.5, 5, 2)
dealer.build_offer(20000)
dealer.build_offer(35)
dealer.build_offer(100000)

x = CarDealer("grey", 1.7, 4, 2)
x.automation_car(1)
x.automation_car(2)
x.automation_car(3)
x.automation_car(4)
x.automation_car(5)


