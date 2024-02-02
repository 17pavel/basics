class Cat:
    __slots__ = ("_name", "_age")

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Cat({self.name}, {self.age})"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 2:
            raise AttributeError(f"Имя это строка длиной 2 и более | {value}")
        self._name = value

    @property
    def age(self):
        """The age property."""
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0 or value >= 21:
            raise AttributeError(f"Возраст это целое число от 1 до 20 | {value}")
        else:
            self._age = value


cat = Cat("tom", 5)
print(cat.__repr__)
print(dir(cat))
