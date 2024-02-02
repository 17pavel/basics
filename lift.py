def move(floor):
    if floor == 1:
        lift["direction"] = "up"
    if floor == 5:
        lift["direction"] = "down"

    if lift["direction"] == "up" and floor < 5:
        floor += 1
    else:
        floor -= 1
    return floor


def call(pas_fl, dest):
    passengers_floor.append({"floor": pas_fl, "destination": dest})
    print(f"Лифт вызвали с этажа {pas_fl}  на этаж {dest}.")


def on_floor(floor):
    print(f"Лифт прибыл на этаж {floor}.")
    for pas in passengers_floor:
        if pas["floor"] != lift["floor"]:
            continue
        if lift["direction"] == "up" and pas["destination"] > floor:
            lift["passengers_lift"].append(pas)
            print(f"Пассажир с {floor} до {pas['destination']} вошел в лифт.")
            pas["floor"] = str(floor)
        elif pas["destination"] < floor:
            lift["passengers_lift"].append(pas)
            print(f"Пассажир с {floor} до {pas['destination']} вошел в лифт.")
            pas["floor"] = str(floor)
    for p in lift["passengers_lift"]:
        if p["destination"] == floor:
            print(
                f"Пассажир с {p['floor']} до {p['destination']} этажа вышел из лифта."
            )
            p["destination"] = str(p["destination"])
    print("Лифт едит дальше.")
    lift["floor"] = move(lift["floor"])


# Пример использования
passengers_floor = []
lift = {
    "floor": 1,
    "direction": "up",
    "passengers_lift": [],
}

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
print(f"На этажах : {passengers_floor}")
print(f"В лифте : {lift['passengers_lift']}")
