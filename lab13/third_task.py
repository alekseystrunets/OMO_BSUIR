
class Pet:
    def __init__(self, name):
        self.name = name

    def sound_of_pet(self):
        raise NotImplementedError("Метод должен быть переопределен в другом классе!")

    def info_about_pet(self):
        return f"Кличка: {self.name}"


class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound_of_pet(self):
        return "Гав-гав!"

    def info_about_pet(self):
        return f"{super().info_about_pet()}, Порода: {self.breed}, Звук: {self.sound_of_pet()}"


class Cat(Pet):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound_of_pet(self):
        return "Мяу!"

    def info_about_pet(self):
        return f"{super().info_about_pet()}, Порода: {self.breed}, Звук: {self.sound_of_pet()}"


class Parrot(Pet):
    def __init__(self, name, able_to_speak, color):
        super().__init__(name)
        self.able_to_speak = able_to_speak
        self.color = color

    def sound_of_pet(self):
        if self.able_to_speak:
            return "Привет!"
        else:
            return "Чик-чик"

    def info_about_pet(self):
        return f"{super().info_about_pet()}, Может говорить: {self.able_to_speak}, Звук: {self.sound_of_pet()}, Цвет: {self.color}"


dog = Dog("Тео", "Шпиц")
cat = Cat("Пух", "Вислоухий")
parrot = Parrot("Кеша", True, "Голубой")

print(dog.info_about_pet())
print(cat.info_about_pet())
print(parrot.info_about_pet())