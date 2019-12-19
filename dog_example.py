class Dog:
    """ просто класс замечательной собаки"""
    def bark(self):
        print("Гав")
        pass
    pass




# давайте создадаим экземпляр собаки
sizzles = Dog()
sizzles.bark()



class Dog_with_Name:
    """ это просто собака  у которой еще есть и и имя и температура"""
    def __init__(self, petname, temp):
        self.name = petname
        self.temp = temp

    def status(self):
        print("имя собаки: ",  self.name)
        print("температура собаки:", self.temp)
        pass

    def setTemperature(self, temp):
        self.temp = temp;
        pass
    def bark(self):
        print('woof')
        pass
    pass


# Теперь мы можем создать новый экземпляр нашего класса
lassie = Dog_with_Name("Lassie", 37)
lassie.status()