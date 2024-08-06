class House:
    def __init__(self, name, num_flor):
        self.name = name
        self.numbers_of_floors = num_flor

    def go_to(self, new_floor):
        if new_floor > self.numbers_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for floor in range(1, new_floor+1):
                print(floor)


    # def gde_jil(self):
    #     print ( f' Я живу в {self.name} на {self.numbers_of_floors} ' )
    # def go_to(self):
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
# h1.gde_jil()
h1.go_to(5)
h2.go_to(10)
#print(f' Я живу в {self.name} на {self.numbers_of_floors} ')
