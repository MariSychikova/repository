import json


FILENAME = 'input.json'


def task() -> float:
    with open(FILENAME) as file:
        data = json.load(file)

    list_prods = [dict_["score"] * dict_["weight"] for dict_ in data]

    return round(sum(list_prods), 3)


print(task())
