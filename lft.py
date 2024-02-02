lift = {"floor": 1, "direct": "up", "pas": []}


def move(floor, direct):
    if direct == "up":
        floor += 1
    elif direct == "down":
        floor -= 1
    return floor


def call(floor, dest):
    if lift["direct"] == "up" and floor >= lift["floor"]:
        lift["pas"].append({"floor": floor, "dest": dest})
        print(f"Лифт вызвали с {floor} до {dest}.")
    elif lift["direct"] == "down" and floor <= lift["floor"]:
        lift["pas"].append({"floor": floor, "dest": dest})
        print(f"Лифт вызвали с {floor} до {dest}.")


def on_floor(floor):
    if floor == lift["floor"]:
        print(f"Лифт на {floor} этаже.")
        for p in lift["pas"]:
            if p["floor"] == floor:
                print(f"Пассажир с {p['floor']} до {p['dest']} вошел в лифт.")
            if p["dest"] == floor:
                lift["pas"].remove(p)
                print(
                    f"Пассажир с {p['floor']} до {p['dest']} вышел из лифта.")
    if floor == 9:
        lift["direct"] = "down"
    if floor == 1:
        lift["direct"] = "up"

    print("Лифт едит дальше")
    lift["floor"] = move(lift["floor"], lift["direct"])


call(1, 7)
call(3, 6)
call(2, 5)
for i in range(1, 10):
    on_floor(i)
call(8, 3)
call(5, 1)
for i in range(8, 0, -1):
    on_floor(i)


print(lift)
print()
