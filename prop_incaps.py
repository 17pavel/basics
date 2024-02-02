class Dog:
    _MIN_AGE = 0
    _MAX_AGE = 40
    _MIN_NAME_LEN = 2

    @classmethod
    def _check_age(cls, age):
        if type(age) is not int:
            raise TypeError(f"Возраст может быть только числом, а получено: {age}")
        elif not (cls._MIN_AGE <= age <= cls._MAX_AGE):
            raise TypeError(
                f"Возраст может быть в диапазоне от {cls._MIN_AGE} до {cls._MAX_AGE}, а получено: {age}"
            )

    @classmethod
    def _check_name(cls, name):
        if not isinstance(name, str):
            raise TypeError(f"Имя должно быть строкой, а получено: {name}")
        if len(name) < cls._MIN_NAME_LEN:
            raise TypeError(
                f"Имя должно быть длиннее, чем {cls._MIN_NAME_LEN} символов. name: {name}"
            )

    def __init__(self, name, age):
        self._check_age(age)

        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._check_name(value)
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._check_age(value)
        self._age = value

    # def get_name(self):
    #     return self.__name
    #
    # def set_name(self, value):
    #     self.__name = value
    #
    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, value):
    #     self.__age = value

    def __str__(self):
        return f"name: {self.name} | age: {self.age}"


dog1 = Dog("Тузик", 5)
# dog1.set_age(10)
print(dog1.name)
dog1.age = 40
print(dog1.age)
dog1.name = "Az"
print(vars(dog1))
print(dir(dog1))
print()
