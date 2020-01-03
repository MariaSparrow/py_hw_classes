# common class - animals
class animals:
    hunger = 'yes'
    name = 'no'
    voice = 'no'
    list_name = []
    list_weight = []

    def eat(self):
        self.hunger = 'no'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.list_name.append(name)
        self.list_weight.append(weight)

    def change_voice(self):
        return self.voice


# class birds
class birds(animals):
    eggs = 0

    def add_eggs(self, value=1):
        self.eggs +=value

# class pets
class pets(animals):
    milk = 0

    def add_milk(self, value=1):
        self.milk +=value

goose1 = birds('Seriy', 10)
goose1.change_voice = 'ga-ga'
goose1.eat()
goose1.add_eggs(5)

goose2 = birds('Beliy',7)
goose2.change_voice = 'ga-ga'
goose2.eat()
goose1.add_eggs()

cow = pets('Manka', 50)
cow.add_milk()
cow.eat()
cow.change_voice = 'mu-mu'

sheep = pets('Барашек', 20)
sheep.eat()
sheep.change_voice = 'be-be'

sheep = pets('Кудрявый', 21)
sheep.eat()
sheep.change_voice = 'be-be'

chicken1 = birds('Ко-Ко', 5)
chicken1.change_voice = 'ko-ko'
chicken1.eat()
chicken1.add_eggs()


chicken2 = birds('Кукареку', 5)
chicken2.change_voice = 'ko-ko'
chicken2.eat()
chicken2.add_eggs()

goat = pets('Рога', 10)
goat.add_milk()
goat.eat()
goat.change_voice = 'me-me'

goat = pets('Копыта', 10)
goat.add_milk()
goat.eat()
goat.change_voice = 'me-me'

duck = birds('Кряква', 5)
duck.change_voice = 'krya'
duck.eat()
duck.add_eggs()


# самое тяжелое животное
print('самое тяжелое животное', animals.list_name[animals.list_weight.index(max(animals.list_weight))])

# общий вес всех животных
list_weight_sum = 0

for i in range(0, 10):
        # print(i)
        list_weight_sum += animals.list_weight[i]


print('общий вес животных ', list_weight_sum)