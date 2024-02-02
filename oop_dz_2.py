class Products:

    def __init__(self, products: dict, bonus: int = 0):
        self.products = products
        self.bonus = bonus

    def sum_price(self):
        price = 0
        for v in self.products.values():
            price += v
        return price - self.bonus

    def __add__(self, other):
        if isinstance(other, int):
            return Products(self.products, self.bonus - other)
        elif isinstance(other, Products):
            new = self.products.copy()
            for k, v in other.items():
                if k in new:
                    new[k] += v
                else:
                    new[k] = v
            return Products(new, self.bonus + other.bonus)

    def __radd__(self, other):
        if isinstance(other, int):
            return Products(self.products, self.bonus + other)

    def __eq__(self, other):
        return self.products == other.products

    def __ge__(self, other):
        if isinstance(other, Products):
            return self.sum_price() >= other.sum_price()
        else:
            raise TypeError

    def __str__(self):
        return f"{self.products} | {self.bonus}"

    def __repr__(self):
        return f"Products({self.products}, {self.bonus})"

    def __contains__(self, item):
        return item in self.products

    def __getitem__(self, key):
        return self.products[key]

    def items(self):
        return self.products.items()

    def __sub__(self, other):
        if isinstance(other, int):
            return Products(self.products, self.bonus - other)
        elif isinstance(other, Products):
            new = self.products.copy()
            for k, v in other.items():
                if k in new and new[k] > v:
                    new[k] -= v
                else:
                    new[k] = 0
            return Products(
                new, (self.bonus - other.bonus if self.bonus > other.bonus else 0)
            )

    def __rsub__(self, other):
        if isinstance(other, int):
            return Products(
                self.products, (other - self.bonus if other > self.bonus else 0)
            )


prod1 = Products({"Молоко": 3, "Хлеб": 2}, 5)
prod2 = Products({"Колбаса": 10, "Молоко": 5}, 2)
print(prod1 + prod2)
print(f"Итого: {prod2.sum_price()} руб")
print(prod1 - prod2)
prod3 = prod2 - prod1
print(prod3)
print(f"Итого: {prod3.sum_price()} руб")
# __sub__ __rsub__
# print(prod1.sum_price())
# print(prod2.sum_price())
