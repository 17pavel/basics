class NameDescriptor:

    @staticmethod
    def validate_name(name):
        if not isinstance(name, str):
            raise TypeError(f"Имя должно быть строкой, а получено: {name}")
        if len(name) < 2:
            raise TypeError(
                f"Имя должно быть длиннее, чем {2} символов. name: {name}")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate_name(value)
        return setattr(instance, self.name, value)


class AgeDescriptor:

    @staticmethod
    def validate_age(age):
        if not isinstance(age, int):
            raise TypeError(f"Возраст - целое число, а получено: {age}")
        if age > 22 or age < 0:
            raise TypeError(f"Возраст от 0 до 21, а получено  {age}")

    def __set_name__(self, owner, age):
        self.age = "_" + age

    def __get__(self, instance, owner):
        return getattr(instance, self.age)

    def __set__(self, instance, value):
        self.validate_age(value)
        return setattr(instance, self.age, value)


class Dog:
    __TYPE_ANIMAL = "Собака"
    name = NameDescriptor()
    age = AgeDescriptor()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.__TYPE_ANIMAL} | name: {self.name} | age: {self.age}"


class Cat:
    __TYPE_ANIMAL = "Кот"
    name = NameDescriptor()
    age = AgeDescriptor()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.__TYPE_ANIMAL} | name: {self.name} | age: {self.age}"


dog1 = Dog("Тузик", 2)
print(vars(dog1))
print(dir(dog1))
cat = Cat("Мурзик", 6)
cat.name = "Том"
cat.__name = "gjh"
print(vars(cat))
print(dir(cat))
print()
