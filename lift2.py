pas_floor = []
lift = {
    "floor": 1,
    "direct": "up",
    "pas_lift": [],
}


def move(floor, direct):
    if direct == "up":
        floor += 1
    elif direct == "down":
        floor -= 1
    return floor


def call(pas_fl, dest):
    pas_floor.append({"floor": pas_fl, "destination": dest})
    print(f"Лифт вызвали с этажа {pas_fl}  на этаж {dest}.")


def on_floor(floor):
    print(f"Лифт прибыл на этаж {floor}.")
    if floor == 5:
        lift["direct"] = "down"
    if floor == 1:
        lift["direct"] = "up"
    for pas in pas_floor:
        if pas["floor"] != lift["floor"]:
            continue
        if lift["direct"] == "up" and pas["destination"] > floor:
            lift["pas_lift"].append(pas)
            print(f"Пассажир с {floor} до {pas['destination']} вошел в лифт.")
            pas["floor"] = str(floor)
        elif pas["destination"] < floor:
            lift["pas_lift"].append(pas)
            print(f"Пассажир с {floor} до {pas['destination']} вошел в лифт.")
            pas["floor"] = str(floor)
    for p in lift["pas_lift"]:
        if p["destination"] == floor:
            print(
                f"Пассажир с {p['floor']} до {p['destination']} этажа вышел из лифта."
            )
            p["destination"] = str(p["destination"])
    print("Лифт едит дальше.")
    lift["floor"] = move(lift["floor"], lift["direct"])


call(1, 3)
call(1, 5)
on_floor(1)
on_floor(2)
call(5, 1)
call(3, 4)
on_floor(3)
on_floor(4)
call(1, 4)
for i in (5, 4, 3, 2, 1, 2, 3, 4, 5):
    on_floor(i)
print(f"На этажах : {pas_floor}")
print(f"В лифте : {lift['pas_lift']}")
